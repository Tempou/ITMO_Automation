#Задача 1
def larger_number():
    a = 20
    b = 30
    if a > b:
        print(a)
    else:
        print(b)
larger_number()


#Задача 2
def diff_numbers():
    a = 335
    b = 200
    if a - b == 135:
        print('Yes')
    else:
        print('No')
diff_numbers()


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
def days(year:int, month:int):
    return year * 12 * 29 + month * 29
print(days(39, 19))







