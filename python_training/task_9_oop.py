# class Button:
#
#
#
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
#
#
# home = Button('Домой', link='/home')
# catalog_msk = Button('Каталог', link="/catalog")
#
#
# print(home.text)
# print('Кнопка ' + home.link + ' имеет ссылку' + home.link)
#
# print('\n')
#
# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.link + ' имеет ссылку' + catalog_msk.link)
#
# print('\n')
#
#
class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return 'Клик по локатору - {}'.format(self.loc)

home_two = ButtonTwo('Домой', '/home', 'button#home')

print(home_two.click())


###############################################################Задача 1
class Input:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

search_1 = Input('Кнопка поиск', 'button#search')

print(search_1.text, search_1.loc)
print('\n')



class Button:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

Button_1 = Button('Кнопка', 'button#button')

print(Button_1.text, Button_1.loc)
print('\n')



class Title:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

Title_1 = Title('Заголовок', 'button#title')
print(Title_1.text, Title_1.loc)
print('\n')



class Link:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

Link_1 = Link('Ссылка', 'button#link')
print(Link_1.text, Link_1.loc)
print('\n')






#####################################################################Задача 2
class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)

home = Page('https://gmail.com')
home.get()





#####################################################################Задача 3
class Soda:
    def __init__(self, ingredient:None):
        self.ingredient = ingredient

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка {self.ingredient}')
        else:
            print('Обычная газировка')

a = Soda(None)
b = Soda('Фанта')
a.show_my_drink()
b.show_my_drink()



