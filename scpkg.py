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
"""
#向jenkins发送消息    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
#print s.recv(1024)
# 发送数据:
s.send(args.pkg)
#print s.recv(1024)
s.send('exit')
s.close()
"""
#本地文件相关配置
path =  ''
pkg = ''
#服务端相关配置
host = '192.168.199.233'
port = 22
username = 'liushy'
password = 'password'
remote_pkg = None

def cli():
    #输入参数：路径（默认当前路径）和pkg名
    global path,pkg
    parser = argparse.ArgumentParser(description='scp function for .pkg between two servers')
    parser.add_argument('--path', type=str, dest='path',default = os.path.dirname(os.path.realpath(__file__)),help='pkg path：default is current path')
    parser.add_argument('--pkg', type=str, dest='pkg',default = None, help='pkg filename: must be specified !')
    path = parser.parse_args().path
    pkg = parser.parse_args().pkg
    print path+'/'+pkg
    
def scp():
    #创建ssh访问
    global path,pkg
    print path+'/'+pkg+'xxxxx'
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, username, password)
    remote_pkg = pkg
    #创建scp
    with closing(scpclient.Write(ssh.get_transport(), '~')) as scp:
        scp.send_file(path+'/'+pkg, True, remote_filename = remote_pkg) 

if __name__=='__main__':
    cli()  
    scp() 
