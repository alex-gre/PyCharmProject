# -*- coding: utf-8 -*-
import os

def clear_disk():
    print ('===============')
    print ('CLEAR DISK: ')
    os.system("cleanmgr")
    print('OK')
    
def comp_manager():
    print ('===============')
    print ('COMPUTER MANAGER: ')
    os.system("compmgmt.msc")
    print('OK')
    
def services():
    print ('===============')
    print ('SERVICES: ')
    os.system("services.msc")
    print('OK')
    
    




