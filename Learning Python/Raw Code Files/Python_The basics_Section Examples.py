# THE BASICS OF PYTHON - SECTION EXAMPLES

#1. VARIABLES AND CONSTANTS
#this is variable:
name= 'lorena'
print(name)
#this is a constant:
salary = 2000
print(salary)

#2.FORMAT FUNCTION
product1 = 'milk'
product2 = 'cereals'
header = "Results of the product 1 '{0}' and the product '{1}':"
print(header.format(product1, product2))
print("The prize of the first product is smaller than the prize of the second product")

#3. INPUT FUNCTION
#let's check an example
print("What is your name?")
name = input()
print("Nice to meet you!")

#4. CONDIDITIONS
#4.1 SIMPLE CONDITIONS
#example of a simple condition
print("Please guess a number between 1 and 10: ")    
guess= int(input())
if guess < 5:
    print("Please guess higher")
    guess= int(input())    
if guess == 5:
    print("Well done, you guessed it")
else:
    print("Sorry, you have not guessed correctly")

#4.2 NESTED CONDITIONS
#example of a nested condition
note1 = int(input("Insert the first note: "))
note2 = int(input("Insert the second note: "))
note3 = int(input("Insert the third note: "))
average = (note1+note2+note3)/3
if average == 9 or average ==10:
    print("Outstanding")
elif average == 5:
    print("Approved")
elif average == 6:
    print("Good")
elif average == 7 or average ==8:
    print("Remarkable")
else:
    print("You did not approve the exame")

#5. LOOPS IN PYTHON
#5.1 WHILE LOOP
available_exists = ("east", "north east", "south")
chosen_exist= 'east'
while chosen_exist not in available_exists:
    chosen_exist = input("Please chose a direction: ")
    if chosen_exist == 'quit':
        print("Game over")
        break
else:
    print("are not you glad you got out of there!")

#5.2 FOR LOOP
number= '9,223,372,036,854,775,807'
clearedNumber= ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print("The before >>" + clearedNumber + "<<interaction number " + str(i))
        #clearedNumber= clearedNumber + number[i] 
        #clearedNumber+= number[i]
        #las dos anteriores frases dicen lo mismo
        clearedNumber= number[i]
        print("The after >>" + clearedNumber + "<<")

newNumber= int(clearedNumber)
print("The number is {}".format(newNumber))

#5.3 BREAK, CONTINUE AND PASS
#Example with BREAK
meal= ("egg", "bacon", "tomato", "sausages")
for item in meal:
    if item == 'bacon':
        nasty_food = item
        break
else:
    nasty_food = ''
    print("I will have a dish of that, please")
if nasty_food :
    print("I Cannot have anything withou bacon on it")

#Example with CONTINUE
shopping_list= ("milk", "pasta", "eggs", "spam", "bread", "rice")
for item in shopping_list:
    if item == 'spam':
        print("I am ignoring " + item)
        continue
    print("Buy " + item)

#Example with PASS
shopping_list= ("milk", "pasta", "eggs", "spam", "bread", "rice")
for item in shopping_list:
    if item == 'spam':
        print("I am ignoring " + item)
        pass
    print("Buy " + item)