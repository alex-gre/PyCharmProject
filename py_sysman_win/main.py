import wincomm

def menu():
	print("""
	   1 - Computer Manager 
	   2 - Clear Disk
	   3 - Show Services
	                           """)
menu()
i=0
i=int(input('select menu: '))
if (i==1):
     wincomm.comp_manager()
if (i==2):
     wincomm.clear_disk()         
if (i==3):
     wincomm.services()         
              
