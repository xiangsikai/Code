#-*- coding:utf-8 -*-
import os,sys,logging
loger_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(loger_path)
loger_log = os.path.dirname(os.path.abspath(__file__))

#日志结构
logging.basicConfig(filename='%s\\filelog\\Atm_loger.log'%(loger_log),
                    level=logging.INFO,
                    format='%(asctime)s    File:%(filename)s   %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

