import rect, circle

def menu():
    print("""
        1 - Select Quadrate and Rectengle
        2 - Select Triangle and Trapeze
        3 - Select Circle  and Sphere
    """)
menu()
i = int(input('select menu: '))
if (i==1):
    rect.menu()
if (i==2):
    menu()
if (i==3):
   circle.menu()
