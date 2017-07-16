#!/usr/bin/env python
#coding=UTF-8
'''
Created on 2017年7月15日

@author: liushy
'''
import paramiko
import scpclient
import argparse
import os
import socket
from contextlib import closing

class scpy(object):
    def __init__(self,host,port,username,password):
        #服务端相关配置
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        #self.remote_filename = None
    
    def cli(self):
        #输入参数：路径（默认当前路径）和pkg名
        parser = argparse.ArgumentParser(description='scp function for .pkg between two servers')
        parser.add_argument('--path', type=str, dest='path',default = os.path.dirname(os.path.realpath(__file__)),help='pkg path：default is current path')
        parser.add_argument('--file', type=str, dest='file',default = None, help='pkg filename: must be specified !')
        self.path = parser.parse_args().path
        self.filename = parser.parse_args().file
        self.remote_filename = parser.parse_args().file
        
    def scp(self):
        #创建ssh访问
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, self.port, self.username, self.password)
        #创建scp
        with closing(scpclient.Write(ssh.get_transport(), '~')) as scp:
            scp.send_file(self.path+'/'+self.filename, True, remote_filename = self.remote_filename)
        

def start():
    scp = scpy('192.168.199.233',22,'liushy','password')
    scp.cli()
    scp.scp()
    
if __name__=='__main__':
    start()
