# def powera3(a):
#     print(a**3)
# powera3(5)

# def power234():
#     a=float(input('Son kirit '))
#     print(a**2, a**3, a**4)
# power234()
# import math
# def mean(a,b):
#     arif=(a+b)/2
#     g=math.sqrt(a*b)
#     print(f" o'rta arifmetigi {arif}, geometrigi {g}")
# mean(24,41)

# import math
# def triangle():
#     a=int(input('Uchbuechak tomonini kirit '))
#     h=math.sqrt(a**2+(a/2)**2)
#     s=h*a/2
#     print(s)
# triangle()

# ism='zafar'
# def name():
#     ism='ali'
#     print(ism)
# print(ism)
# name()

# def full():
#     print('Hello')
#     def name():
#         print('Zafar')
#     name()
# full() 

# def chine():
#     print('Hello')
#     def byd():
#         print("Mashinalar")
#     byd()
# chine() 

# def add():
#     a=4
#     b=5
#     print(a+b)
# def a():
#     add()
#     print("a klass haqida ma'lumot")

# def b():
#     add()
#     print("b klass haqida ma'lumot")
# a()
# b() 

# rekursiya - funksiyani o'zini ichida o'zini chaqirish:
def child(n):
    if n==1:
        return 1
    else:
        return n*child(n-1)
print(child(10)) 

