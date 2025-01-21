#Задача 1
def task_1(a: int='3', b: float = '10.1', c: str='Имя', d: list = [1,5,6,4,3], e: bool=True ) :
    return type(a),type(b),type(c),type(d),type(e)
print(task_1(), '\n')


#Задача 2
def task_2():
    a = [1,2,3,5,8,13,21]
    print(a[0:3])
    return a
print('Числа Фибоначчи',task_2(),'\n')


#Задача 3
def task_3(a:int) -> int:
    return a*a
print(task_3(10))











