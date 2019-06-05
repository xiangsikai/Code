import os,sys
bin_client_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(bin_client_path)
from core import core
client = core.ftp_login()
client.ftp_core()