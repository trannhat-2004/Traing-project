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
matrix =[
    [1,2,3],
    [4,6,5],
    [7,10,11]
]
a = int(input('Nhap so hang: '))
b = int(input('Nhap so cot: '))
matrix = []
for i in range(a):
    row = []
    for j in range(b):
        row.append(int(input('Nhap phan tu thu:')))
    matrix.append(row)    
for i in range(a):
    for j in range(b):
        print(matrix[i][j], end = ' ')
    print()
    