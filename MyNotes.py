
# printing 

print ("Hello, World!")


# Indentions
if 5 > 2: 
    print ("Five is greater than two!")

if 5 > 2: 
    print("Five is greater than two!")



# Variable declaration 
x = 5
y = "Hello, World!"


'''
Comments Example #
'''




# Variable declaration with print declare

x = 5           # int 
y = "john"      # str 

print(x)
print(y)



# Data type specification 

x = str(3) # x= '3'
y = int(3) # y = 3
z = float(3) # z = 3.0



# Getting the type of data 
x= 5
y = "John"

print(type(x))
print(type(y))





# Variable Names 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"




#MultiWord Variable Names 


'''Camel case '''

myVariableName = "John" 
MyVariableName = "John"
my_variable_name = "John"



#Printing multiple Values at once 

x,y,z = "Orange", "Banana","Cherry"

print(x)
print(y)
print(z)


# One value to multiple variables 

x= y = z = "orange"
print(x)
print(y)
print(z)





# Unpacking collection "list"

fruits = ["apple","banana","cherry"]
x,y,z = fruits 

print (x)
print (y)
print (z)


#Output Variables 

x = "Python is awesome"
print(x)

x = "Python "
y = "is"
z = " awesome"

print(x+y+z)

x = 5
y = 10 
print(x+y)

x = "John"
y = "20"

print(x,y)




# Global Variables

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 



#Global Keyword

def myfunc(): 
    global x
    x = "fantastic"

myfunc()

print("python is " + x )
