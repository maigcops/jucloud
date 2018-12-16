# coding=utf-8
import socket
import time
import struct
import logging

logger = logging.getLogger(__name__)


class SensorDriver(object):

    def __init__(self):
        sock = self.get_socket()
        self.connection, self.address = sock.accept()

    def get_socket(self):
        logger.info("Server is starting")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 15001)) #配置soket，绑定IP地址和端口号
        sock.listen(5) # 设置最大允许连接数，各连接和server的通信遵循FIFO原则
        logger.info("Server is listenting port 15001, with max connection 5")
        return sock

    def send(req_data):
        self.connection.send("")
        return data

    def run(self):
        while True: #循环轮询socket状态，等待访问
            try:
                peer_host, peer_port=self.connection.getpeername()
                self.connection.settimeout(100000)
            # 获得一个连接，然后开始循环处理这个连接发送的信息
            '''''
            如果server要同时处理多个连接，则下面的语句块应该用多线程来处理，
            否则server就始终在下面这个while语句块里被第一个连接所占用，
            无法去扫描其他新连接了，但多线程会影响代码结构，所以记得在连接数大于1时
            下面的语句要改为多线程即可。
            '''
            while True:
                time.sleep(30)
                buf = self.connection.recv(1024)
                connection.send(b"\x01\x03\x00\x00\x00\x02\xC4\x0B")
                if buf == '1':
                  print(">{}:send welcome".format(peer_host))
                  connection.send('welcome to server!')
                elif buf=='bye':
                  print(">{}:buf:{}".format(peer_host, buf))
                  connection.send('bye bye!')
                  print("close")
                  break #退出连接监听循环
                elif buf=='www.usr.cn':
                  print(">{}:buf:{}".format(peer_host, buf))
                else:
                  dataprint("get data", peer_host, buf)
                  print(b"\x01\x03\x00\x00\x00\x02\xC4\x0B")
                  connection.send(b"\x01\x03\x00\x00\x00\x02\xC4\x0B")
        except socket.timeout: #如果建立连接后，该连接在设定的时间内无数据发来，则time out
             logger.error('time out')
        self.close()
        

    def close(self):
        logger.info("closing one connection") #当一个连接监听循环退出后，连接可以关掉
        self.connection.close()
