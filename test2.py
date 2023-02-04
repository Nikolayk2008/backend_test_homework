from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
          'квадратного корня из заданного числа')

"""Вычисляет квадратный корень"""
def Calculate_Square_Root(Amt):
    return  sqrt(Amt)

def calc(your_number):
    if your_number<=0:
        return    
x = Calculate_Square_Root(your_number)     
    print(f'Мы вычислили корень квадратный из введенного вами числа. Это будет {x}')

print(message)
calc (25.5)