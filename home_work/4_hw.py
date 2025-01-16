#Задача 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        print(self.width * self.height)

    def perimeter(self):
        print(self.width + self.height)

a = Rectangle(30, 40)
b = Rectangle(50, 60)
c = Rectangle(70, 80)

a.square()
a.perimeter()
b.square()
b.perimeter()
c.square()
c.perimeter()
print('\n')



#Задача 2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print (self.a + self.b)

    def multiplication(self):
        print (self.a * self.b)

    def division(self):
        print (self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

number = Math(1, 2)
number.addition()
number.multiplication()
number.division()
number.subtraction()
print ('\n')



#Задача 3
class Buttons1:
    def __init__(self, text, type, loc=None):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return('Клик по кнопке - {}'.format(self.text))

text_box = Buttons1('Text Box','Кнопка', Buttons1.click)
check_box = Buttons1('Check Box', Buttons1.click)
radio_button = Buttons1('Radio Button', Buttons1.click)
web_tables = Buttons1('Web Tables', Buttons1.click)
buttons = Buttons1('Buttons', Buttons1.click)
links = Buttons1('Links', Buttons1.click)
broken_links_images = Buttons1('Broken Links - Images', Buttons1.click)
upload_and_download = Buttons1('Upload and Download', Buttons1.click)
dynamic_properties = Buttons1('Dynamic Properties', Buttons1.click)

print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(broken_links_images.click())
print(upload_and_download.click())
print(dynamic_properties.click())











