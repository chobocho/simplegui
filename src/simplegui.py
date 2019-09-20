import wx
from simpleguiframe import *

SW_TITLE = "SIMPLE GUI"

def main(): 
    app = wx.App()
    frm = SimpleGuiFrame(None, title=SW_TITLE, size=(600,600))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()