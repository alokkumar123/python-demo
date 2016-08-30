'''
Created on Aug 30, 2016

@author: alok
'''

import os
fo = open("foo.txt", "w")
print("fo=", fo)

var ="hello python\nhi bro\nlets have party"
fo.write(var)

print("file=", fo)

#f=os.rename("foo.txt", "foo1.txt")
#print("file1=", f)

fo=open("foo.txt", "r")

len = len(var)
str = fo.read(len);
print ("Read file : ", str)




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