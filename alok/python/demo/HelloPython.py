'''
Created on Aug 27, 2016

@author: alok
'''

from pip._vendor.distlib.compat import raw_input
#from test.test_decimal import file

#var =4+5
#print("Hello var =", var)


import math

#content = dir(__doc__)

#print (content)

#a= raw_input("enter value=")
#print("a=", a)

#b = input("enter input=")
#print("b=", b)

fo = open("foo.txt", "w")
print("fo=", fo)

var ="hello python"
fo.write(var)

print("file=", fo)

f=fo.rename("foo.txt", "foo1.txt")
print("file1=", f)

fo=open("foo.txt", "r")

len = len(var)
str = fo.read(len);
print ("Read String is : ", str)




# Close opend file
fo.close()

'''fo= open("file.txt", "r+")

str= fo.read(10)
fo.close()

print ("File read =", str)
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
#print ("Softspace flag : ", fo.softspace)'''