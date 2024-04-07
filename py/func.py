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
#     a=int(input('Uchburchak tomonini kirit '))
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
# def child(n):
#     if n==1:
#         return 1
#     else:
#         return n*child(n-1)
# print(child(10)) 


# // belgisi bo'lib butun qismini oladi
# def digitcountsum():
#     num=int(input('son kirit '))
#     count=0
#     while num>0:
#         num//=10
#         count+=1
#     print(count)
# digitcountsum()    

# def digitcountsum():
#     num=int(input('son kirit '))
#     sum=0
#     count=0
#     while num>0:
#         a=num%10
#         num//=10
#         count+=1
#         sum+=a
#     print(count, sum)
# digitcountsum()

# #   a=global funksiya ichidagi esa lokal
# a=3
# def change():
#     global a
#     a=20
# change()
# print(a)     
#print da endi 20 chiqadi

# nonlocal o'zidan oldingi funksiyadagi qiymatni oladi, funksiyani ichida funksiya bo'lgan holatlarda:
# a=3
# def change():
#     a=14
#     print(a)
#     def inner():
#         nonlocal a
#         print(a)
#     inner()
# change()
# print(a)

# raqamlarni teskari tartibda chiqarish:
# def invertdigit():
#     num=input('Son kirit ')
#     print(num[::-1])
# invertdigit()

# def swap(a,b):
#     a,b=b,a
#     print(a,b)
# swap(3,8)

# def ishora():
#     a=int(input('son kirit '))
#     if a>0:
#         print('son musbat')
#     elif a<0:
#         print('son manfiy')
#     else:
#         print('son nolga teng')
# ishora()


# def sumrange(a,b):
#     if a<b:
#         sum=0
#         for i in range(a,b):
#             sum+=i
#     elif a>b:
#         print(0)
#     else:
#         print('sonlar teng')
#     print(sum)
# sumrange(2,12) 

# def quarter():
#     x,y=map(int,input('sonlarni kirit ') .split())
#     if x>0 and y>0:
#         print('1-chorak')
#     elif x>0 and y<0:
#         print('4-chorak')
#     elif x<0 and y>0:
#         print('2-chorak')
#     else:
#         print('3-chorak')
# quarter()

# def even():
#     k=int(input('son kirit '))
#     if k%2==0:
#         print('juft son')
#     else:
#         print('toq son')
# even()

# def issquare():
#     k=float(input('musbat son kirit '))
#     a=k**0.5
#     if a**2==k:
#         print(a)
#     else:
#         print('false')
# issquare()

# import math
# def ispower5():
#     k=int(input('son kirit '))
#     a=math.log(k,5)
#     if 5**a==k:
#         print(a, 'true')
#     else:
#         print('false')
# ispower5()

# import math
# def powern(n,k):
#     a=math.log(k,n)
#     if n**a==k:
#         print('true')
#     else:
#         print('false')
# powern(2,9)

# def digitcount():
#     num=int(input('son kirit '))
#     count=0
#     while num>0:
#         a=num%10
#         num//=10
#         count+=1
#     print(count)
# digitcount()

# def degtorad():
#     a=int(input('son kirit '))
#     pi=3.14
#     k=a*pi/180
#     print(k)
# degtorad()

# def radtodeg():
#     a=float(input('son kirit '))
#     pi=3.14
#     k=a*180/pi
#     return k
# print(radtodeg())

# import math
# def fact(n):
#     a=math.factorial(n)
#     return a
# print(fact(5))
