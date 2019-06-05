# -*- coding:utf-8 -*-
import os,sys
bin_server_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(bin_server_path)
from core import core
server = core.ftp_login()
server.ftp_core()
