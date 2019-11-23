import wx
# app = wx.App()
# frame =wx.Frame(None,title="hello python")
# frame.Show()
# app.MainLoop()

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="sdada",pos=(100,100),size=(300,300))

    pass
if __name__ == '__main__':
    app =wx.App()
    frame=MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

