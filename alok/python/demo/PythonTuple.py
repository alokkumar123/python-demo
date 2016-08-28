'''
Created on Aug 28, 2016

@author: alok
'''
'''
Tuple tutorial

syntax:- (1,2)
Tuple can not be updated 

'''
tuple=(1,3,"alok","super")

print(tuple) # print all the elements of tuple
print(tuple[2]) # print 2nd index value of the tuple 
print(tuple[1:]) # print all the value of tuple from index 1st to end
print(tuple[2:4]) # print value form 2nd index to 4rth position of tuple

#tuple[2]="kumar" # here it will show error because tuple can not be updated 

print("updated tuple=",tuple)
