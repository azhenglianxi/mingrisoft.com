#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@Time     :2019-10-24 23:10:53
#@Author   :azhenglianxi
#@Site     :
#@File     :threading_test02.py
#@Software :PyCharm

from threading import Thread
import  time
class SubThread(Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg ='子进程'+self.name+'执行，i='+str(i)
            print(msg)

if __name__ == '__main__':
    print('---进行开始--')
    t1 =SubThread()
    t2 =SubThread()
    t3 = SubThread()
    t1.start()
    t3.start()
    t2.start()
    t1.join()
    t2.join()
    t3.join()
    print('----主进程结束--')