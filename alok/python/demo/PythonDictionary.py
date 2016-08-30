'''
Created on Aug 28, 2016

@author: alok
'''
import time
import calendar
'''
syntax- {'nanme':'alok','Age':7}
'''
dict = {'Name': 'Zara', 'Age': 7,'Class': 'First','Name': 'ajay'} #when duplicate entry of any key , then last assignment of key wins

dict['Age']=8 # update the value of Age Key

print ("dict['Name']: ", dict['Name'])#print the value of name key
print ("dict['Age']: ", dict['Age'])# print the value of Age key
print ("dict['Class']: ", dict['Class'])#print the value of Class key
del dict['Class']# delete class key as well as its value
print("Data type= ",type(dict['Name'])) # print the data type of  Name key
print("updated dic=" ,dict)# print update dictionary

#ticks=time.time();
ticks= time.asctime(time.localtime(time.time()))


print("current time=", ticks)

cal= calendar.isleap(2016)

print("calendar=",cal)


