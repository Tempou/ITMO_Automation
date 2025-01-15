#Задача 1
from itertools import count

a = 200
b = 335
if a > b:
    print(a)
else:
    print(b)


#Задача 2
a = 200
b = 335
if a + 135 == b:
    print('Yes')
else:
    print('No')


#Задача 3
def month_number(month):
    if month == 12 or month == 1 or month == 2:
        print('Зима')
    elif month in range(3,6):
        print('Весна')
    elif month in range(6,9):
        print('Лето')
    elif month in range(9,12):
        print('Осень')
month_number(2)


#Задача 4

def numbers():
    a=1
    b=1
    c=1
    if a and b and c > 10:
        print('Yes')
    else:
        print('No')
numbers()

#Задача 5
a = [1, -1, 2, -2, 3]
def numbers2(b):
    return b > 0
print(len(list(filter(numbers2, a))))


#Задача 6
def days(day):
    year = int(day.year)
    month = int(day.month)





