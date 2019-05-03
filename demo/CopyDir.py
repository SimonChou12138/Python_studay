from multiprocessing import Pool,Manager
import os
import time

def copy(name,oldFolder,newFolder,queue):
    # 打开
    fr = open(oldFolder+"/"+name)
    # 写入
    fw = open(newFolder+"/"+name, "w")

    temp=fr.read()#保存读取的数据
    fw.write(temp)#写入读取的数据

    queue.put(name)#进程队列里面添加name

    fr.close()
    fw.close()

def main():
    # 1.首先获取旧的文件夹名字
    oldFolder = input("请输入您想要复制的文件夹名字:")
    # 2.赋予新文件夹新的名字
    newFolder = oldFolder + "-副件"
    os.mkdir(newFolder) #新建文件夹

    fileName=os.listdir(oldFolder)#获取文件夹中的所有文件

    p=Pool(5)#创建进程池
    queue=Manager().Queue()#进程内部数据共享
    allNum=len(fileName)
    num=0

    for name in fileName:
        p.apply_async(copy,args=(name,oldFolder,newFolder,queue))

    while True: #进度条
        queue.get()
        num+=1
        culum=num/allNum
        print("\r---复制的进度是:%d%%"%(culum*100),end="")
        time.sleep(1)
        if num==allNum:
            break

    p.close()
    p.join()

if __name__=="__main__":
    main()