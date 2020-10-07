import wx
from ui.filedrop import *

WINDOW_SIZE = 480

class SimpleGuiPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(SimpleGuiPanel, self).__init__(*args, **kw)
        filedrop = FileDrop(self)
        self.SetDropTarget(filedrop)
        self._initUi()
        self.SetAutoLayout(True)


    def _initUi(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.text = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER|wx.TE_MULTILINE, size=(WINDOW_SIZE,WINDOW_SIZE))
        self.text.SetValue("")
        sizer.Add(self.text, 1, wx.EXPAND)
        
        btnBox = wx.BoxSizer(wx.HORIZONTAL)

        clearBtnId = wx.NewId()
        clearBtn = wx.Button(self, clearBtnId, "Clear", size=(50,30))
        clearBtn.Bind(wx.EVT_BUTTON, self.OnClearBtn)
        btnBox.Add(clearBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        copyBtnId = wx.NewId()
        copyBtn = wx.Button(self, copyBtnId, "Copy", size=(50,30))
        copyBtn.Bind(wx.EVT_BUTTON, self.OnCopyBtn)
        btnBox.Add(copyBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        runBtnId = wx.NewId()
        runBtn = wx.Button(self, runBtnId, "Run", size=(50,30))
        runBtn.Bind(wx.EVT_BUTTON, self.OnRunBtn)
        btnBox.Add(runBtn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(btnBox, 0, wx.ALIGN_CENTRE, 5)
        self.SetSizer(sizer)

    def OnCallback(self, filelist):
        self._printFileList(filelist)

    def _printFileList(self, files):
        fileList = ""
        for file in files:
            fileList += file + "\n"
        self.text.SetValue(fileList)

    def OnClearBtn(self, event):
        self.text.SetValue("")
        
    def OnCopyBtn(self, event):
        toCopyData = self.text.GetValue()
        
        if len(toCopyData) == 0:
            return 
            
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(toCopyData))
            wx.TheClipboard.Close()

    def OnRunBtn(self, event):
        pass
