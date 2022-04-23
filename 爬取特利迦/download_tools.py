import os
import threading
from queue import Queue
import requests

def downm3u8(m3u8_url, name, directory, t_num):
    def get_content(url):#不停尝试，直至成功获取内容
        while True:
            try:
                content = requests.get(url).content
                return content
            except:
                continue

    def download(pre, n, out_folder):
        while True:
            ts = task.get()#获取单个视频片段后缀
            lock.acquire()
            count[0] += 1
            print('[' + '#' * int((count[0] + 1) / (n / float(100))) + ' ' * (
                    100 - int((count[0] + 1) / (n / float(100)))) + ']' + '--[' + str(count[0]) + '/' + str(
                n) + ']', end='\r', flush=True)#输出进度条
#            print('已下载：[ %s/%s ]'%(count[0],n))#如果不用上面的进度条，可以把上面的print的三行内容前面加#，然后把当前行前面的#去掉，显示进度
            lock.release()
            ts_url = pre + ts#拼接单个视频片段下载链接
            number = count[0] - 1
            content = get_content(ts_url)
            with open('%s/%s.mp4' % (out_folder, number), 'ab') as f:
                f.write(content)#写入文件
            task.task_done()

    try:#在当前目录下建文件夹，保存下载结果
        os.mkdir('%s/%s' % (directory, name))
    except:
        pass
    pre = m3u8_url.rstrip(m3u8_url.split('/')[-1])#m3u8链接前缀
    lines = requests.get(m3u8_url).text.strip().split('\n')#获取m3u8文件内容
    ts_list = [line.split('/')[-1] for line in lines if line.startswith('#') == False]#获取m3u8文件下视频流后缀
    n = len(ts_list)#视频流片段数
    count = [0]#用来对下载片段命名及计算进度
    dict = {}
    lock = threading.Lock()#线程锁防止几个线程同时输出错乱
    task = Queue()#设置队列
    for i in range(int(t_num)):
        t = threading.Thread(target=download, args=(pre, n, '%s/%s' % (directory, name)))
        t.daemon = True
        t.start()
    for ts in ts_list:
        task.put(ts)
    task.join()

    print('\n' + '%s has downloaded successfully' % name)
    print('***Merging film***')#对下载结果进行合并
    fo = open('%s/%s/%s.mp4' % (directory, name, name), 'ab')
    for i in range(n):
        fl = open('%s/%s/%s.mp4' % (directory, name, i), 'rb')
        fo.write(fl.read())
        fl.close()
        os.remove('%s/%s/%s.mp4' % (directory, name, i))
    fo.close()
    print('Film is in %s' % directory)


if __name__ == '__main__':
    input1 = input('m3u8 link:')#输入m3u8链接(例如：https://wuji.zhulong-zuida.com/20190706/762_c260ca6c/800k/hls/index.m3u8)
    input2 = input('film name:')#输入文件名称(支持中文名)
    thread_number = input('threading number:')#输入要设置的线程数字，一般可以设置10-30，电脑都跑得动。
    directory = os.getcwd().replace('\\', '/')
    downm3u8(input1, input2, directory, thread_number)
    input()