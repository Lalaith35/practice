#Дан текстовый файл в формате csv. Каждая строка файла описывает одну
#фигуру. Разделитель полей в строке — запятая. Первое поле строки — тип
#фигуры, затем одно или два float-числа — размеры фигуры.
#Прининять список этих объектов и
#возвратить их суммарную площадь.

import os

class Circle:

	def __init__ (self, r = 2):
		self.r = r
		
	def area (self):
		return self.r*3.14
	def len_and_write (self, data, number ):
		len(data)
		
		if len(data)!=2:
			print ("Wrong number of parameters\nString ", number)
		else:
			try:
				Figure.append(Circle(float( data[1])))
			except ValueError:
				print ("Data Error \nString ", number)
	def __repr__(self):
		return ("Radius {}".format(self.r))


class Rectangle:

	def __init__ (self, a = 2, b = 3):
		self.a = a
		self.b = b
		
	def area (self):
		return self.a*self.b

	def len_and_write (self, data, number ):
		len(data)
		
		if len(data)!=3:
			print ("Wrong number of parameters\nString ", number)
		else:
			try:
				Figure.append(Rectangle(float( data[1]),float( data[2])))
			except ValueError:
				print ("Data Error \nString ", number)
	def __repr__(self):
		return ("a and b {} {}".format(self.a,self.b))

class Square:

	def __init__ (self, a = 2):
		self.a = a
		
	def area (self):
		return self.a**2

	def len_and_write (self, data, number ):
		len(data)
		
		if len(data)!=2:
			print ("Wrong number of parameters\nString ", number)
		else:
			try:
				Figure.append(Square(float( data[1])))
			except ValueError:
				print ("Data Error \nString ", number)
	def __repr__(self):
		return ("Square {} ".format(self.a))
		
try:
	File = open("Area.txt","r")
except FileNotFoundError:
	 print ("Append file to directory with programm")
	 exit()

classes = {"Circ":Circle, "Rect":Rectangle, "Sqr":Square}
Figure = []
string_number = 1
Area_square = 0

for string in File:

	string = string.strip()
	string = string.split(",")
	if string [0] in classes:
		object = classes[string[0]]
		obj = object()
		obj.len_and_write(string, string_number)
	else:
		print ("Wrong name of field \nString ", string_number)
	string_number += 1

for Area_items in Figure:
	Area_square += Area_items.area()

print(Area_square)

os.system("PAUSE")