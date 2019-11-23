import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="用户登录",pos=(400,300),size=(300,300))
        # 创建一个面板
        pannel =wx.Panel(self)
        # 创建按钮
        self.bt_confim =wx.Button(pannel,label ='确定')
        self.bt_cannel =wx.Button(pannel,label ='取消')

        #创建文本    # 标题

        self.title = wx.StaticText(pannel, label='请输入用户名和密码')

        self.label_user = wx.StaticText(pannel,label ='用户名:')
        self.text_user =wx.TextCtrl(pannel,style=wx.TE_LEFT)

        self.label_pwd = wx.StaticText(pannel,label='密    码:')
        self.text_pwd =wx.TextCtrl(pannel,style=wx.TE_PASSWORD)

        # 创建横向容器
        Hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        Hsizer_user.Add(self.label_user,proportion=0, flag=wx.ALL,border =5)
        Hsizer_user.Add(self.text_user,proportion=1, flag=wx.ALL,border =5)

        hsizer_pwd =wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd,proportion=0,flag=wx.ALL,border =5)
        hsizer_pwd.Add(self.text_pwd ,proportion=1,flag=wx.ALL,border=5)

        hsizer_button =wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confim,proportion =0,flag =wx.ALL,border= 5)
        hsizer_button.Add(self.bt_cannel,proportion=0,flag=wx.ALL,border=5)

        viszer_all=wx.BoxSizer(wx.VERTICAL)
        viszer_all.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=15)
        viszer_all.Add(Hsizer_user,proportion =0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)

        viszer_all.Add(hsizer_pwd,proportion =0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
        viszer_all.Add(hsizer_button,proportion =0,flag=wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT,border=15)
        pannel.SetSizer(viszer_all)


if __name__ == '__main__':
    app = wx.App()                      # 初始化应用
    frame = MyFrame(parent=None,id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()                        # 显示窗口
    app.MainLoop()                      # 调用主循环方法


