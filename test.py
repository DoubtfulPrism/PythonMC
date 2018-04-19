#print("First Program")

#Replaced = ('Audit'.replace('A','O'))

#print(Replaced)
#
# def currencyConverter(rate,euros):
#     dollars = euros*rate
#     return dollars
#
# print(currencyConverter(1.45,1000))
#
# dict = {"name":"Audit","profession":"Instructor"}
# print (dict["name"])
#
# a = list(dict.values())
# print (a)

# v = 3
# if v<3:
#     print("less")
# elif v ==3:
#     print("equal")
# else:
#     print("greater")
# a=2
# print("positive" if a>0 else "negative")
#
# emails=['me@gmail.com','you@hotmail.com','they@gmail.com']
# for email in emails:
#     if 'gmail' in email:
#         print(email)

# planet=input("what planet are you from?")
# print(planet)
#
# def currencyConverter(rate,euros):
#     dollars = euros*rate
#     return dollars
# r=input("enter rate: ")
# e=input("enter euros: ")
# print(currencyConverter(float(r),float(e))
#

# names=['james','john','jake']
# emailDomains=['gmail','hotmail','yahoo']
#
# for i,j in zip(names,emailDomains):
#     print(i,j)

# file=open("example.txt",'r')
# content=file.read()
# print(content)
#
# file.seek(0)
# content=file.readlines()
# print(content)
#
# file.seek(0)
# content=[i.rstrip("\n")for i in content]
# print(content)
# file.close()
#
# file=open("example2.txt",'w')
# file.write("line1\n")
# file.close()
# file=open("example2.txt",'a')
# file.write("line2")
# file.close()
# l=["line1\n","line2\n","line3\n"]
# file=open("example2.txt",'w')
# for item in l:
#     file.write(item)
# file.close()

# with open("example3.txt",'a+') as file:
#     file.seek(0)
#     content=file.read()
#     file.write("\nline6")
#
# print(content)
# import os
#
# print(os.listdir())

import datetime
# now=datetime.datetime.now()
#
# yesterday=datetime.datetime(2018,4,18,0,0,0,0)
#
# print(now-yesterday)
#
# filename=datetime.datetime.now()
#
# def createFile():
#     with open(filename.strftime("%B-%Y-%d")+".txt", 'w') as file:
#         file.write("")
#
# createFile()
#
# after=now+datetime.timedelta(days=2)
# print(after)

import time
lst=[]
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1)

for i in lst:
    print(i)