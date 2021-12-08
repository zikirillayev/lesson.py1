
# first lesson
# ________________________________________________
# number = 5
# int = integer = butun son e.g: 1,2,3,4,5,6,7,8,9...
# float = residual number = qoldiqli sonlar e.g: 1.2 ; 2.5 ...
# modul = 45 % 6 
# print(modul) # 3 (it prints residues)
# devide = 3 / 2
# print(devide)
# // #(it gives integer)


# ________________________________________________
# day = "friday"
# tomorrow = " saturday"
# result = day + tomorrow
# print(result)
# result = day * 10
# print(result)
# devide & minus are imposible to solve


# list_________________________________________
# test1 = [1,2,3,4,5,6,7,8,9]
# test2 = ["Monday","Tuesday"]

# test = test1 + test2
# test1[0] = 2
# test = test1 + test2
# test.append(571) #it can add smth new at the end
# test.pop() #it can remove from the end 
# test[2:4] = [] #remove from at the beginning 
# test[:2] = ["hello" , "world"]
# print(test)

# # working with append
# user = ['me']
# # user.append() append is only able to add one argument !!!!
# user[1:] = ['sister' , 'brother' , 'mum' , 'dad']
# print(user)
# print("Good morning,Have a nice day")
# # versiyani tekshirish terminalda python -V yozamiz

# print(9**2) #darajaga ko`tarish

# print("\"Nexia\" , \"Tico\" , \'Damas\' ko`rganlar qilas havas ")
# print(5**4)
# print("qoldiq:",22%4)
# a = 125
# res1 = a*a
# res2 = a + a + a + a
# print('s=',res1 , 'p=',res2)

# d = 12
# res3 = d * 3.14
# print('surface of the circle', res3)

# k1 = 6
# k2 = 7
# res4 = (k1**2) + (k2**2)
# print(res4)

# name = "Saidali"
# age = 18
# print(name)
# print(age)

# simple = "Hello World"
# print(simple)

# text = "assalomu alaykum"
# text = "va alaykum assalom"
# print(text)

# # class = "wrong"
# # print(class)

# taple = (4,5,'monday')
# taple1 = taple[:2] #slicing
# addingTaples = taple + taple1 #taplelarni qo`shish`
# print(addingTaples)

# multiply = taple * 5 #ko`paytirish
# # del multiply
# print(multiply)

# # dictionaries
# # {'key': 'text'}
# c1 = {1:['Monday' ,12 ,'meee'] , 2:'Tuesday' , 3:'Wednesday'}
# print(c1[1][2])

# # loops
# # for & while

# for i in range(3):
#     print(1)

# friends = ['Said', 'Ali', 'Xon']
# for a in friends:
#     print(a)

# # text1 = "Saidali"
# # for k in text1:
# #     print(k)


# # # boolean
# # # 1 true
# # # 2 false

# # # and while now
# # # while loop
# # for i in range(10):
# #     print(0)

# # ab = 5
# # while ab == 5:
# #     print(2)
# #     ab = 0


# # # if statements
# # v = 5
# # if 5 * 3 == 15:
# #     print("true")

# # z = "welcome"
# # if  z == "new":
# #     print("bye")
# # elif z == "welcome":
# #     print("allow")
# # elif z == "":
# #     print("empty")
# # else :
# #     print("I could not find")



# #     # functions
# # def test():
# #     print('I am here')
# # test()

# # def fun(f, g = 12):
# #    print(f + g)
# # fun(3, 21)


# # # types of the functions
# # # fruitful vs void
# # def flue():
# #     a = 32
# #     b = 32
# #     d = a + b
# #     return d

# # r = flue()
# # print(r) 

# # def block(o , p ):
# #     j = o+p
# #     return j

# # t = block(1,2)
# # print(t)

# # # void functionga tushunmadim

# # # global and local scope

# # a = 9

# # def misol():
# #     global a 
# #     a = a + 4 
# #     b = 8
# #     print(a)
    
# # misol()

# # # module
# # # package - math matematika package, pyg pygame
# # # library

# # # import pygame 
# # import turtle

# # wn = turtle.Screen()
# # test == turtle.Turtle()
# # # test.forward(50)
# # test.left(90)



# wn.mainloop()




import turtle
def func1():
    tosh.pencolor(colors[color])
    tosh.forward(50)

def func2():
    tosh.left(45)

def func3():
    tosh.right(45)

def func4():
    wn.bye()

def func5():
    global pensz
    pensz += 1
    tosh.pensize(pensz)
    
def func6():
    global pensz
    pensz -= 1
    if pensz > 0:
        tosh.pensize(pensz)
    else:
        pensz = 1
        tosh.pensize(pensz)
        
    print(pensz)

def func7():
    global ruchka
    if ruchka == 1:
        tosh.penup()
        ruchka = 0
    else:
        tosh.pendown()
        ruchka = 1

def func8():
    tosh.pencolor("green")
    tosh.back(50)

def func9():
    global color
    colors = ["yellow" , "orange" , "red" , "blue"]

    tosh.pencolor(colors[color])
    if color > 2:
        color = 0
    else:
        color += 1
    print(color)



def func10(text, x , y):
    meeting = turtle.Turtle()
    meeting.hideturtle
    meeting.penup()
    meeting.goto(x, y)
    meeting.write(text , font=10)

def main():
    global tosh
    global wn
    global pensz 
    global ruchka
    global color
    global colors
    color = 0
    pensz = 1
    ruchka = 1
    wn = turtle.Screen()
    wn.setup(700,500)
    wn.title("toshiba")
    wn.bgcolor("green")
    colors = ["yellow" , "orange" , "red" , "blue"]


    tosh = turtle.Turtle()
    # tosh.pencolor("red")
    # tosh.pensize(5)
    tosh.pensize(pensz)

    func10("'Up' - go forward" , 450, 300)
    func10("'Down' - delete" , 450, 275)
    func10("'Right' - turn right" , 450, 250)
    func10("'Left' - turn left" , 450, 225)
    func10("'Space' - carry the pen and down" , 450, 200)
    func10("'a' - making bigger" , 450, 175)
    func10("'s' - making smaller" , 450, 150)
    func10("'d' - change the color" , 450, 125)
    

    wn.onkey(func1, "Up")
    wn.onkey(func2, "Left")
    wn.onkey(func3, "Right")
    wn.onkey(func4, "q")
    wn.onkey(func5, "a")
    wn.onkey(func6, "s")
    wn.onkey(func7, "space")
    wn.onkey(func8, "Down")
    wn.onkey(func9, "d")


    wn.listen()
    wn.mainloop()

main()





#  _____________________________________________________________________________________________________
# list() >>> []
# tuple() >>> ()
# dict() >>> {"one":1 ,}
# set()  >>> {1,2,3}
# frozenset() >>> {1,2,3,}
# range() >>> 3 ... 8

# dataType >> int , float , str , bool : (complex)
# dataStructure >> list , tuple , dict , set , frozenset


# s = 10
# s %= 4
# print(s)
# # print("s" in s)


# operatorlar
# "s" in s
# "s" not s 


# is operatori
# x = 2
# y = 2
# print(x is y)
# print(x is not y)


# if 5 * 3 / 2 == 7.5:
#     print("yes") 


# user = input()
# if user == "1" :
#     print("windows")
# elif user == "2":
#     print("Linux")
# elif user == "3":
#     print("MacOS")
# elif user == "4":
#     print("Symbion OS")
# else:
#     print("try again")


# for i in range(0,19,2):
#     print(i , end='')
# else: 
#     print("\n finished")

# print()
# type()
# dir()

# arr = [1,2,3,4,5]
# for x in arr:
#     pass # will do nothing\


arr = []
for i in range(10):
    arr.append(i)
print(arr)