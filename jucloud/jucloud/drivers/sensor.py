# coding: utf-8
import socket
import time
import struct
import logging
from socketserver import BaseRequestHandler, ThreadingTCPServer
import threading
from portal import utils
from portal import models
BUF_SIZE=1024

logger = logging.getLogger(__name__)

class SensorHandler(BaseRequestHandler):

    def handle(self, data_addr=0,  data_len=1):
        address = self.client_address
        print("客户端{}已连接".format(address))
        server_addr=1
        func=3
        arr=[
                server_addr,
                func,
		0,
                data_addr,
		0,
                data_len
            ]
        while True:
            data = self.request.recv(BUF_SIZE)
            if len(data)>0 and data!=b'www.usr.cn':
                print("客户端:{}, data:{}".format(address, data))
                print("客户端:{}, data:{}".format(address, data.hex()))
                self.input_temperature(data.hex())
            else:
                print("客户端:{}, data:{}".format(address, data))
            crc16 = utils.CRC16()
            crc_data = crc16.createcrc(arr)
            request_data=struct.pack('>BBHHH', server_addr, func, data_addr, data_len, crc_data)
            print("request_data:{}".format(request_data))
            self.request.sendall(request_data)
            time.sleep(600)

    def input_temperature(self, data):
        origin_data = int(data[6:10], 16)	
        display_data = origin_data*0.1
        temperature_sensor = models.Sensor.objects.get(code='0X0000')
        print("tempreture:{}".format(display_data))
        models.Message.objects.create(
            data=data[6:10],
            display_data=display_data,
            sensor=temperature_sensor
        )

class SensorServer(object):

    def __init__(self, handler):
        host = '0.0.0.0'
        port = 15001
        addr = (host, port)
        self.serve(addr, handler)

    def serve(self, addr ,handler):
        logger.info("Server is starting")
        server = ThreadingTCPServer(addr, handler)
        server.serve_forever()


class ProxyHandler(object):

    def __init__(self, sock):
        self.connection , self.client_address = sock.accept()
        print("connection:{},client_address:{}".format(self.connection, self.client_address))
        self.peer_host, self.peer_port=self.connection.getpeername()
        print("peer_host:{},peer_port:{}".format(self.peer_host, self.peer_port))
        self.crc16 = utils.CRC16()

    def get_request_data(self, data_addr=0, data_len=1):
        server_addr=1
        func=3
        arr=[
                server_addr,
                func,
		0,
                data_addr,
		0,
                data_len
            ]
        crc_data = self.crc16.createcrc(arr)
        request_data=struct.pack('>BBHHH', server_addr, func, data_addr, data_len, crc_data)
        print("request_data:{}".format(request_data))
        return request_data

    def dataprint(self, data):
        try:
            print("peer_host:{}, data:{}".format(self.peer_host, data))
            print("peer_host:{}, data:{}".format(self.peer_host, data.hex()))
        except Exception as ex:
            print("data:{},exception:{}".format(data, ex))


    def handle(self):
        try:
            self.connection.settimeout(100000)
            while True:
                time.sleep(10)
                buf = self.connection.recv(1024)
                request_data = self.get_request_data()
                self.connection.send(request_data)
                if buf == '1':
                    print("peer_host:{}, data:{}, send welcome".format(self.peer_host, buf))
                    self.connection.send('welcome to server!')
                elif buf=='bye':
                    print("peer_host:{}, data:{}, send bye bye".format(self.peer_host, buf))
                    self.connection.send('bye bye!')
                    break #退出连接监听循环
                elif buf=='www.usr.cn':
                    print("peer_host:{}, data:{}, send nothing".format(self.peer_host, buf))
                else:
                    print(buf)
                    self.dataprint(buf)
                    self.connection.send(request_data)

        except socket.timeout: #如果建立连接后，该连接在设定的时间内无数据发来，则time out
             print('time out')
        print("closing one connection") #当一个连接监听循环退出后，连接可以关掉
        self.connection.close()


class Server(object):

    def __init__(self, handler):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 15001)) #配置soket，绑定IP地址和端口号
        sock.listen(5) #设置最大允许连接数，各连接和server的通信遵循FIFO原则
        print("Server is listenting port 15001 , with max connection 5")
        while True:
            handler(sock).handle()
