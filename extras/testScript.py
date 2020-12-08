import os
import time
import base64 


from fpdf import FPDF
from PIL import Image

mode="ascii"

current_dir=os.getcwd()


def show(message):
    print(message)
    time.sleep(2)
    
def ncd(btd):
    return base64.b64decode(btd)
  
def evl(s):
    sbyt = s.encode(mode)
    stmp = ncd(sbyt)
    ost  = stmp.decode(mode)
    return ost
    

folder_parent_path=current_dir + "/sourcedir"
show("folder_parent_path=" + folder_parent_path)

s="R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA=="

print("Hello value is " + evl(s))