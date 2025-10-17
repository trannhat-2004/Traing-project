import main2
#print("Hello one mỏe time")
#evething in input() is string
# two number divide always return float
# take the number as input
# take the initial cell population as input
# cells = int(input())

# # take the number of days as input
# days = int(input())

# # initialize the day counter
# counter = 1

# #complete the while loop
# while counter <= days:
#   cells = cells * 2
#   # Daily message
#   print("Day " + str(counter) + ": " +str(cells))
#   counter = counter + 1
# a = 18 
# is_student = True
# if a < 18:
#     if is_student:
#         print("You get a discount")
#     else:
#         print("You don't get a discount")
# else:
#     print("You don't get a discount")
# b = [] 
# for i in range(3):
#     a = int(input('Enter a number:'))
#     b.append(a)

# my_pet = b[2]
# print(my_pet)   
# số đầu tiên mang tính bao gồm, số cuối cùng mang tính loại trừ
# list = ["Tran", "phi",'Nhat']
# print(list[0])
# word = [list[:2]]
# print(word)
# #step counts for the past week
# steps = [1513, 5035, 7891, 1212, 2534, 4648, 3785]

#make a slice for the last 3 days
# word  = 'Tran Nhat'
# print('a' in word)
# a = [1,2,3]
# a.append(5)
# a. insert(3,'nhat')
# print(a[3])
# a.pop(1)
# print(a)
# #pop xoa di phan tu o vi tri pop
# #insert them phan phan tu vao vi tri index
# queue = ['John', 'Amy', 'Bob', 'Adam']
# name = input()
# #take an input
# print(queue)

#add the taken value to the end of the queue

count = 0

# def greet():
#     global count  # make count accessible inside the function
#     print("hello from greet function")
#     if count >= 5:
#         return  # stop recursion when count reaches 5
#     count += 1
#     greet()  # recursive call

# greet()
# def trueorfalse():
#     a = 5 + 1
#     return a
# print(trueorfalse())
# import tkinter as tk

# window = tk.Tk()
# window.title("Chào bạn!")
# window.geometry("300x200")

# label = tk.Label(window, text="Xin chào từ Tkinter!")
# label.pack(pady=20)

# button = tk.Button(window, text="Thoát", command=window.quit)
# button.pack()

# window.mainloop()
# def name(name = "tran nhat", num = 57):
#     print("Hello", name, num)

# name('Jonh',45)
# list_3 = [5,2,3,3,1,6]
# list_1 = 'nhat2'
# list_2 = ['1','2','3']
# def add_list(list_3, list_1):
#     return list_1 in list_3
# total = sum(list_3)
# total_2 = 0
# # for i in list_2:
# #     total_2 += int(i)
# list_33 = ['nhat','a chau', 'a bau','dep trai']
# total_2 = sum(map(int,list_2))
# print(total_2)
# print(add_list(list_3, list_1), total_2)
# print(sorted(list_3, reverse = True))
# print(sorted(list_33))
# learn about tuple
# list_1 = [1,2,3,4,5,3,3,4]
# day , month, year = list_1[:3]
# tuple_1 = (1,2,3,4,5,3,3,4)
# # phải đầy đủ thì mới gán được giá trị
# a,b,c,d,e,f,g,h = tuple_1
# # * dùng khi không biết độ dài của tuples(bo du lieu) và nó sẽ tạo ra một list
# winer ,*rest = tuple_1
# print(winer)
# print(type(rest))
# print(a,b,c)
# print(tuple_1)
# print(tuple_1.count(3))
# print(max(tuple_1))
# print(min(tuple_1))
# print(len(tuple_1))
# print(list_1.count(3))


# tuple_1[0] = 5 # error because tuple is immutable
#tuple có thể thay đổi nhưng list thì không và nó thường dùng để lưu trữ các giá trị không thay đổi
# đây là sets và nó không có thứ tự và không có phần tử trùng lặp
# set_1 = {1,3,"nhat", 'tran'}
# print(set_1)
# # print(set_1[0]) # error because set is unordered
# # sets sử dụng add và remove để thêm và xóa phần tử
# set_1.add(5)
# set_1.add('nhat ')
# set_1.remove(3)
# print(set_1)
# # difference() trả về các phần tử có trong set_1 nhưng không có trong set_2
# set_2 = {1,2,3,4,5}
# print(set_1.difference(set_2))
# print(set_2.clear())
#clear xóa tất cả các phần tử trong set

# thu_vien = {
#     'name' : 'nhat tran',
#     'age' : 18,
#     'float_2' :3.7 
# }
# info_key = thu_vien.keys()
# info_item = thu_vien.items()
# infor_value = thu_vien.values()
# print(info_key)
# print(infor_value)
# print(thu_vien)
# thu_vien['name'] = 'nhat dep trai'
# thu_vien.update({'intenger' : 37})
# thu_vien.update({'age' : 19})
# thu_vien.pop('float_2')
# print(info_item)
# print('float_2' in thu_vien, 'age' in thu_vien)
# print('nhat dep trai' in thu_vien.values())
# for i in thu_vien:
#     print(i)
# for i in thu_vien.values():
#     print(i)

# list_6=['#'+str(x).capitalize() for x in thu_vien.values()]
# print(list_6)

# def fibonacci(n):
# matrix =[
#     [1,2,3],
#     [4,6,5],
#     [7,10,11]
# ]
# a = int(input('Nhap so hang: '))
# b = int(input('Nhap so cot: '))
# matrix = []
# for i in range(a):
#     row = []
#     for j in range(b):
#         row.append(int(input('Nhap phan tu thu:')))
#     matrix.append(row)    
# for i in range(a):
#     for j in range(b):
#         print(matrix[i][j], end = ' ')
#     print()
# for i in range(a):
#     for j in range(b):
#         if matrix[i][j] %2 == 0:
#             print(matrix[i][j], end = ' ')
#     print()
# prices = [250, 300, "240", 400]
# try:
#   #block that may cause an exception
#   total = sum(prices)
#   print(total)

# except TypeError:
#   # to perform if there is an exception
#   print("Invalid data type")

# # print("Happy Shopping")
# total = 0
# list_1 = [1,2,3,4,5]
# try:
#     for i in range(len(list_1)):
#        total += list_1[i]
# except :
#     print('Error')
# finally:
#     print('Done and dont worry')
# # có thể dùng else trong trường hợp không có lỗi nào
# list_2 = [1,2,3,4]
# try:
#     total_2 = sum(list_2)
#     print(total_2)
# except:
#     print('error')
# else:
#     print('no error will display')


# name = ' tran nhat'
# try:
#     count = int(name)
# except ValueError as e:
#     print('Error: ',e)
# def hola(name):
#     return 'Hola'+name
# greet = hola
# # print(hola('nhat'))
# greet = lambda a = 6, b = 4 :  a+b
# print(greet(6,7))
# hi = (lambda a , b : a * b) (4,6)
# print(hi)
# students = [("Nam", 18), ("An", 20), ("Bình", 17)]
# list_1 = [1,2,3,4,6,5]
# # Sắp xếp theo tuổi (phần tử thứ 2)
# students.sort(key=lambda x: x[1])
# print(students)
# list_1.sort(reverse=True)
# print(list_1)
# xin_chao = lambda x : x.capitalize()
# print(xin_chao('tran nhat'))
# [('Bình', 17), ('Nam', 18), ('An', 20)]

# name = ['tran', 'nhat', 'dep', 'trai']
# name_1 = map(lambda x : x.capitalize(), name)
# name_1 = list(name_1)
# print(name_1)
# dict_1 = {'a':1, 'b':2, 'c':3}
# number = [1,2,3,4]
# number_2 = list(map(lambda x : x *2, number) )
# number_3 = list(filter(lambda x : x %2 == 0, number))
# number_4 = dict_1.values()
# number_5 = list(map(lambda x : x*2,dict_1.values()))
# number_6 = dict_1.values()  
# for i in number_6:
#     print(i)
# print((lambda x : x * 2) (5))
# print(number_2)
# print(number_3)
# print(number_4)
# print(number_5)
# print(number_6)
# tuple_1 = (1,2,3,4,5)
# a, *b = tuple_1
# print(a,b)
# def name (*args):
#     for i in args:
#         print(i)
# name ('tran', 'nhat', 'dep', 'trai')
# *args is a tuple and it can take any number of arguments
# def add_name (nhat , * args):
#     print('Hello', nhat)
#     for i in args:
#         print('Hi', i)
# add_name ('nhat', "tran" , "nhat" , "trai") 

# #**kwargs is a dictionary
# def display_info(**kwargs):
#   #kwargs.items() returns the key:valie pairs
#   for key, value in kwargs.items():
#     print(key, ":", value)

# display_info(name="Alice", age=30, city="New York")

# def dict_take_name(**hi):
#    for key, valur in hi.items():
#       print(key, ":", valur)
# dict_take_name(name = 'nhat', age = 18, city = 'hanoi',height = 1.8)

# def multiple_1(hi, *args, **kwargs):
#    print('Hello',hi)
#    for i in args:
#       print('Hi', i)
#    for keyy, value in kwargs.items():
#       print('', keyy, ":", value)
# multiple_1('nhat', 'tran', 'dep', 'trai', age = 18, city = 'hanoi', height = 1.8)
# def order():
#   def prepare():
#     return "Your meal is being prepared!"
#   status = prepare()
#   return status
# # print(order())
# def stock_status_decorator(func):
#     def wrapper(item):
#         result = func(item)
#         print(result, ": stock status for", item)
#         return result
#     return wrapper

# @stock_status_decorator
# def restock_item(item):
#     return "Restocked"

# @stock_status_decorator
# def sell_item(item):
#     return "Sold"

# print(restock_item("Laptop"))
# print(sell_item("Smartphone"))
# 
# def an_object(Cat):
#     return Cat()
# cat = an_object(main2.Cat())
# print(cat)
#parent class
# class Animal:
#   def __init__(self, name):
#     self.name = name
  
#   def move(self):
#     print("Moving")

# #child class
# class Dog(Animal):
#   def __init__(self, breed, age):
#     # Initialize attributes of the superclass
#     # Additional attributes specific to Dog
    
#     self.breed = breed
#     self.age = age

#   def bark(self):
#     print("Woof!")


# my_dog = Dog( "Bulldog", 5)
# #inherited attribute
# print(my_dog.name)

# #Additional attributes
# print(my_dog.breed)
# print(my_dog.age)
a = 1000021
# b = str(a)
# list_1 = []
# for i in range(len(b)):
#     list_1.append (b[i])
# list_1.reverse()
# for i in range(len(b)):
#     if b[i] != list_1[i]:
#         print("false")
#     else:
#         print("true")


    

