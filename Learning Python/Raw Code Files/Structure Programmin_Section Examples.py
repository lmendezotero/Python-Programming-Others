# STRUCTURE PROGRAMMING - SECTION EXAMPLES

#1. FUNCTIONS
# 1.1 CREATE A FUNCTION
#let's check an example of program with simple functions
def presentation():
    print('Program to do arithmetic operations of two values')
    print('************************************')
def enterData ():
    global valor1
    global valor2
    valor1 = int(input("Enter the value 1:"))
    valor2 = int(input("Enter the value 2:"))
def suma ():
    suma = valor1 + valor2
    print("The result of the sum is: ", suma)
def subtraction ():
    resta = valor1 - valor2
    print("The result of the subtraction is: ", resta)
def ending():
    print('************************************')
    print('Thanks for using the program')
#Call the functions
presentation()
enterData()
suma()
subtraction()
ending()

# 1.2 FUNCTIONS WITH PARAMETERS
#Let's check an example 
def show_message(mensaje):
    print("*****************************")
    print(mensaje)
    print("*****************************")
def upload_sum():
    valor1 = int(input("Enter the first value:"))
    valor2 = int(input("Enter the second value:"))
    suma = valor1 + valor2
    print("The value of the sum is: ", suma)
show_message("Calculation of the sum of the values")
upload_sum()
#The parameter is "message"

# 1.3 FUNCTIONS THAT RETURN DATA
#Let's check an example
def return_surface(side):
    surface = side*side
    return surface  
va = int(input("Enter the value of the side of the square: "))
superficie = return_surface (va) 
print("The surface of the square is: ", superficie)

# 1.4 DEFAULT PARAMETERS
#Let's check an example
def greet(name, message = "Hello"):
    print(message, name)
greet("Lorena Mendez", "this is the change")
#In this case I am only sending values ​​to a parameter (name)
#since the parameter "message" already has the values ​​established when defining the function

# 1.5 ARBITRARY PARAMETERS
#Let's check an example
def sumar (v1, v2, *lista):
    suma = v1 + v2
    for x in range(len(lista)):
        suma = suma + lista[x]    
    return suma
print("******Suma of 2 values*****")
print(sumar(4, 5))
print("******Suma of 5 values*****")
print(sumar(4,5,6,7,8))
print("******Suma of 8 values*****")
print(sumar(4,5,6,7,8,9,10,11))
#Important to specify the len () statement when working with tuples, otherwise we will encounter an error


#2. LISTS & TUPLES
# 2.1 TUPLE DATA
#Tuples Definition
print("a","b","c")
print(("a","b","c"))

#Let's check an example
def upload_date():
    dd = int(input("Enter the number of the day: "))
    mm = int(input("Enter the number of the month: "))
    aa = int(input("Enter the number of the year: "))
    tuple = (dd, mm, aa)
    return tuple
def print_date(date):
    print(date[0], date[1], date[2], sep = "/")
date = upload_date()
print_date(date)

# 2.2 LIST DATA
#Let's check an example
odd = [1, 2, 3, 5, 5]
even = [6, 7, 8, 9]
numbers = odd + even
numbers_in_order = sorted(numbers)
print(numbers_in_order)  
if numbers_in_order == sorted(numbers):
    print("These lists are equal")
else:
    print("These lists are not equal")

# 2.3 NESTED TUPLES AND LISTS
#Let's check an example
employee=["juan", 53, (25, 11, 1999)]
print(employee)
employee.append((1, 1, 2016))
print(employee)
student=("pedro",[7, 9])
print(student)
student[1].append(10)
print(student)

# 2.4 LOTS OF LISTS, TUPLES AND STRINGS
#Let's check an example with a program that extracts the remaining months from the list
def missing_months(number):
    months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
    return months [number :]
#main part
#return the missing months until the end of the year
print ("Print the missing months until the end of the year")
number = int(input("Insert the number of the month: "))
missingmonths = missing_months(number)
print(missingmonths)

# 2.5 NEGATIVE INDICES IN LISTS, TUPLES AND STRINGS
#Let's check an example
list1=[0,1,2,3,4,5,6]
print(list1[-1]) 
print(list1[-2])


#3. DICTIONARIES
#Let's check an example of a dictionary
bike = {"make": "Honda", "model": "250 dran", "colour": "red", "engine_size": 250}
print(bike["make"])
print(bike["engine_size"])

#Let's check another example of a dictionary
fruit = {"orange": "a sweet, organge, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "apple": "nice with juice",
         "lime": "a sour, green citrus fruit"}
print(fruit)
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key,"We do not have a " + dict_key)
    print(description)