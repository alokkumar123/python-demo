'''
Created on Aug 27, 2016

@author: alok
'''

var =4+5
print("Hello var =", var)


def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32
print ("temp ", KelvinToFahrenheit(273))