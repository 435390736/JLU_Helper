# # # # class Phone:
# # # #     functions = "打电话"
# # # #     def __init__(self, brand, color, version):
# # # #         self.brand = brand
# # # #         self.color = color
# # # #         self.version = version
# # # #
# # # #
# # # #     @property
# # # #     def call(self):
# # # #         return "正在用%s牌子的%s手机打电话"%(self.brand, self.version)
# # # #
# # # #
# # # #     @classmethod
# # # #     def func(cls):
# # # #         #print(cls)
# # # #         print("----->", cls.functions)
# # # #
# # # #
# # # #     @staticmethod
# # # #     def see_movie(a, b):
# # # #         print("%s 正在用 %s 手机看电影"%(a, b))
# # # #
# # # #
# # # # p1 = Phone("apple", "白色", "iphone_8")
# # # # v = p1.call
# # # # print(v)
# # # #
# # # # Phone.func()
# # # #
# # # # Phone.see_movie("小明", "小米")
# # # # p1.see_movie("alex", "iphone8")
# # #
# # # class Date:
# # #     def __init__(self,year,mon,day):
# # #         self.year=year
# # #         self.mon=mon
# # #         self.day=day
# # #     def tell_birth(self):
# # #         print('出生于<%s>年 <%s>月 <%s>日'%(self.year,self.mon,self.day))
# # #
# # #
# # # class Teacher:
# # #     def __init__(self,name,age,sex,year,month,day):
# # #         self.name=name
# # #         self.age=age
# # #         self.sex=sex
# # #         self.birth=Date(year,month,day)
# # #     def teaching(self):
# # #         print('%s is teaching'%self.name)
# # # class Student:
# # #     def __init__(self,name,age,sex,year,mon,day):
# # #         self.name=name
# # #         self.age=age
# # #         self.sex=sex
# # #         self.birth=Date(year,mon,day)
# # #     def studying(self):
# # #         print('%s is studying'%self.name)
# # #
# # # xiaobai=Student('xiaobai',22,'male','1995','3','16')
# # # xiaobai.birth.tell_birth()
# # # xiaobai.studying()
# #
# # #------------------------------------------------------------
# #
# # class School:
# #     def __init__(self,name,addr):
# #         self.name = name
# #         self.addr = addr
# #
# #     def zhao_sheng(self):
# #         print("%s正在招生"%self.name)
# #
# #
# # class Course:
# #     def __init__(self,name,price,period,school):
# #         self.name = name
# #         self.price = price
# #         self.period = period
# #         self.school = school
# #
# #
# # s1 = School("Oldboy","北京")
# # s2 = School("Oldboy","南京")
# # s3 = School("Oldboy","东京")
# #
# # msg = """
# # 1 老男孩 北京校区
# # 2 老男孩 南京校区
# # 3 老男孩 东京校区
# # """
# # while True:
# #     print(msg)
# #     menu = {
# #         "1":s1,
# #         "2":s2,
# #         "3":s3
# #     }
# #     choice = input("学校名>>>")
# #     school_obj = menu[choice]
# #
# #     name = input("课程>>>")
# #     price = input("学费>>>")
# #     period = input("学时>>>")
# #
# #     new_course = Course(name,price,period,school_obj)
# #
# #     print("课程 <%s> 属于 <%s> 学校"%(new_course.name, menu[choice].name))
#
# #《----------------------------------------------------------------------》
#
# #
# #
# # import pickle
# # import time
# # import hashlib
# #
# # num = 0
# #
# # def creat_md5():
# #     global num
# #     m = hashlib.md5()
# #     m.update(str(num).encode("utf-8"))
# #     num = int(num)
# #     num += 1
# #     return m.hexdigest()
# #
# # class Base:
# #     def save(self,id):
# #         with open(id, "wb") as f:
# #             pickle.dump(self, f)
# #
# #
# # class School(Base):
# #     def __init__(self,school_name,addr):
# #         self.school_name = school_name
# #         self.addr = addr
# #
# # class Course(School, Base):
# #     def __init__(self,school_name,addr,name,price,period):
# #         super().__init__(school_name,addr)
# #         self.name = name
# #         self.price = price
# #         self.period = period
# #
# # def creat():
# #     global num
# #     id = creat_md5()
# #     school_name = input("学校名>>")
# #     addr = input("学校地址>>")
# #     course_name = input("课程名>>")
# #     course_price = input("价格>>")
# #     course_period = input("学时>>")
# #     c1 = Course(school_name,addr,course_name,
# #                 course_price, course_period)
# #     c1.save(id)
# #
# # def load():
# #     number = input("请输入要查的学校编号:")
# #     m = hashlib.md5()
# #     m.update(str(number).encode("utf-8"))
# #     ind = m.hexdigest()
# #     obj = pickle.load(open(str(ind),"rb"))
# #     print(obj.name, obj.addr, obj.price)
# #
# #
# #
# # msg = """
# # 0 退出
# # 1 输入学校及课程
# # 2 查看课程
# # """
# # while True:
# #     print(msg)
# #     choice = input("请输入选项:")
# #     if choice == "1":
# #         obj = creat()
# #     elif choice == "2":
# #         load()
# #     elif choice == "0":
# #         break
#
#
# #-----------------------------------------------------
#
# # class Fib:
# #     def __init__(self):
# #         self.a = 1
# #         self.b = 1
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         self.a,self.b = self.b,self.a+self.b
# #         return self.a
# #
# # f = Fib()
# # print(f.__next__())
# # print(f.__next__())
# # for i in range(20):
# #     print(f.__next__())
#
# #------------------------------------------------------
# #
# # format_dic = {
# #     "ymd":"{0.year} {0.mon} {0.day}",
# #     "y:m:d":"{0.year}:{0.mon}:{0.day}",
# #     "m-d-y":"{0.mon}-{0.day}-{0.year}"
# # }
# #
# # class Date:
# #     def __init__(self,year,mon,day):
# #         self.year = year
# #         self.mon = mon
# #         self.day = day
# #     def __format__(self, format_spec):
# #         print("<----->",format_spec)
# #         if not format_spec or format_spec not in format_dic:
# #             format_spec = "ymd"
# #         fm = format_dic[format_spec]
# #         return fm.format(self)
# #
# # d = Date(2019,5,20)
# # print(format(d,"y:m:d"))
# # print(format(d,"aaaaaa"))
# # print(format(d))
#
#
# #-----------------------------------------------------
# #
# # class MyDescriptor:
# #     def __init__(self):
# #         self.data = None
# #     def __get__(self, instance, owner):
# #         print("from get")
# #         return self.data
# #     def __set__(self, instance, value):
# #         print("from set")
# #         self.data = value
# #     def __delete__(self, instance):
# #         print("from delete")
# #         del self.data
# # class Foo:
# #     attr = MyDescriptor()
# #
# # f=Foo()
# # print(f.attr)
# # f.attr = "abc"
# # print(f.attr)
# # del f.attr
# # # print(f.attr)   #删去后打印会报错 has no attribute
#
#
# #-------------------------------------------------
# # class Foo:
# #     def __init__(self, name):
# #         self.name = name
# #     def __enter__(self):
# #         print("执行enter")
# #         return self
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         print("执行exit")
# #         print(exc_type) #异常类    类似NameError
# #         print(exc_val)  #异常值    类似name "aaa" is not defined
# #         print(exc_tb)   #追踪信息   没啥用
# #         return True
# #
# #
# # with Foo("a.txt") as f:
# #     print(f)
# #     print(f.name)
# #     print(f.aaa)
# #     print("<--->")
# # print("abcdef")
#
# #---------------------------------------------------------
# #
# # import threading,time
# # def foo(num):
# #     print("time is %s"%time.ctime())
# #     time.sleep(num)
# #     print("stop")
# #
# # if __name__ == "__main__":
# #     t1 = threading.Thread(target=foo, args=(3,))
# #     t2 = threading.Thread(target=foo, args=(5,))
# #     # t2.setDaemon(True)
# #     t1.start()
# #     t1.join(1)
# #     t2.start()
# #
# #     print("ending")
#
#
# #-------------------------------------=--------------------------------------
# # 多进程
# # from multiprocessing import Process
# # import os
# # def run_proc(name):
# #     print('Run child process %s (%s)...' % (name, os.getpid()))
# # if __name__=='__main__':
# #
# #     print('Parent process %s.' % os.getpid())
# #     p = Process(target=run_proc, args=('test',))
# #     print('Child process will start.')
# #     p.start()
# #     p.join()
# #     print('Child process end.')
#
# #----------------------------------------------------------------------------
# #进程池
# # from multiprocessing import Pool
# # import os,time,random
# #
# # def long_time_task(name):
# #     print('Run task %s (%s)...' % (name, os.getpid()))
# #     start = time.time()
# #     time.sleep(random.random() * 3)
# #     end = time.time()
# #     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
# # if __name__=="__main__":
# #     print("parent process %s"%os.getpid())
# #     p = Pool(4) #可以同时跑的进程数
# #     for i in range(5):
# #         p.apply_async(long_time_task, args=(i,))
# #     print("waiting for all subprocess done ")
# #     p.close()
# #     p.join()
# #     print("ending")
#
# #--------------------------------------------------------------------
# # 同步锁
# # import time,threading
# # num = 100
# # def foo():
# #     global num
# #     lock.acquire()
# #     temp = num
# #     time.sleep(0.001)
# #     num = temp - 1
# #     lock.release()
# # l = []
# # lock = threading.Lock()
# # for i in range(100):
# #     t = threading.Thread(target=foo)
# #     t.start()
# #     l.append(t)
# # for t in l:
# #     t.join()
# # print(num)
#
# #-------------------------------------------------------
# #死锁
# # import threading,time
# # class sisuo(threading.Thread):
# #     def A(self):
# #         a_lock.acquire()
# #         print("{} a_lock {}\n".format(self.name, time.ctime()),end="")
# #         time.sleep(3)
# #         b_lock.acquire()
# #         print("{} b_lock {}\n".format(self.name, time.ctime()),end="")
# #         time.sleep(0.5)
# #         b_lock.release()
# #         a_lock.release()
# #     def B(self):
# #         b_lock.acquire()
# #         print("{} b_lock {}\n".format(self.name,time.ctime()), end="")
# #         time.sleep(3)
# #         a_lock.acquire()
# #         print("{} a_lock {}\n".format(self.name, time.ctime()), end="")
# #         time.sleep(0.5)
# #         a_lock.release()
# #         b_lock.release()
# #     def run(self):
# #         self.A()
# #         self.B()
# # if __name__ == "__main__":
# #     a_lock = threading.Lock()
# #     b_lock = threading.Lock()
# #     l = []
# #     for i in range(5):
# #         t = sisuo()
# #         t.start()
# #         l.append(t)
# #     for t in l:
# #         t.join()
# #     print("ending……")
#
# #--------------------------------------------------------------
# #递归锁
# # import threading,time
# # class sisuo(threading.Thread):
# #     def A(self):
# #         r_lock.acquire()
# #         print(self.name, "a_lock", time.ctime())
# #         time.sleep(3)
# #         r_lock.acquire()
# #         print(self.name, "b_lock",time.ctime())
# #         time.sleep(0.5)
# #         r_lock.release()
# #         r_lock.release()
# #     def B(self):
# #         r_lock.acquire()
# #         print(self.name, "b_lock", time.ctime())
# #         time.sleep(3)
# #         r_lock.acquire()
# #         print(self.name, "a_lock", time.ctime())
# #         time.sleep(0.5)
# #         r_lock.release()
# #         r_lock.release()
# #     def run(self):
# #         self.A()
# #         self.B()
# # if __name__ == "__main__":
# #     r_lock = threading.RLock()
# #     a_lock = threading.Lock()
# #     b_lock = threading.Lock()
# #     l = []
# #     for i in range(5):
# #         t = sisuo()
# #         t.start()
# #         l.append(t)
# #     for t in l:
# #         t.join()
# #     print("ending……")
#
# #-----------------------------------------------------------
# #同步对象event
# # import threading, time
# # class Boss(threading.Thread):
# #     def run(self):
# #         print("Boss:今晚加班")
# #         event.set()
# #         time.sleep(3)
# #         print("Boss:加班结束")
# #         event.set()
# #
# # class Worker(threading.Thread):
# #     def run(self):
# #         event.wait()
# #         print("{}:emmm\n".format("Worker"),end="")
# #         event.clear()
# #         event.wait()
# #         print("{}Worker:666^_^\n".format(""), end="")
# #
# # if __name__ == "__main__":
# #     event = threading.Event()
# #     l = []
# #     for i in range(3):
# #         l.append(Worker())
# #     l.append(Boss())
# #     for j in l:
# #         j.start()
# #     for j in l:
# #         j.join()
# #     print("ending ")
#
# #--------------------------------------------------------
# #信号量
# # import threading,time
# # s = threading.Semaphore(3)
# # class mythread(threading.Thread):
# #     def foo(self):
# #         s.acquire()
# #         time.sleep(2)
# #         print("{}   :{}\n".format(self.name, time.ctime()), end="")
# #         s.release()
# #     def run(self):
# #         self.foo()
# #
# # if __name__ == "__main__":
# #     for i in range(10):
# #         t = mythread()
# #         t.start()
#
# #-------------------------------------------------------------------------
# # Manager实现多进程共享内存
# # from multiprocessing import Process,Manager
# # import os
# # # 这里实现的就是多个进程之间共享内存，并修改数据
# # # 这里不需要加锁，因为manager已经默认给你加锁了
# #
# # def f(d,l):
# #     d[1] = '1'
# #     d['2'] = 2
# #     # d[0.25] = None
# #     l.append(os.getpid())
# #     print(l)
# #
# # if __name__ == '__main__':
# #     # with Manager() as manager:
# #         d =  Manager().dict() #生成一个字典
# #         l = Manager().list(range(5))  #生成一个列表
# #         p_list = []
# #         for i in range(10):
# #             p = Process(target=f,args=(d,l))
# #             p.start()
# #             p_list.append(p)
# #         for res in p_list:
# #             res.join()
# #         print(d)
# #         print(l)
#
# #------------------------------------------------------
# #geenlet协程
# # import greenlet
# # # greenlet 其实就是手动切换；gevent是对greenlet的封装，可以实现自动切换
# #
# # def test1():
# #     print("123")
# #     gr2.switch()   # 切换去执行test2
# #     print("456")
# #     gr2.switch()   # 切换回test2之前执行到的位置，接着执行
# #
# # def test2():
# #     print("789")
# #     gr1.switch()   # 切换回test1之前执行到的位置，接着执行
# #     print("666")
# # gr1 = greenlet.greenlet(test1)   # 启动一个协程 注意test1不要加()
# # gr2 = greenlet.greenlet(test2)   #
# # gr1.switch()
#
# #--------------------------------------------------------------
# # gevent协程
# # import gevent
# #
# # def A():
# #     while 1:
# #         print('-------A-------')
# #         gevent.sleep(1) #用来模拟一个耗时操作，注意不是time模块中的sleep
# #
# # def B():
# #     while 1:
# #         print('-------B-------')
# #         gevent.sleep(0.6)  #每当碰到耗时操作，会自动跳转至其他协程
# #
# # g1 = gevent.spawn(A) # 创建一个协程
# # g2 = gevent.spawn(B)
# # g1.join()  #等待协程执行结束
# # g2.join()
#
# #------------------------------------------------------------------
# # import asyncio
# #
# # async def coroutine_example():
# #     await asyncio.sleep(1)
# #     print('zhihu ID: Zarten')
# #
# # core = coroutine_example()
# #
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(core)
# # loop.close()
#
# #--------------------------------------------------------
# # #selector模块
# # import selectors
# # import socket
# #
# # sel = selectors.DefaultSelector()   #创建对象，根据操作系统自动选择IO多路复用的方式
# #
# # def accept(sock, mask): #监听是否有客户端来链接
# #     conn, addr = sock.accept()
# #     print('客户端链接 : ', conn, 'from', addr)
# #     conn.setblocking(False) #设置非阻塞
# #     sel.register(conn, selectors.EVENT_READ, read)#注册conn链接，把conn和read方法绑定
# #
# # def read(conn, mask):
# #     try:
# #         data = conn.recv(1024)
# #         if data:    #接收客户端发消息
# #             print('客户端发来消息 : ', data.decode("utf-8"))
# #             conn.send(data.upper())
# #     except Exception:   #客户端断开链接，解注册conn
# #             print('断开客户端链接 : ', conn)
# #             sel.unregister(conn)    #解注册conn
# #             conn.close()
# #
# # sock = socket.socket()
# # sock.bind(('127.0.0.1', 8080))
# # sock.listen(100)
# # sock.setblocking(False)
# #
# # sel.register(sock, selectors.EVENT_READ, accept)#注册sock，把sock与accept方法绑定
# #
# # while True:
# #     events = sel.select()   #对sel对象监听
# #     for key, mask in events:    #mask是一个整数，意义不大
# #         callback = key.data #callback是accept方法
# #         callback(key.fileobj, mask) #key.fileobj就是监听的对象
#
# #--------------------------------------------------------------------------
#
# # import re
# # s = '15020220000117xxxx'
# # res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})',s)
# # print(res.groupdict())
#
# #----------------------------------------------------------------------
#
# import random
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
#
# myfont = font_manager.FontProperties(fname = "C:\Windows\Fonts\FZSTK.TTF")
#
# years = range(21,31)
# nums1 = [random.randint(0,5) for i in range(10)]
# nums2 = [random.randint(0,5) for j in range(10)]
#
# plt.figure(figsize=(10,8),dpi=80)
#
# plt.xlabel("年龄",fontproperties=myfont,size=20)
# plt.ylabel("数量",fontproperties=myfont,size=20)
#
# _years = ["{}岁".format(i) for i in years]
# plt.xticks(years,_years,rotation=45,fontproperties=myfont,size=15)
#
# plt.plot(years, nums1, label="折线一")
# plt.plot(years, nums2, label="折线二")
#
# plt.legend(loc=2,prop=myfont)
#
# plt.grid(alpha = 0.3)
# plt.show()


# import pandas as pd
# from matplotlib import pyplot as  plt
# from matplotlib import font_manager
#
# starbucks_data = pd.read_csv("starbucks_store_worldwide.csv")
# cn_starbucks = starbucks_data[starbucks_data["Country"]=="CN"]
# group = cn_starbucks.groupby(by=[cn_starbucks["State/Province"]])
# num_list = []
# city_list = []
# f = open("China_Starbucks.txt","w+",encoding="utf-8")
# for i in group:
#     for j in i[1]["Store Name"].index:
#         temp_index = j
#         # print((i[1])["Store Name"][j]+"\t"+(i[1])["Street Address"][j]+"\t"+str((i[1])["Phone Number"][j]))
#         txt = ((i[1])["Store Name"][j]+"\t"+(i[1])["Street Address"][j]+"\t"+str((i[1])["Phone Number"][j])+"\n")
#         f.write(txt)
#         city_list.append(((i[1])["Store Name"][j])[0:2])
#     f.write("\n\n")
#     print(((i[1])["Store Name"][temp_index])[0:2])
#     city_list.append(((i[1])["Store Name"][i[1]["Store Name"].index])[0:2])
#     num_list.append(len(i[1]["Store Name"].index))
# f.close()
#
# myfont = font_manager.FontProperties(fname="C:\Windows\Fonts\FZSTK.TTF")
# _x = [i for i in range(len(num_list))]
#
# plt.plot(city_list, num_list)
# plt.show()

#------------------------------------------------------------------

# from urllib import request
# from urllib import parse
# url = "http://www.budejie.com"
# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
#     "Cookie":"BAIDU_SSP_lcr=https://www.baidu.com/link?url=FKwkOrBxg3Gso2FyhGS3vV2h47omlisaNkogHVCkZCsQG8bZBalG8RutDSVrSN1M&wd=&eqid=c51a8dc7003d0699000000035d92f7b6; _ga=GA1.2.1786076054.1569912762; _gid=GA1.2.335605203.1569912762; Hm_lvt_7c9f93d0379a9a7eb9fb60319911385f=1569912762; Hm_lpvt_7c9f93d0379a9a7eb9fb60319911385f=1569912762"
# }
# res = request.Request(url=url, headers=header, method="GET")
# resp = request.urlopen(res)
# print(resp.read().decode("utf-8"))


#------------------------------------------------------------------

#代理
# from urllib import request
#
# url = "http://www.baidu.com"
# # resp = request.urlopen(url)
# # print(resp.read().decode("utf8"))
#
# hander = request.ProxyHandler({"http":"124.205.155.154:9090"})
# opener = request.build_opener(hander)
# # request.install_opener(opener)
# resp = opener.open(url)
# print(resp.read().decode("utf8"))


#----------------------------------------------------------------------

#cookie登陆QQ空间
# from urllib import request
# url = "https://user.qzone.qq.com/435390736"
# header = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
#     # "cookie":"pgv_pvi=2373600256; pgv_si=s8252944384; _qpsvr_localtk=0.8795283998122239; uin=o0435390736; skey=@JcdveWJK7; ptisp=cnc; RK=1Sbkg1R5EI; ptcz=d93c47ac758ac6e95ce117f5d870b3a25c9f8fef704f068414fba9763a0afc3c; p_uin=o0435390736; pt4_token=ZHLu53FCn7PsD8jcalTMpfB7fyXQGIbkQGx20l0kl3Q_; p_skey=sAUnrwu3yM*v0v6gr23TziA21p1urocyButx8RPgfVs_; Loading=Yes; qz_screen=1536x864; 435390736_todaycount=0; 435390736_totalcount=12923; pgv_pvid=1731301400; pgv_info=ssid=s9134167128; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0",
#     "cookie":"_qpsvr_localtk=0.37434196868397884; pgv_pvi=2496802816; pgv_si=s7102041088; uin=o0435390736; skey=@KTN651Bqj; ptisp=cnc; RK=1Sbkg1R5EI; ptcz=275c5c2cdf88222dacaec2a26cf1f7d26419a7c7cd55e3e02d149abd4fc3434e; p_uin=o0435390736; pt4_token=-jGpRNiS64WeB4nEk6Igx7oEZEauD1fSy*0ZsY0rYHE_; p_skey=vlynOESJShEn2-RTZhBZRCuE-7Dw**svgovNX5jUIqc_; Loading=Yes; qz_screen=1536x864; 435390736_todaycount=0; 435390736_totalcount=12923; pgv_pvid=5418922392; pgv_info=ssid=s199813259",
#     "referer":"https://qzone.qq.com/"
# }
# req = request.Request(url=url, headers=header, method="GET")
# resp = request.urlopen(req)
# print(resp.read().decode("utf8"))


#
# from urllib import request
# from  urllib import parse
# from http.cookiejar import CookieJar
#
# # 1.登陆
# cookiejar = CookieJar()
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
# header = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
#     "referer":"http://www.renren.com/SysHome.do"
# }
# data = {
#     "email":"18947721668",
#     "password":"ka1701607108"
# }
# login_url = "http://www.renren.com/PLogin.do"
# req = request.Request(login_url, data=parse.urlencode(data).encode("utf-8"),
#                       headers=header)
# resp = opener.open(login_url)
# # with open("renren.html","w") as f:
# #     f.write(resp.read().decode("utf8"))
# print(resp.read().decode("utf8"))



# import requests
#
# url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
# data = {
#     "first":"true",
#     "pn":"1",
#     "kd":"python"
# }
# header = {
#     "Referer":"https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
#     "Cookie":"JSESSIONID=ABAAABAAADEAAFIF58A6AD0116B74BAD726A15AEC849B06; user_trace_token=20191004134538-c0f3bf2e-6bdc-4f3e-97c1-1a1d9269e400; _ga=GA1.2.2097317028.1570167936; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570167936; LGSID=20191004134539-31f8af5e-e66a-11e9-97da-525400f775ce; PRE_UTM=; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fgongsi%2F147.html; LGUID=20191004134539-31f8b104-e66a-11e9-97da-525400f775ce; _gid=GA1.2.748725692.1570167936; WEBTJ-ID=20191004134539-16d954d625e432-0b0774b605a93f-67e1b3f-1327104-16d954d625fac0; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d954d94d410a-0a043eef4b2c2c-67e1b3f-1327104-16d954d94d59c2%22%2C%22%24device_id%22%3A%2216d954d94d410a-0a043eef4b2c2c-67e1b3f-1327104-16d954d94d59c2%22%7D; sajssdk_2015_cross_new_user=1; X_HTTP_TOKEN=c2e88596d7c6bcab8897610751b0fcd86b5c8c0b2e; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570167985; LGRID=20191004134628-4f32885e-e66a-11e9-97da-525400f775ce; SEARCH_ID=abe309346a354349af1b0b38dcdaf4b6"
# }
#
# response = requests.post(url,data=data,headers=header)
#


# import requests
# proxy = {
#     "http":"125.123.124.186:9999"
# }
# response = requests.get("http://httpbin.org/ip",proxies=proxy)
# print(response.text)


# import requests
# from lxml import etree
# url = "https://movie.douban.com/cinema/nowplaying/changchun/"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
#     "Referer":"https://movie.douban.com/",
#     "Host":"movie.douban.com"
# }
#
# response = requests.get(url, headers=headers)
# text = response.content.decode("utf-8")
#
# html = etree.HTML(text)
# title = html.xpath("//div[@id='nowplaying']/div[@class='mod-bd']/ul[@class='lists']/li/@data-title")
# score = html.xpath("//div[@id='nowplaying']/div[@class='mod-bd']/ul[@class='lists']/li/@data-score")
# for i in range(len(title)):
#     print(title[i]+"\t",score[i]+"分")



##################################电影天堂############################################################
# import requests
# from lxml import etree
# import time
#
# BASIC_URL = "https://www.dytt8.net"
# f = open("movies.txt", "w+", encoding="utf-8")
# useragent = [
#     "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
# ]
# for i in  range(1,202):
#     time.sleep(0.5*(i%3))
#     url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html".format(i)
#     headers = {
#         "User-Agent":useragent[i%2],
#         "Referer":"https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html".format(i-1 if i!=0 else 1),
#     }
#     response = requests.get(url, headers=headers)
#     text = response.content.decode("gb18030","ignore")
#     html = etree.HTML(text)
#     title = html.xpath("//table[@class='tbspan']//a/text()")
#     href = html.xpath("//table[@class='tbspan']//a/@href")
#     for j in range(len(title)):
#         temp_href = BASIC_URL + href[j]
#         f.write(title[j]+"\t\t"+temp_href+"\n")
#     if not len(title):
#         print("爬取失败!")
#         break
#     else:
#         print("成功爬取第%s页!" %i)
# f.close()
# a = input()



# import pandas as pd
# from matplotlib import pyplot as plt
# file_path = "D:\pyprogram\PM2.5\BeijingPM20100101_20151231.csv"
# df = pd.read_csv(file_path)
# #把分开的时间字符串通过pd.PeriodIndex方法转换为pandas时间类型,并设置为索引
# period = pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],hour=df["hour"], freq="H")
# df["datatime"] = period
# df.set_index("datatime",inplace=True)
# df = df.resample("7D").mean()
#
# #删除缺失的数据
# data = df["PM_US Post"].dropna()
# data_china = df["PM_Dongsi"].dropna()
# #画图
# _x = data.index
# _x = [i.strftime("%Y%m%d") for i in _x]
# _x_china = [i.strftime("%Y%m%d") for i in data_china.index]
# _y = data.values
# _y_china = data_china.values
#
# plt.figure(figsize=(20,8),dpi=80)
# plt.plot(range(len(_x)), _y, label="US_POST")
# plt.plot(range(158,158+len(_x_china)), _y_china, label="CN_POST")
# plt.xticks(range(0,len(_x),10), list(_x)[::10], rotation=45)
# plt.legend(loc="best")
# plt.show()



# 腾讯招聘
# import time
# import requests
# import json
#
# for i in range(11, 31):
#     url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn"
#     now_time = int(time.time() * 100)
#     url = url.format(now_time,i)
#     headers = {
#         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
#     }
#     response = requests.get(url, headers=headers)
#     text = response.content.decode("utf-8")
#     text = json.loads(text)
#     data = text["Data"]["Posts"]
#     for i in range(len(data)):
#         job = {}
#         job["title"] = data[i]["RecruitPostName"] + "\n"
#         job["place"] = data[i]["LocationName"] + "\n"
#         job["duty"] = ""
#         duty = data[i]["Responsibility"].strip("\n").split("\r\n")
#         for j in range(len(duty)):
#             job["duty"] += duty[j]+"\n"
#         job["duty"] += "\n\n"
#         print(job)
#         with open("tencent_jobs.txt", "a+", encoding="utf-8") as fp:
#             fp.write(job["title"]+job["place"]+job["duty"])



# # 中国天气网
# import requests
# import html5lib
# from bs4 import BeautifulSoup
# place = ["hd","db", "hd","hz","hn","xb","xn","gat"]
# ALL_DATA = []
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
# }
# for p in place:
#     url = "http://www.weather.com.cn/textFC/{}.shtml".format(p)
#     html = requests.get(url=url, headers=headers).content.decode("utf-8")
#     soup = BeautifulSoup(html, "html5lib")
#     conMidtab = soup.find("div", attrs={"class":"conMidtab"})
#     tables = conMidtab.find_all("table")
#     for table in tables:
#         trs = table.find_all("tr")[2:]
#         for index,tr in enumerate(trs):
#             tds = tr.find_all("td")
#             if index==0:city_td = tds[1]
#             else:city_td = tds[0]
#             min_temp_td = tds[-2]
#             city = list(city_td.stripped_strings)[0]
#             min_temp = list(min_temp_td.stripped_strings)[0]
#             ALL_DATA.append({"city":city,"min_temp":int(min_temp)})
#
# ALL_DATA.sort(key=lambda data:data["min_temp"])
# data = ALL_DATA[0:10]
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
# _x = [i["city"] for i in data]
# _y = [i["min_temp"] for i in data]
# myfont = font_manager.FontProperties(fname="D:\pyprogram\FangZhengFangSongFanTi-1.ttf")
# plt.figure(figsize=(20,8), dpi=80)
# plt.xticks(range(10),_x,fontproperties=myfont)
# plt.plot(_x,_y)
# plt.show()



#
# import requests
# import re
# url = "https://www.gushiwen.org/default_1.aspx"
# def parse_page():
#     headers = {
#         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
#     }
#     response = requests.get(url, headers)
#     text = response.content.decode("utf-8")
#     title = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
#     time = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
#     author = re.findall(r'<p\sclass="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
#     contents = re.findall(r'<div\sclass="contson" .*?>(.*?)</div>',text,re.DOTALL)
#     peoms = []
#     for content in contents:
#         x = re.sub(r'<.*?>',"",content)
#         peoms.append(x.strip())
#     print(peoms)
# if __name__ == "__main__":
#     parse_page()


# import time
# def coding():
#     for x in range(3):
#         print("正在写代码%s"%x)
#         time.sleep(0.5)
#
# def drawing():
#     for x in range(3):
#         print("正在画图%s"%x)
#         time.sleep(0.5)
#
# def main():
#     coding()
#     drawing()
#
# if __name__ == "__main__":
#     main()



# #多线程
# import time
# import threading
# def coding():
#     for x in range(3):
#         print("正在写代码%s"%x)
#         time.sleep(0.5)
#
# def drawing():
#     for x in range(3):
#         print("正在画图%s"%x)
#         time.sleep(0.5)
#
# def main():
#     t1 = threading.Thread(target=coding)#创建线程
#     t2 = threading.Thread(target=drawing)
#     t1.start()#启动线程
#     t2.start()
#
# if __name__ == "__main__":
#     main()
#     # print(threading.enumerate())#打印线程数
#     # print(threading.current_thread())#打印当前线程的对象


# import threading
# import time
# class CodingThread(threading.Thread):
#     def run(self):
#         for x in range(3):
#             print("正在写代码%s"%x)
#             time.sleep(0.5)
# class DrawingThread(threading.Thread):
#     def run(self):
#         for x in range(3):
#             print("正在画图%s"%x)
#             time.sleep(0.5)
#
# def main():
#     t1 = CodingThread()
#     t2 = DrawingThread()
#     t1.start()
#     t2.start()
# if __name__ == '__main__':
#     main()


# #访问全局变量不需要加锁，修改全局变量才需加锁
# import threading
# tickets = 0
# glock = threading.Lock()
# def addt():
#     global tickets
#     glock.acquire()
#     for x in range(1000000):
#         tickets += 1
#     glock.release()
#     print(tickets)
#
# def main():
#     for x in range(2):
#         t = threading.Thread(target=addt)
#         t.start()
# if __name__ == '__main__':
#     main()


# #爬取表情包
# import requests
# from lxml import etree
# import re
# from urllib import request
# import os
# from queue import Queue
# import threading
# 
# class Producer(threading.Thread):
#     def __init__(self,page_queue,img_queue,*args,**kwargs):
#         super(Producer,self).__init__(*args,**kwargs)
#         self.page_queue = page_queue
#         self.img_queue = img_queue
# 
#     def run(self):
#         while True:
#             if self.page_queue.empty():break
#             url = self.page_queue.get()
#             self.parse_page(url)
# 
#     def parse_page(self,url):
#         headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
#         response = requests.get(url,headers=headers)
#         text = response.text
#         html = etree.HTML(text)
#         images = html.xpath("//div[@class='expression-list clearfix']//img")
#         imgs,srcs = [],[]
#         for i in images:
#             if re.search("gif$",i.xpath("./@src")[0]):pass
#             else:
#                 imgs.append(i)
#                 srcs.append(i.xpath("./@src")[0])
#         for index,img in enumerate(imgs):
#             img_url = srcs[index]
#             alt = img.get("alt")
#             alt = re.sub(r"[\?？\.，。！\!\*\\]",'',alt)
#             suffix = os.path.splitext(img_url)[1]
#             file_name = alt+suffix
#             self.img_queue.put((img_url,file_name))
# 
# class Comsumer(threading.Thread):
#     def __init__(self,page_queue,img_queue,*args,**kwargs):
#         super(Comsumer, self).__init__(*args, **kwargs)
#         self.page_queue = page_queue
#         self.img_queue = img_queue
#     def run(self):
#         while True:
#             if self.img_queue.empty() and self.page_queue.empty():break
#             img_url, file_name = self.img_queue.get()
#             request.urlretrieve(img_url,"images/"+file_name)
#             print(file_name,"下载完成!")
# 
# def main():
#     page_queue = Queue(10)
#     img_queue = Queue(100)
#     for x in range(1,11):
#         url = "https://www.doutub.com/img_lists/new/%d"%x
#         page_queue.put(url)
#     for x in range(5):
#         t = Producer(page_queue,img_queue)
#         t.start()
#     for x in range(5):
#         t = Comsumer(page_queue, img_queue)
#         t.start()
# 
# if __name__ == '__main__':
#     main()


# 图片验证码识别
# import pytesseract
# from urllib import request
# from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r"D:\Tools\TesseractOCR\tesseract.exe"
# url = "https://reg.mail.163.com/unireg/call.do?cmd=register.verifyCode&v=common/verifycode/vc_en&vt=main_acode"
# request.urlretrieve(url,"p.png")
# image = Image.open("p.png")
# text = pytesseract.image_to_string(image)
# print(text)


# -- coding:utf-8 --
import hashlib
import requests
import json


class Query_Scores:

    def __init__(self, user_id, pwd):
        self.user_id = user_id
        self.pwd = pwd
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15",
            "Origin": "https://uims.jlu.edu.cn",
            "Host": "cjcx.jlu.edu.cn",
        }

    def Login(self):
        self.pwd = "UIMS" + self.user_id + self.pwd
        m = hashlib.md5()
        m.update(bytes(self.pwd, encoding="utf-8"))
        self.pwd = m.hexdigest()
        login_url = "https://cjcx.jlu.edu.cn/score/action/security_check.php"
        self.headers["Referer"] = "https://cjcx.jlu.edu.cn/score/userLogin.php"
        data = {
            "j_username": self.user_id,
            "j_password": self.pwd,
        }
        self.session.post(url=login_url, data=data, headers=self.headers)

    def Get_Scores(self):
        service_url = 'https://cjcx.jlu.edu.cn/score/action/service_res.php'
        post_data = {
            'tag': 'lessonSelectResult@oldStudScore',
            'params': {
                'xh': self.user_id
            }
        }
        self.headers['Content-Type'] = 'application/json'
        self.headers['Referer'] = 'https://cjcx.jlu.edu.cn/score/action/index.php'
        res = self.session.post(url=service_url, data=json.dumps(post_data), headers=self.headers)
        data = res.content.decode('utf-8')
        data = json.loads(data)
        items = data['items']
        items.sort(key=lambda time: time['termId'], reverse=True)
        print('\n' + items[0]['studName'], items[0]['xh'] + '\n\n')
        print('课程名称\t课程绩点\t成绩\t对应绩点')
        for item in items:
            print(item['kcmc'], '\t', item['credit'], '\t', item['cj'], '\t', item['gpoint'])


def main():
    user_id = input('请输入学号:')
    pwd = input('请输入密码:')
    program = Query_Scores(user_id, pwd)
    program.Login()
    program.Get_Scores()
    a = input()

if __name__ == '__main__':
    main()
