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

#import datetime
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
#
# import time
# lst=[]
# for i in range(5):
#     lst.append(datetime.datetime.now())
#     time.sleep(1)
#
# for i in lst:
#     print(i)
#
# import pandas, numpy, xlrd, geopy
# from geopy.geocoders import Nominatim
# nom=Nominatim()
#
# df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["price","age","value"],index=["first","second"])
# print(df1)
#
# df2=pandas.DataFrame([{"name":"john"},{"name":"jake"}])
# print(df2)
#
# print(df1.mean())
# print(df1.price.mean())
#
# df1=pandas.read_csv("supermarkets.csv")
# print(df1.set_index("ID"))

# df2=pandas.read_excel("supermarkets.xlsx",sheet_name=0)
# print(df2.set_index("ID"))
#
# df3=pandas.read_csv("https://pythonhow.com/supermarkets.csv")
# print(df3)

# df4=pandas.read_json("https://pythonhow.com/supermarkets.json")
# df4=df4.set_index("ID")
# #print(df4)

#print(df4.iloc[1:3,1:3])

#print(df4.ix[3,4])

#print(df4.drop("City",1))

#df4=df4.drop(df4.columns[0:3],1)
#
# df4["continent"]=df4.shape[0]*["North America"]
# df4["continent"]=df4["Country"]+","+"North America"

#g=nom.geocode("3995 23rd St, San Francisco, CA 94114")

# print(g.latitude)
# print(g)
#
# df4["Address"]=df4["Address"]+", "+df4["City"]+", "+df4["State"]+", "+df4["Country"]
# df4["Coordinates"]=df4["Address"].apply(nom.geocode)
# df4["Latitude"]=df4["Coordinates"].apply(lambda x:x.latitude if x!= None else None)
# df4["Longitude"]=df4["Coordinates"].apply(lambda x:x.longitude if x!= None else None)
# #print(df4.Coordinates[1])
# print(df4)

#import numpy
# n=numpy.arange(27)
# r=n.reshape(3,9)
# e=n.reshape(3,3,3)
# print(e)
# m=numpy.asarray([[123,12,123,12,33],[],[]])
# print(m)

# import cv2, numpy
#
# im_g=cv2.imread("smallgray.png",0)

# print(im_g)
#
# cv2.imwrite("newsmallgray.png",im_g)

#print(im_g[0:2,2:4])

# for i in im_g.T:
#     print(i)

# for i in im_g.flat:
#     print(i)
# ims=numpy.hstack((im_g,im_g))
# print(ims)
#
# ims=numpy.vstack((im_g,im_g))
# print(ims)
#
# lst=numpy.hsplit(ims,5)
# print(lst)
#
# lst=numpy.vsplit(ims,3)
# print(lst)

