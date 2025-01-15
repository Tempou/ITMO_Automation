#Программа проверяет является число положительным
#или отрицательным и выводит соответствующее сообщение


#num = 1
#
# # Другие варианты значения num (тест)
# # #num = -5
# # #num = 0
#
#
# if num >= 0:
#     print('Число больше либо равно 0')
# else:
#     print('Число отрицательное')
#
################################################################### #Задача
# #str_2 содержит в себе str_1?
#
# str_1 = 'test'
# str_2 = 'test1'
#
# if str_1 in str_2:
#     print('Да')
# else:
#     print('Нет')
#

#################################################################### ##Elif
# num_float = 0
# #Другие варианты num_float : 0     -6.1
#
# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('Равно нулю')
# else:
#     print('Отрицательное число')


#################################################################### #if-or and
# permit_print = True
# if num > 0 and permit_print:
#     print('num - положительно число')
# elif not permit_print:
#     print('Печать запрещена')

def course_studentt(study_year):
    if study_year in range(1,5):
        print('Вы - бакалавр')
    elif study_year in range(5,7):
        print('Вы - магистр')
    elif study_year in range(7,9):
        print('Вы - аспирант')
    else:
        print('Введите корректный год обучения')

course_studentt(4)



def number(number_100):
    if number_100 <= 100:
        print('-')
    else:
        print('+')
number(-100)