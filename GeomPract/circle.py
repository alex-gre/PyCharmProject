import math, help_menu
def menu():
    m = """  Calculation:
            1)  Length Circle  
            2)  Square Circle
            3)  """
    print (m)
   # i = 0
    i = int(input('select menu: '))
    if (i==1):
        length_circle()
   # if (i==2):
        #quadr_square()
  #  if (i==3):
       # guadr_bulk()

def length_circle():
    help_menu.help_length_circle()
    d = int(input('Input diameter circle '))
    c = math.pi*d
    print(f'Value: = {c}')

