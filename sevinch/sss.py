# sariq dev 2-dars 
# print(2+4*2)
# print('Assalomu aleykum')
# # print(19/5)
# # print(2f4f**4)

# # 3-dars:
# print(5**4)
# print(22%4)

# a=125
# s=a**2
# p=4*a
# print(s, p)

# r=12
# pi=3.14
# s=pi*r**2 
# print(s)

# import math 
# a=6
# b=7
# c=math.sqrt(a**2+b**2)
# print(c)

# 4-dars o'zgaruvchilar
# a="Hello world!"
# print(a)

# xabar="Ertaga dars yo'q"
# print(xabar)

# class="Bugun sana 20-mart"
# print(class) class deb o'zgaruvchi qo'yib bo'maydi

# radius=5
# pi=3.14159
# aylana_yuzi=pi*radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi= ", aylana_yuzi)

# 5-dars srting
# kocha='buyuk ipak yoli '
# mahalla='Amir Temur '
# tuman='Samarqand'
# viloyat='Samarqand'
# print(f" {kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# kocha=input("Kocha nomini kirit ")
# mahalla=input("Mahalla nomini kirit ")
# tuman=input("Tuman nomini kirit ")
# viloyat=input("Viloyat nomini kirit ")
# print(f" {kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# kocha='buyuk ipak yoli '
# mahalla='Amir Temur '
# tuman='Samarqand'
# viloyat='Samarqand'
# manzil=(f" {kocha.title()} kochasi , {mahalla.upper()} mahallasi, {tuman.lower()} tumani, {viloyat.capitalize() } viloyati")
# print(manzil)

# 6-dars sonlar
# a=int(input("Son kirit "))
# print(a**2, a**3)

# age=int(input("Yoshingni kirit "))
# year=2024-age
# print( year,"-yilda tug'ilgansan")

# a=int(input("1-sonni kirt "))
# b=int(input("2-sonni kirit "))
# c=a+b
# d=a-b
# e=a*b
# f=a/b
# print(f" Yig'indisi {c}, Ayirmasi {d}, K'paytmasi {e}, Bo'linmasi {f}")


# 7-dars list
# ismlar=['Amira', 'Aziza', 'Guli']
# print('Salom', ismlar[0], 'yaxshimisan')
# print(ismlar[1],"bugun darsga kelmadi")
# print("Uning ismi:" ,ismlar[2])

# sonlar=[12, -54, 14.4, 78, 45,0.24]
# print(sonlar[2]+sonlar[5])
# sonlar[3]=5
# print(sonlar)

# t_shaxslar=["Imom Buxoriy", "Ibn Sino"]
# z_shaxslar=["Ilon Musk", "May Musk"]
# a=t_shaxslar.pop(0)
# b=z_shaxslar.pop(1)
# print(f"Men tarixiy shaxslardan {a} bilan va zamonaviy shaxslaran {b} bilan suhbat qilishni istar edim")

# friends=[]
# friends.append("Aziza")
# friends.append("Amira")
# friends.append("Asal")
# friends.append("Guli")
# print(friends)

# friends.remove("Aziza")
# print(friends)
# friends.insert(0,"Aziza")
# friends.insert(2,"Umida")
# friends.insert(5,"Muxlisa")
# print(friends)

# mehmonlar=[]
# a=friends.pop(2)
# b=friends.pop(0)
# mehmonlar.append(a)
# mehmonlar.append(b)
# print(mehmonlar)

# 8-dars ro'yxatlar bilan ishlash
# davlatlar=['Korea', 'USA', 'Russia', 'Turkey']
# print(len(davlatlar))

# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar) 
# davlatlar.reverse()
# print(davlatlar)

# list=[]
# for i in range(120,1200):
#     list.append(i)
# a=max(list)
# b=min(list)
# c=a-b
# print(a, b, 'ayirmasi: ', c)

# list=[]
# for i in range(120,1200,2):
#     list.append(i)
# print(list)
# s=list=[]
# sum=0
# for i in range(120,1200):
#     sum+=i
# print(sum)

# print(len(list))
# list=[]
# for i in range(120,1200):
#     list.append(i) 
# print(len(list)) 1080
# print(list[0:20])
# print(list[int(1080/2)-10:int(1080/2)+10])
# print(list[-20:-1])

# taomlar=['lagmon', 'choy']
# nonushta=taomlar
# del taomlar[0]
# taomlar.append('tuxum')
# taomlar.append("saryog'")
# print(nonushta)
# print(taomlar)

# nonushta=('choy','tuxum','saryog')
# nonushta[0]='aaa' tuple ni o'zgartirib bo'maydi
# print(nonushta)

# 9-dars: for
# list=['ali','asal','salim','salima','sobir']
# for i in list:
#     print('Salom', i)

# for i in range(11,100,2):
#     print(i**3)

# kinolar=[]
# for i in range(5):
#     a=input("Kino nomi ")
#     kinolar.append(a)
# print(kinolar)

# a=int(input("Nechta odam bilan suhbatlashding "))
# list=[]
# for i in range(a):
#     list.append(input(f"{i+1}-suhbat qilgan odamingiz kim edi: "))
# print(list)
          
# 10-dars
# cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for i in cars:
#     if i=='gm':
#         print('gm'.upper())
#     else:
#         print(i.capitaliza())
   
# cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for i in cars:
#     if i!='gm':
#         print(i.capitalize())
#     else:
#         print(i.upper())

# login=input('Ism kirit ')
# if login=='admin':
#     print("Xush kelibsiz, Admin.Foydalanuvchilar ro'yxatini ko'rasizmi?" )  
# else:
#     print(f"Xush kelibsiz , {login}") 

# a=int(input("1-sonni kirit  "))
# b=int(input("2-sonni kirit  "))
# if a==b:
#     print('Sonlar teng')
# else:
#     print('Sonlar teng emas')

# son=int(input('Son kirit '))
# if son>=0:
#     print('Son musbat')
# else:
#     print('Son manfiy')

# import math
# son=int(input('Son kirit '))
# if son>0:
#     print(math.sqrt(son))
# else:
#     print('Musbat son kirit')

# 11-dars
# a=int(input('Juft on kirit '))
# if a%2==0:
#     print('Rahmat')
# else:
#     print('Juft son emas')

# age=int(input('Yoshingni kirit '))
# if age<=4 or age>=60:
#     print('Sizga bepul')
# elif age<18:
#     print('Chipta narxi 10ming som')
# else:
#     print('Chipta narxi 20ming som')

# a=int(input("1-sonni kirit "))
# b=int(input("2-sonni kirit "))
# if a==b:
#     print(f"{a}={b}")
# elif a<b:
#     print(f"{a}<{b}")
# elif a>b:
#     print(f"{a}>{b}")

# mahsulotlar=['kartoshka','uzum','pomidor','sabzi','bodring','olma','banan','apelsin']
# s=[]
# for i in range(5):
#     s.append((input(f"Savatga {i+1}- mahsulotni qo'sh  ")))
# for i in s:
#     if i in mahsulotlar:
#         print(f"Do'konda {i} bor")
#     else:
#         pri print("Bunaqa login mavjud,yangisini top")nt(f"Do'konda {i} yo'q ")

# foydalanuvchilar=['asa','ali','fantonx','sardor','komila','lobar','santo','bb77']
# a=input("Foydalanuvchi qo'sh ")
# if a in foydalanuvchilar:
#     print("Login band")
# else:
#     print("Xush kelibsan")

# a=int(input("Sonni kirit "))
# for i in range(2,10):
#     if a%i==0:
#         print(f"{a} soni {i} ga qoldiqsiz bo'linadi")

# 14-dars:
# otam={
#     'ismi':'Alisher',
#     'yoshi':'43',
#     'address':'Amir Temur 101/45'
# }
# onam={
#     'ismi':'Umida',
#     'yoshi':'42',
#     'address':'Amir Temur 101/45'
# }
# print(f" Otamning ismi {otam['ismi']}, yoshi {otam['yoshi']}da,manzil: {otam['address']}")
# print(f" Obamning ismi {onam['ismi']}, yoshi {onam['yoshi']}da,manzil: {onam['address']}")

# ali={
#     'ismi':'Ali',
#     'taomi':'osh'
# }
# lola={
#     'ismi':'Lola',
#     'taomi':'pizza'
# }
# Asal={
#     'ismi':'asal',
#     'taomi':"Lag'mon"
# }
# print(f"{ali['ismi']}ning sevimli taomi {ali['taomi']}")
# print(f"{lola['ismi']} {lola['taomi']} ni yoqtiradi")
# print(f"{Asal['taomi']} {Asal['ismi']}ning yoqtirgan taomi")

# python={
#     'int':'Butun son',
#     'float':'Haqiqiy son',
#     'input':'string formatda',
#     'if':'Shart operatori',
#     'while':'Shart operatori, cheksiz',
#     'boolen':'True va false',
#     'loop':'Sikl',
#     'list':'royxat',
#     'dict':"lug'at"
# }
# a=input("So'zni kirit ")
# print(python.get(a))

# python={
#      'int':'Butun son',
#      'float':'Haqiqiy son',
#      'input':'string formatda',
#      'if':'Shart operatori',
#      'while':'Shart operatori, cheksiz',
#      'boolen':'True va false',
#      'loop':'Sikl',
#      'list':'royxat',
#      'dict':"lug'at"
# }
# a=input("So'zni kirit ") 
# b=python.get(a)
# if b==None:
#      print("Bunday so'z mavjud emas")  
# else:
#      print(python.get(a))

# 15-dars:
# python={
#       'int':'Butun son',
#      'float':'Haqiqiy son',
#      'input':'string formatdagi ma'lumot',
#      'if':'Shart operatori',
#      'while':'Shart operatori, cheksiz davom eta oladi',
#       'boolen':'True va False',
#       'loop':'Sikl',
#       'list':'royxat',
#       'dict':"lug'at"
# }
# for i in sorted(python):
#     print(i,'-', python[i])

# davlatlar={
#     'Uzbekistan':'Tashkent',
#     'USA':'Washington dc',
#     'UK':'London',
#     'Tajikistan':'Dushanbe',
#     'Russia':'Moscow',
#     'Belorussia':'Minsk'
# }
# a=input('Qaysi davlat poytaxt kerak ')
# b=davlatlar.get(a)
# if b==None:
#     print("Bizda bu davlat ma'lumoti yo'q")
# else:
#     print(b)

# print("Davlatlar: ")
# for i in sorted(davlatlar.keys()):
#     print(i)
# print('Poytaxtlar:')
# for i in sorted(davlatlar.values()):
#     print(i)

# menyu={
#     'osh':30000,
#     'shorva':15000,
#     'lagmon':20000,
#     'manti':25000,
#     'un oshi':30000,
#     'barak':40000
# }
# list=[]
# for i in range(3):
#     list.append(input(f"{i+1} - taomni kirit "))
# for j in list:
#     if j in menyu:
#         print(f"{menyu[j]} so'm ")
#     else:
#         print("Menyuda bunaqa ovqat yo'q") 

# 16-dars:
# a_navoiy={
#     'ismi':'Alisher Navoiy',
#     'birth':1441,
#     'death':1501,
#     'place':'Hirot',
#     'asarlari':['Xamsa','Xazoin al-maoni','Devoni Foniy', 'Majolis al-nafois']
# }
# bobur={
#     'ismi':"Zahiriddin Muhammad Bobur",
#     'birth':1483,
#     'death':1530,
#     'place':'Andijon',
#     'asarlari':['Boburnoma','Mubayyin','Xati Boburiy']
# }
# print("Navoiy asarlari:")
# for i in a_navoiy['asarlari']:
#     print(i)
# print("Bobur asarlari:")
# for i in bobur['asarlari']:
#     print(i)

# print(f"{a_navoiy['ismi']} {a_navoiy['birth'] }-yilda {a_navoiy['place']}da tug'ilgan")
# print(f"{bobur['ismi']} {bobur['birth'] }-yilda {bobur['place']}da tug'ilgan")

# amira={
#     'ismi':'Amira',
#     'kinolar':['Sexirli qalpoqcha','Tilim qursin']
# }
# shaxnoza={
#     'ismi':'Shaxnoza',
#     'kinolar':['Mahallada duv-duv gap','Shaytanat','Terminator']
# }
# print(f"{amira['ismi']}ning sevimli kinolari:")
# for i in amira['kinolar']:
#     print(i)

# print(f"{shaxnoza['ismi']}ning sevimli kinolari:")
# for i in shaxnoza['kinolar']:
#     print(i)

# davlatlar={
#     "ozbekiston":{
#         'poytaxti':'Toshkent',
#         'hududi':'448.9ming kv.km',
#         'aholisi':36799800
#     },
#     "AQSH":{
#         'poytaxti':'Washington',
#         'hududi':'9834000 kv km',
#         'aholisi':336000000
#     },
#     'yaponiya':{
#         'poytaxti':'Tokio',
#         'hududi':'337973 kv km',
#         'aholisi':125416877
#     }
# }
# a=input('Davlat nomini kirit ')
# if a in davlatlar:
#     kalit=a
#     print(f"{davlatlar[kalit]}")
# else:
#     print("Bu davlat haqida ma'lumot yo'q")

# print("O'zbekiston")
# print(f"poytaxti: {davlatlar['ozbekiston']['poytaxti']}",
#       f"hududi:{davlatlar['ozbekiston']['hududi']} "
#       f"aholisi: {davlatlar['ozbekiston']['aholisi']}")

# print("AQSH")
# print(f"poytaxti: {davlatlar['AQSH']['poytaxti']}",
#       f"hududi:{davlatlar['AQSH']['hududi']} "
#       f"aholisi: {davlatlar['AQSH']['aholisi']}")
# print("Yaponiya")
# print(f"poytaxti: {davlatlar['yaponiya']['poytaxti']}",
#       f"hududi:{davlatlar['yaponiya']['hududi']} "
#       f"aholisi: {davlatlar['yaponiya']['aholisi']}")

# 17-dars:
# a="Yaxshi ko'rgan kitoningni kirit "
# while True:
#     b=input(a)
#     if b=='stop':
#         break

# a="Yoshingni kirit "
# while True:
#     b=input(a)
#     if b=='exit':
#         break
#     c=int(b)
#     if c<7:
#         print("Narxi 2000so'm")
#     elif c>=7 and c<18:
#         print("Narxi 3000so'm")
#     elif c>=18 and c<=65:
#         print("Narxi 10000so'm")
#     else:
#         print('Bepul')
    
# 18-dars:
# list=[]
# while True:
#     a=input("Mahsulot qo'shing ")
#     list.append(a)
#     if a=='stop':
#         break
# print(list)

# e_bozor={}
# while True:
#     a=input('Mahsulot nomini kirit ')
#     b=int(input(f"{a}  narxini kirit "))
#     e_bozor[a]=b
#     c=input('Davom etamizmi ')
#     if c=='yoq':
#         break
# print(e_bozor)

# 17-dars:
# def age():
#     name=input('Ismingni kirit ')
#     yosh=int(input('Yoshingni kirit '))
#     a=2024-yosh
#     print(f"{a}-yilda tug'ilgansan")
# age()

# def son():
#     a=int(input('Son kirit '))
#     b=a**2
#     c=a**3
#     print(f"sonning kvadrati {b}, sonning kubi {c}") 
# son()

# def son():
#     a=int(input('Son kirit '))
#     if a%2==0:
#         print('Son juft')
#     else:
#         print('Son toq')
# son()

# def taq():
#     a=int(input('1-sonni kirit '))
#     b=int(input('2-sonni kirit '))
#     if a>b:
#         print(f"{a} katta {b}dan")
#     elif a<b:
#         print(f"{b} katta {a}dan" )
#     else:
#         print('Sonlar teng ')
# taq()

# def daraja():
#     x, y=map(int,input('Sonlarni kirit ') .split())
#     print(x**y)
# daraja()

# def dar(x,y=2):
#     print(x**y)
# dar(4,2)
# sariq dev funksiya bo'yicha amaliyot yechimlari tepadagi 17-dars
