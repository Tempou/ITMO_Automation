#Задача 1
def task_1():
    a = 10
    print(a, type(a))

    b = 10.1
    print(b, type(b))

    c = 'Имя'
    print(c, type(c))

    d = [1, 5, 6, 4, 3]
    print(d, type(d))

    e = 'bools'
    print(bool, 9 > 3)
    return a,b,c,d,e
print(task_1(), '\n')


#Задача 2
def task_2():
    a = [1,2,3,5,8,13,21]
    print(a[0:3])
    return a
print('Числа Фибоначчи',task_2(),'\n')


#Задача 3
def task_3():
    a=7
    return a**2
print(task_3())











