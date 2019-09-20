import wx
from simpleguipanel import *

class SimpleGuiFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(SimpleGuiFrame, self).__init__(*args, **kw)
        self.panel = SimpleGuiPanel(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)