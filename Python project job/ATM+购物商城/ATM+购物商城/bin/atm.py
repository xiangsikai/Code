import os,sys
atm_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(atm_path)
from core import list

list.list()
