import os,sys
bin1_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(bin1_path)
from core import core
core.Center().run()