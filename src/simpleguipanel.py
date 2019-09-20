import wx
from filedrop import *

class SimpleGuiPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(SimpleGuiPanel, self).__init__(*args, **kw)
        filedrop = FileDrop(self)
        self.SetDropTarget(filedrop)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER,size=(600,600))
        self.text.SetValue("")
        sizer.Add(self.text, 1, wx.EXPAND)
        
    def OnCallback(self, filelist):
        self._printFileList(filelist)

    def _printFileList(self, files):
        fileList = ""
        for file in files:
            fileList += file + "\n"
        self.text.SetValue(fileList)