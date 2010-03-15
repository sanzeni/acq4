# -*- coding: utf-8 -*-
from __future__ import with_statement
from PatchTemplate import *
from PyQt4 import QtGui, QtCore
#from PyQt4 import Qwt5 as Qwt
from WidgetGroup import WidgetGroup
from pyqtgraph.PlotWidget import PlotWidget
from metaarray import *
from Mutex import Mutex, MutexLocker
import traceback, sys, time
from numpy import *
import scipy.optimize
from lib.util.debug import *
from functions import siFormat
from lib.Manager import getManager


class PatchWindow(QtGui.QMainWindow):
    def __init__(self, dm, clampName):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle(clampName)
        self.startTime = None
        
        self.analysisItems = {
            'inputResistance': u'Ω', 
            'accessResistance': u'Ω',
            'capacitance': 'F',
            'restingPotential': 'V', 
            'restingCurrent': 'A', 
            'fitError': ''
        }
        
        self.params = {
            'mode': 'vc',
            'rate': 200000,
            'downsample': 20,
            'cycleTime': .2,
            'recordTime': 0.1,
            'delayTime': 0.03,
            'pulseTime': 0.05,
            'icPulse': -10e-12,
            'vcPulse': -10e-3,
            'icHolding': 0,
            'vcHolding': -50e-3,
            'icHoldingEnabled': False,
            'icPulseEnabled': True,
            'vcHoldingEnabled': False,
            'vcPulseEnabled': True
        }
        
        
        self.paramLock = Mutex(QtCore.QMutex.Recursive)

        self.manager = dm
        self.clampName = clampName
        self.thread = PatchThread(self)
        self.cw = QtGui.QWidget()
        self.setCentralWidget(self.cw)
        self.ui = Ui_Form()
        self.ui.setupUi(self.cw)

        self.stateFile = self.clampName + '_ui.cfg'
        uiState = getManager().readConfigFile(self.stateFile)
        if 'geometry' in uiState:
            geom = QtCore.QRect(*uiState['geometry'])
            self.setGeometry(geom)
        if 'window' in uiState:
            ws = QtCore.QByteArray.fromPercentEncoding(uiState['window'])
            self.restoreState(ws)


        self.plots = {}
        for k in self.analysisItems:
            p = PlotWidget()
            p.setLabel('left', k)
            self.ui.plotLayout.addWidget(p)
            self.plots[k] = p
        #irp = self.plots['inputResistance']
        #irp.setManualYScale()
        #irp.setYLog(True)
        #irp.setYRange(1e6, 1e11)
            
        
        
        
        self.stateGroup = WidgetGroup([
            (self.ui.icPulseSpin, 'icPulse', 1e12),
            (self.ui.vcPulseSpin, 'vcPulse', 1e3),
            (self.ui.icHoldSpin, 'icHolding', 1e12),
            (self.ui.vcHoldSpin, 'vcHolding', 1e3),
            (self.ui.icPulseCheck, 'icPulseEnabled'),
            (self.ui.vcPulseCheck, 'vcPulseEnabled'),
            (self.ui.icHoldCheck, 'icHoldingEnabled'),
            (self.ui.vcHoldCheck, 'vcHoldingEnabled'),
            (self.ui.cycleTimeSpin, 'cycleTime', 1),
            (self.ui.pulseTimeSpin, 'pulseTime', 1e3),
            (self.ui.delayTimeSpin, 'delayTime', 1e3),
        ])
        self.stateGroup.setState(self.params)
        
        #for p in [self.ui.patchPlot, self.ui.commandPlot]:
            #p.setCanvasBackground(QtGui.QColor(0,0,0))
            #p.replot()
            
        self.patchCurve = self.ui.patchPlot.plot(pen=QtGui.QPen(QtGui.QColor(200, 200, 200)))
        #self.patchCurve = PlotCurve('cell')
        #self.patchCurve.setPen(QtGui.QPen(QtGui.QColor(200, 200, 200)))
        #self.patchCurve.attach(self.ui.patchPlot)
        self.commandCurve = self.ui.commandPlot.plot(pen=QtGui.QPen(QtGui.QColor(200, 200, 200)))
        #self.commandCurve = PlotCurve('command')
        #self.commandCurve.setPen(QtGui.QPen(QtGui.QColor(200, 200, 200)))
        #self.commandCurve.attach(self.ui.commandPlot)
        
        QtCore.QObject.connect(self.ui.startBtn, QtCore.SIGNAL('clicked()'), self.startClicked)
        QtCore.QObject.connect(self.ui.recordBtn, QtCore.SIGNAL('clicked()'), self.recordClicked)
        QtCore.QObject.connect(self.ui.bathModeBtn, QtCore.SIGNAL('clicked()'), self.bathMode)
        QtCore.QObject.connect(self.ui.patchModeBtn, QtCore.SIGNAL('clicked()'), self.patchMode)
        QtCore.QObject.connect(self.ui.cellModeBtn, QtCore.SIGNAL('clicked()'), self.cellMode)
        QtCore.QObject.connect(self.ui.resetBtn, QtCore.SIGNAL('clicked()'), self.resetClicked)
        QtCore.QObject.connect(self.thread, QtCore.SIGNAL('finished()'), self.threadStopped)
        QtCore.QObject.connect(self.thread, QtCore.SIGNAL('newFrame'), self.handleNewFrame)
        #QtCore.QObject.connect(self.ui.icModeRadio, QtCore.SIGNAL('toggled(bool)'), self.updateParams)
        QtCore.QObject.connect(self.ui.vcModeRadio, QtCore.SIGNAL('toggled(bool)'), self.updateParams)
        QtCore.QObject.connect(self.stateGroup, QtCore.SIGNAL('changed'), self.updateParams)
                
        ## Configure analysis plots, curves, and data arrays
        self.analysisCurves = {}
        self.analysisData = {'time': []}
        for n in self.analysisItems:
            w = getattr(self.ui, n+'Check')
            QtCore.QObject.connect(w, QtCore.SIGNAL('clicked()'), self.showPlots)
            p = self.plots[n]
            #p.setCanvasBackground(QtGui.QColor(0,0,0))
            #p.replot()
            self.analysisCurves[n] = p.plot(pen=QtGui.QPen(QtGui.QColor(200, 200, 200)))
            for suf in ['', 'Std']:
                #self.analysisCurves[n+suf] = p.plot(pen=QtGui.QPen(QtGui.QColor(200, 200, 200)), replot=False)
                #self.analysisCurves[n+suf] = PlotCurve(n+suf)
                #self.analysisCurves[n+suf].setPen(QtGui.QPen(QtGui.QColor(200, 200, 200)))
                #self.analysisCurves[n+suf].attach(p)
                self.analysisData[n+suf] = []
        self.showPlots()
        self.updateParams()
        self.show()
    
    def quit(self):
        #print "Stopping patch thread.."
        geom = self.geometry()
        uiState = {'window': str(self.saveState().toPercentEncoding()), 'geometry': [geom.x(), geom.y(), geom.width(), geom.height()]}
        getManager().writeConfigFile(uiState, self.stateFile)
        
        self.thread.stop(block=True)
        print "Patch thread exited; module quitting."
        
    def closeEvent(self, ev):
        self.quit()
    
    def bathMode(self):
        self.ui.vcPulseCheck.setChecked(True)
        self.ui.vcHoldCheck.setChecked(False)
        self.ui.vcModeRadio.setChecked(True)
        self.ui.cycleTimeSpin.setValue(0.2)
        self.ui.pulseTimeSpin.setValue(50)
    
    def patchMode(self):
        self.ui.vcPulseCheck.setChecked(True)
        self.ui.vcHoldCheck.setChecked(True)
        self.ui.vcModeRadio.setChecked(True)
        self.ui.cycleTimeSpin.setValue(0.2)
        self.ui.pulseTimeSpin.setValue(50)
    
    def cellMode(self):
        self.ui.icPulseCheck.setChecked(True)
        self.ui.icModeRadio.setChecked(True)
        self.ui.cycleTimeSpin.setValue(0.2)
        self.ui.pulseTimeSpin.setValue(150)
    
    def showPlots(self):
        """Show/hide analysis plot widgets"""
        for n in self.analysisItems:
            w = getattr(self.ui, n+'Check')
            p = self.plots[n]
            if w.isChecked():
                p.show()
            else:
                p.hide()
        self.updateAnalysisPlots()
    
    def updateParams(self, *args):
        with self.paramLock:
            if self.ui.icModeRadio.isChecked():
                mode = 'ic'
            else:
                mode = 'vc'
            self.params['mode'] = mode
            state = self.stateGroup.state()
            for p in self.params:
                if p in state:
                    self.params[p] = state[p]
            self.params['recordTime'] = self.params['delayTime'] *2.0 + self.params['pulseTime']
        self.thread.updateParams()
        
    def recordClicked(self):
        if self.ui.recordBtn.isChecked():
            data = self.makeAnalysisArray()
            sd = self.storageDir()
            self.storageFile = sd.writeFile(data, self.clampName, autoIncrement=True, appendAxis='Time', newFile=True)
            
    def storageDir(self):
        return self.manager.getCurrentDir().getDir('Patch', create=True)
                
    #def storageFile(self):
        #sd = self.storageDir()
        #return sd.getFile(self.clampName, create=True)
            
        
    def resetClicked(self):
        for n in self.analysisData:
            self.analysisData[n] = []
        self.startTime = None
        
    def handleNewFrame(self, frame):
        with self.paramLock:
            mode = self.params['mode']
        
        data = frame['data'][self.clampName]
        #if mode == 'vc':
            #scale1 = 1e12
            #scale2 = 1e3
        #else:
            #scale1 = 1e3
            #scale2 = 1e12
        self.patchCurve.setData(data.xvals('Time'), data['primary'])
        self.commandCurve.setData(data.xvals('Time'), data['secondary'])
        #self.ui.patchPlot.replot()
        #self.ui.commandPlot.replot()
        
        for k in self.analysisItems:
            if k in frame['analysis']:
                self.analysisData[k].append(frame['analysis'][k])
                
        for r in ['input', 'access']:
            res = r+'Resistance'
            label = getattr(self.ui, res+'Label')
            resistance = frame['analysis'][res]
            label.setText(siFormat(resistance) + u'Ω')
        self.ui.restingPotentialLabel.setText(siFormat(frame['analysis']['restingPotential'], error=frame['analysis']['restingPotentialStd'], suffix='V'))
        self.ui.restingCurrentLabel.setText(siFormat(frame['analysis']['restingCurrent'], error=frame['analysis']['restingCurrentStd'], suffix='A'))
        self.ui.capacitanceLabel.setText('%sF' % siFormat(frame['analysis']['capacitance']))
        self.ui.fitErrorLabel.setText('%7.2g' % frame['analysis']['fitError'])
        
        if self.startTime is None:
            self.startTime = data._info[-1]['startTime']
        self.analysisData['time'].append(data._info[-1]['startTime'] - self.startTime)
        self.updateAnalysisPlots()
        
        ## Record to disk if requested.
        if self.ui.recordBtn.isChecked():
            
            arr = self.makeAnalysisArray(lastOnly=True)
            #print "appending array", arr.shape
            arr.write(self.storageFile.name(), appendAxis='Time')
        
    def makeAnalysisArray(self, lastOnly=False):
        ## Determine how much of the data to include in this array
        if lastOnly:
            sl = slice(-1, None)
        else:
            sl = slice(None)
            
        ## Generate the meta-info structure
        info = [
            {'name': 'Time', 'values': self.analysisData['time'][sl], 'units': 's'},
            {'name': 'Value', 'cols': []}
        ]
        for k in self.analysisItems:
            for s in ['', 'Std']:
                if len(self.analysisData[k+s]) < 1:
                    continue
                info[1]['cols'].append({'name': k+s, 'units': self.analysisItems[k]})
                
        ## Create the blank MetaArray
        data = MetaArray(
            (len(info[0]['values']), len(info[1]['cols'])), 
            dtype=float,
            info=info
        )
        
        ## Fill with data
        for k in self.analysisItems:
            for s in ['', 'Std']:
                if len(self.analysisData[k+s]) < 1:
                    continue
                try:
                    data[:, k+s] = self.analysisData[k+s][sl]
                except:
                    print data.shape, data[:, k+s].shape, len(self.analysisData[k+s][sl])
                    raise
                
        return data
            
            
        
    def updateAnalysisPlots(self):
        for n in self.analysisItems:
            p = self.plots[n]
            if p.isVisible():
                self.analysisCurves[n].setData(self.analysisData['time'], self.analysisData[n])
                #if len(self.analysisData[n+'Std']) > 0:
                    #self.analysisCurves[p+'Std'].setData(self.analysisData['time'], self.analysisData[n+'Std'])
                #p.replot()
    
    def startClicked(self):
        if self.ui.startBtn.isChecked():
            if not self.thread.isRunning():
                self.thread.start()
            self.ui.startBtn.setText('Stop')
        else:
            self.ui.startBtn.setEnabled(False)
            self.thread.stop()
            
    def threadStopped(self):
        self.ui.startBtn.setText('Start')
        self.ui.startBtn.setEnabled(True)
        self.ui.startBtn.setChecked(False)
        
        
class PatchThread(QtCore.QThread):
    def __init__(self, ui):
        self.ui = ui
        self.manager = ui.manager
        self.clampName = ui.clampName
        QtCore.QThread.__init__(self)
        self.lock = Mutex(QtCore.QMutex.Recursive)
        self.stopThread = True
        self.paramsUpdated = True
    
    def updateParams(self):
        with self.lock:
            self.paramsUpdated = True
    
    def run(self):
        """Main loop for patch thread. This is where protocols are executed and data collected."""
        try:
            with MutexLocker(self.lock) as l:
                self.stopThread = False
                clamp = self.manager.getDevice(self.clampName)
                daqName = clamp.config['commandChannel'][0]
                clampName = self.clampName
                self.paramsUpdated = True
                l.unlock()
                
                lastTime = None
                while True:
                    lastTime = time.clock()
                    
                    updateCommand = False
                    l.relock()
                    if self.paramsUpdated:
                        with self.ui.paramLock:
                            params = self.ui.params.copy()
                            self.paramsUpdated = False
                        updateCommand = True
                    l.unlock()
                    
                    ## Regenerate command signal if parameters have changed
                    numPts = int(float(params['recordTime']) * params['rate'])
                    mode = params['mode']
                    if params[mode+'HoldingEnabled']:
                        holding = params[mode+'Holding']
                    else:
                        holding = 0.
                    if params[mode+'PulseEnabled']:
                        amplitude = params[mode+'Pulse']
                    else:
                        amplitude = 0.
                    cmdData = empty(numPts)
                    cmdData[:] = holding
                    start = int(params['delayTime'] * params['rate'])
                    stop = start + int(params['pulseTime'] * params['rate'])
                    cmdData[start:stop] = holding + amplitude
                    #cmdData[-1] = holding
                    
                    cmd = {
                        'protocol': {'duration': params['recordTime'], 'leadTime': 0.02},
                        daqName: {'rate': params['rate'], 'numPts': numPts, 'downsample': params['downsample']},
                        clampName: {
                            'mode': params['mode'],
                            'command': cmdData,
                            'holding': holding
                        }
                        
                    }
                    
                    
                    ## Create and execute task.
                    ## the try/except block is just to catch errors that come up during multiclamp auto pipette offset procedure.
                    exc = False
                    count = 0
                    while not exc:
                        count += 1
                        try:
                            ## Create task
                            task = self.manager.createTask(cmd)
                            ## Execute task
                            task.execute()
                            exc = True
                        except:
                            err = sys.exc_info()[1].args
                            #print err
                            if count < 5 and len(err) > 1 and err[1] == 'ExtCmdSensOff':  ## external cmd sensitivity is off, wait to see if it comes back..
                                time.sleep(1.0)
                                continue
                            else:
                                raise
                    #print cmd
                    
                    ## analyze trace 
                    result = task.getResult()
                    #print result[clampName]['raw'].max(), result[clampName]['raw'].min()
                    
                    #print result[clampName]
                    analysis = self.analyze(result[clampName], params)
                    frame = {'data': result, 'analysis': analysis}
                    
                    self.emit(QtCore.SIGNAL('newFrame'), frame)
                    
                    ## sleep until it is time for the next run
                    c = 0
                    stop = False
                    while True:
                        ## check for stop button every 100ms
                        if c % 100 == 0:
                            l.relock()
                            if self.stopThread:
                                l.unlock()
                                stop = True
                                break
                            l.unlock()
                        now = time.clock()
                        if now >= (lastTime+params['cycleTime']):
                            break
                        
                        time.sleep(1e-3) ## Wake up every 1ms
                        c += 1
                    if stop:
                        break
        except:
            printExc("Error in patch acquisition thread, exiting.")
        #self.emit(QtCore.SIGNAL('threadStopped'))
            
    def analyze(self, data, params):
        #print "\n\nAnalysis parameters:", params
        ## Extract specific time segments
        base = data['Time': 0.0:(params['delayTime']-1e-3)]
        pulse = data['Time': params['delayTime']:params['delayTime']+params['pulseTime']-1e-3]
        pulseEnd = data['Time': params['delayTime']+(params['pulseTime']*2./3.):params['delayTime']+params['pulseTime']-1e-3]
        end = data['Time':params['delayTime']+params['pulseTime']+1e-3:]
        #print "time ranges:", pulse.xvals('Time').min(),pulse.xvals('Time').max(),end.xvals('Time').min(),end.xvals('Time').max()
        ## Exponential fit
        #  v[0] is offset to start of exp
        #  v[1] is amplitude of exp
        #  v[2] is tau
        def expFn(v, t):
            return (v[0]-v[1]) + v[1] * exp(-t / v[2])
        # predictions
        ar = 10e6
        ir = 200e6
        if params['mode'] == 'vc':
            ari = params['vcPulse'] / ar
            iri = params['vcPulse'] / ir
            pred1 = [ari, ari-iri, 1e-3]
            pred2 = [iri-ari, iri-ari, 1e-3]
        else:
            clamp = self.manager.getDevice(self.clampName)
            bridge = float(clamp.getParam('BridgeBalResist'))
            bridgeOn = clamp.getParam('BridgeBalEnable')
            if not bridgeOn:
                bridge = 0.0
            #print "bridge:", bridge
            arv = params['icPulse'] * ar - bridge
            irv = params['icPulse'] * ir
            pred1 = [arv, -irv, 10e-3]
            pred2 = [irv, irv, 50e-3]
            
        # Fit exponential to pulse and post-pulse traces
        fit1 = scipy.optimize.leastsq(
            lambda v, t, y: y - expFn(v, t), pred1, 
            args=(pulse.xvals('Time')-pulse.xvals('Time').min(), pulse['primary'] - base['primary'].mean()),
            maxfev=200, full_output=1, warning=False)
        fit2 = scipy.optimize.leastsq(
            lambda v, t, y: y - expFn(v, t), pred2, 
            args=(end.xvals('Time')-end.xvals('Time').min(), end['primary'] - base['primary'].mean()),
            maxfev=200, full_output=1, warning=False)
            
        
        err = max(abs(fit1[2]['fvec']).sum(), abs(fit2[2]['fvec']).sum())
        #err = max(fit1[2]['nfev'], fit2[2]['nfev'])
        
        #times = pulse.xvals('Time')-pulse.xvals('Time').min()
        #err = fromfunction(lambda t: pulse['primary'][t] - expFn(fit1[0], times[t]), pulse['primary'].shape)
        #err *= err
        #err = err.sum()
        
        
        # Average fit1 with fit2 (needs massaging since fits have different starting points)
        #print fit1
        fit1 = fit1[0]
        fit2 = fit2[0]
        fitAvg = [
            0.5 * (fit1[0] - (fit2[0] - (fit1[0] - fit1[1]))),
            0.5 * (fit1[1] - fit2[1]),
            0.5 * (fit1[2] + fit2[2])            
        ]
        fitAvg = fit1

        (fitOffset, fitAmp, fitTau) = fit1

        #0.5 * (fit1[0] + (fit2[0] * array([-1, -1, 1])))
        #print pred1, fit1, pred2, fit2, fitAvg
        
        ## Handle anelysis differently depenting on clamp mode
        if params['mode'] == 'vc':
            #global iBase, iPulse, iPulseEnd
            iBase = base['Channel': 'primary']
            iPulse = pulse['Channel': 'primary'] 
            iPulseEnd = pulseEnd['Channel': 'primary'] 
            vBase = base['Channel': 'Command']
            vPulse = pulse['Channel': 'Command'] 
            vStep = vPulse.mean() - vBase.mean()
            sign = [-1, 1][vStep > 0]

            iStep = sign * max(1e-15, sign * (iPulseEnd.mean() - iBase.mean()))
            iRes = vStep / iStep
            
            ## From Santos-Sacchi 1993
            pTimes = pulse.xvals('Time')
            iCapEnd = pTimes[-1]
            iCap = iPulse['Time':pTimes[0]:iCapEnd] - iPulseEnd.mean()
            Q = sum(iCap) * (iCapEnd - pTimes[0]) / iCap.shape[0]
            Rin = iRes
            Vc = vStep
            Rs_denom = (Q * Rin + fitTau * Vc)
            if Rs_denom != 0.0:
                Rs = (Rin * fitTau * Vc) / Rs_denom
                Rm = Rin - Rs
                Cm = (Rin**2 * Q) / (Rm**2 * Vc)
            else:
                Rs = 0
                Rm = 0
                Cm = 0
            aRes = Rs
            cap = Cm
            
        if params['mode'] == 'ic':
            iBase = base['Channel': 'Command']
            iPulse = pulse['Channel': 'Command'] 
            vBase = base['Channel': 'primary']
            vPulse = pulse['Channel': 'primary'] 
            vPulseEnd = pulseEnd['Channel': 'primary'] 
            iStep = iPulse.mean() - iBase.mean()
            sign = [-1, 1][iStep >= 0]
            
            vStep = sign * max(1e-5, sign * (vPulseEnd.mean() - vBase.mean()))
            if iStep == 0:
                iStep = 1e-14
            iRes = (vStep / iStep) + bridge
            #print iRes, vStep, iStep, bridge
            #print "current step:", iStep
            #print "bridge:", bridge
            aRes = (fitAvg[0] / iStep) + bridge
            #iRes = (-fitAvg[1] / iStep) + bridge
            cap = fitAvg[2] / (iRes-aRes)
            
            
        rmp = vBase.mean()
        rmps = vBase.std()
        rmc = iBase.mean()
        rmcs = iBase.std()
        #print rmp, rmc
        
            
        return {
            'inputResistance': iRes, 
            'accessResistance': aRes,
            'capacitance': cap,
            'restingPotential': rmp, 'restingPotentialStd': rmps,
            'restingCurrent': rmc, 'restingCurrentStd': rmcs,
            'fitError': err
        }
            
    def stop(self, block=False):
        with self.lock:
            self.stopThread = True
        if block:
            if not self.wait(10000):
                raise Exception("Timed out while waiting for patch thread exit!")
                