import help_menu

def menu():
    m = """  Calculation:
            1) Perimeter 
            2) Square
            3) Bulk """
    print (m)
   # i = 0
    i = int(input('select menu: '))
    if (i==1):
        quadr_perimeter()
    if (i==2):
        quadr_square()
    if (i==3):
        guadr_bulk()

#===========================
#======procedure
def quadr_perimeter():
    help_menu.help_perimeter_quadrate()
    a = int(input('input a:'))
    print(f'Result: {a*4}')

def quadr_square():
    help_menu.help_square_quadrate()
    a = int(input('input a:'))
    print(f'Result: {a*a}')

def guadr_bulk():
    help_menu.help_bulk_quadrate()
    a = int(input('input a:'))
    print(f'Result: {a*a*a}')
