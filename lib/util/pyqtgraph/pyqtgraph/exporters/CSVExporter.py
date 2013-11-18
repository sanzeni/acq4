import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from .Exporter import Exporter
from pyqtgraph.parametertree import Parameter


__all__ = ['CSVExporter']
    
    
class CSVExporter(Exporter):
    Name = "CSV from plot data"
    windows = []
    def __init__(self, item):
        Exporter.__init__(self, item)
        self.params = Parameter(name='params', type='group', children=[
            {'name': 'separator', 'type': 'list', 'value': 'comma', 'values': ['comma', 'tab']},
            {'name': 'precision', 'type': 'int', 'value': 10, 'limits': [0, None]},
        ])
        
    def parameters(self):
        return self.params
    
    def export(self, fileName=None):
        
        if not isinstance(self.item, pg.PlotItem):
            raise Exception("Must have a PlotItem selected for CSV export.")
        
        if fileName is None:
            self.fileSaveDialog(filter=["*.csv", "*.tsv"])
            return

        fd = open(fileName, 'w')
        data = []
        header = []
        for n, c in enumerate(self.item.curves):
            data.append(c.getData())
            header.extend(['x%04d' % n, 'y%0d' % n])  # headers should be unique for every column for import

        if self.params['separator'] == 'comma':
            sep = ','
        else:
            sep = '\t'
            
        fd.write(sep.join(header) + '\n')
        i = 0
        numFormat = '%%0.%dg' % self.params['precision']
        numRows = reduce(max, [len(d[0]) for d in data])
        for i in range(numRows):
            for d in data:
                if d is not None and i < len(d[0]): # sometimes d can be none - incomplete protocols, extra data in plot, etc.
                    fd.write('%g%s%g%s'%(d[0][i], sep, d[1][i], sep))
                    done = False
                else:
                    fd.write(' %s %s' % (sep, sep))
            fd.write('\n')
        fd.close()

        
                
        