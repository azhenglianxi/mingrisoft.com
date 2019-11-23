# gui  输入-> 处理->输出

# 常用的GUI框架
"""
**wxpython :python 语言的一套优秀GUI 图形库
kivy ：开源的工具包 能够让相同的源代码创建的程序能跨平台运行
Fkexx: 一个纯python 工具吧 用来创建图形化界面应用程序
**Pyqt ：c++ Qt库的Python版本 支持跨平台   爬虫用的多

TKinter ：也叫TK接口 是TK图形用户界面工具包的标准python 接口 TK是一个轻量级的跨平台图形用户界面工具

"""
import wx

class App(wx.App):
    # 定义一个子类
    def OnInit(self):
        frame =wx.Frame(parent=None,title ="hello python")
        frame.Show()
        return True

if __name__ == '__main__':
     # 实例化该子类
     app =App()

     # 调用主程序的方法
     app.MainLoop()

"""
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id, title="创建Frame",pos=(100, 100), size=(300, 300))

if __name__ == '__main__':
    app = wx.App()  	                    # 初始化应用
    frame = MyFrame(parent=None,id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()                        # 显示窗口
    app.MainLoop()   """



