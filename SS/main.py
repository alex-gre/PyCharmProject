#organizer sqlite3 project for python 3.8

import organizerdb

def menu():
    print("""
        1 - Input contacts organizer.db
        2 - View select contacts   
        3 - Clear Table
    """)
menu()
i = int(input('select menu: '))
if (i==1):
    organizerdb.input_contacts_base()
if (i==2):
    organizerdb.view_table()

if (i==3):
    sq=input('You delete table Y yes/N no > ')
    if (sq=='Y'):
      organizerdb.clear_table()
    if (sq=='N'):
        exit()



       