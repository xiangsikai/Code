import sys,os
bin_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(bin_path)
from core import main
obj = main.Select_ftp()
obj.action_select()