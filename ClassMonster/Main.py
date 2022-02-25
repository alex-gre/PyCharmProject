class ClassMonster:
    def __init__(self, x,y):# конструктор класса
        print('Monster initialize...')
        self.x_coordinate = x   # поля
        self.y_coordinate = y

    def moveme(self, new_x,new_y):
        print('Moveme to ...')
        self.x_coordinate = self.x_coordinate + new_x
        self.y_coordinate = self.y_coordinate + new_y


zombie = ClassMonster(24,45)
print(f'Coordinate x = {zombie.x_coordinate} y = {zombie.y_coordinate}')
zombie.moveme(36,20)
print(f'x = {zombie.x_coordinate} y = {zombie.y_coordinate}')

