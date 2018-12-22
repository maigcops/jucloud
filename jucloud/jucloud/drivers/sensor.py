# coding=utf-8
import socket
import time
import struct
import logging
from socketserver import BaseRequestHandler, ThreadingTCPServer
import threading
from portal import utils
BUF_SIZE=1024

logger = logging.getLogger(__name__)

class SensorHandler(BaseRequestHandler):

    def handle(self, start="0000",  data_length="0001"):
        address = self.client_address
        print("{}客户端连接".format(address))
        while True:
            data = self.request.recv(BUF_SIZE)
            if len(data)>0:
                print("客户端:{}, {}".format(address, data.decode('utf-8')))
                crc16 = utils.CRC16()
                hex_string = "0103{}{}".format(start ,data_length)
                crc_data = crc16.createcrc(hex_string)
                request_data = bytes.fromhex(hex_string)+hex(crc_data).encode("utf-8")
                self.request.sendall(request_data)

class SensorServer(object):

    def __init__(self, handler):
        host = '0.0.0.0'
        port = 15001
        addr = (host, port)
        self.serve(addr, handler)

    def serve(self, addr ,handler):
        logger.info("Server is starting")
        server = ThreadingTCPServer(addr, handler)
        print("listening")
        server.serve_forever()