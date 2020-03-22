
# OBJECT ORIENTED PROGRAMMING WITH PYTHON - SECTION EXAMPLES

#1. LOGIC BEHIND CLASSES
#Let's check an example of the Pet Class
class pet:
    #creation of attributes
    color = "brown"
    number_of_legs = 0
#create a method
def sleep (self):
    print('zzzzzzzzzzz')
#Build the objects
dog = pet()

#Let's check another example with the Student Class
class Student:
    #declare methods with parameters
    def declare (self, name, data):  
        self.name =name   
        self.puntuation = data 
    
    #declare methods of visualization and statistics
    def visualization (self):
        print("Name: ", self.name)
        print("Puntuation: ", self.puntuation) 
    
    def statistics (self):
        if self.puntuation <=4:
            print("Not Approved")
        elif self.puntuation >=5:
            print("Approved")
        elif self.puntuation >=8:
            print("Remarkable")
        else:
            print("Free")
#Build the objects
Student1 = Student()
Student1.declare("Lorena", 7)
Student1.visualization()
Student1.statistics()
Student2 = Student()
Student2.declare("Hugo", 6)
Student2.visualization()
Student2.statistics()

#2. CONSTRUCTOR METHOD OF A CLASS
#let's check an example of the __init__ method with the User Class
class User:
    def __init__ (self):
        self.user = ""
        self.revenues = 0  
    def intro (self):
        self.user = input("Name of the user: ")
        self.revenues = float(input("Anual income amount: ")) 
    def visualization (self):
        print("Name: ", self.user)
        print("Revenues: ", self.revenues)
    def taxation (self):
        if self.revenues >= 22000:
            print("You must pay taxes")
        else:
            print("You do not have to pay taxes")
User1 = User()
User1.intro()
User1.visualization()
User1.taxation()

# 3. CALL A METHOD FROM ANOTHER METHOD OF THE SAME CLASS
class Operation:   
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
    def sumar (self):
        suma = self.value1 + self.value2
        print("The result of the sum is: ", suma)
    def subtract (self):
        subtract = self.value1 - self.value2
        print("The result of the subtract is: ", subtract)
    def multiply (self):
        multi = self.value1 * self.value2
        print("La result of the multiply is: ", multi)
    def division (self):
        divi = self.value1 / self.value2
        print("The result of the division is: ", divi)
    def enter_values (self):
        self.value1 = int(input("Enter a value: "))
        self.value2 = int(input("Enter a value: "))
    def main(self):
        self.sumar()
        self.subtract()
        self.multiply()
        self.division()
#Build the objects
Operation1 = Operation()
Operation1.enter_values()
Operation1.main()

#4. COLLABORATION BETWEEN CLASSES
#let's check an example with the Client Class and Bank Class
#Methods of the Client class are referenced in the Bank class

#Build the Client Class
class Client:
    def __init__ (self, name):
        self.name = name
        self.amount = 0
    def deposit (self, amount):
        self.amount = self.amount + amount
    def extract (self, amount):
        self.amount = self.amount - amount
    def retunr_amount (self):
        return self.amount
    def print (self):
        print(self.name, "You has deposited the sum of: ", self.amount) 
#Build the Bank Class
class Bank:
    def __init__ (self):
        self.client1 = Client("Lorena")
        self.client2 = Client("Melvin")
        self.client3 = Client("Noel")
    def operate (self):
        self.client1.deposit (1000)
        self.client2.deposit (500)
        self.client3.deposit (250)
        self.client3.extract (120)
    def total_deposits (self):
        total= self.client1.retunr_amount() + self.client2.retunr_amount() + self.client3.retunr_amount() 
        print("The total amount of the bank is: ", total)
        self.client1.print()
        self.client2.print()
        self.client3.print()   
#Build the objects
Bank1 = Bank()
Bank1.operate()
Bank1.total_deposits()

#5. HERITAGE
class Operation:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.result = 0
    def upload(self):
        self.value1 = int(input('Enter the first value: '))
        self.value2 = int(input('Enter the second value: '))    
    def show_result(self):
        print(self. result)
class Suma(Operation):
    def operate (self):
        self.result = self.value1 + self.value2
class Subtract(Operation):
    def operate(self):
        self.result =  self.value1 - self.value2
#Build the Objects for the Suma Class
suma1 = Suma()
suma1.upload()
suma1.operate()
print('The result of the sum is: ')
suma1.show_result()
#Build the Objects for the Subtract Class
subtract1 = Subtract()
subtract1.upload()
subtract1.operate()
print('The result of the subtract is: ')
subtract1.show_result()

#6. CLASSES VARIABLES
class Client:
    not_approved = [] #variable class in list form
    def __init__ (self, code, name):
        self.code = code
        self.name = name
    def print (self):
        print("Code: ", self.code)
        print("Name: ", self.name)
        self.is_unapproved()
    def is_unapproved(self):
        if self.code in Client.not_approved:  #Using the Class Variable, which is fed by the attribute "code"
            print("You are not approved")
        else:
            print("You are approved")
    def failed(self):
        Client.not_approved.append(self.code) 
#Build the objects
client1 = Client(1, "Lorena")
client2 = Client(2, "Tere")
client3 = Client(3, "Mila")
client4 = Client(4, "Manuel")
client3.failed()
client4.failed()
client1.print()
client2.print()
client3.print()
client4.print()

#7. STR METHOD: REDIFINITION OF METHODS
#Check an example of the STR method with the Family Class
class Family:
    def __init__ (self, father, mother, sons=[]):
        self.father = father
        self.mother = mother
        self.sons = sons
    def __str__ (self):
        string = self.father + "," + self.mother
        for son in self.sons:
            string = string + "," + son
        return string
#Building the objects
Family1 = Family("Manuel", "Teresa", ["Mila", "Lorena"])
Family2 = Family ("Manolo", "Gloria", ["Juan Antonio", "Laura"])
Family3 = Family("David", "Sonia")
print(Family1)
print(Family2)
print(Family3)

#8.SETTER AND GETTER
#Build the ComplexNumber class
class ComplexNumber:   
    #Attributes of the class
    RealPart = 0
    ImaginaryPart = 0 
   
    #Methods of the class
    #Constructor of the class
    def __init__(self, real, imaginary):
        self.RealPart = real
        self.ImaginaryPart = imaginary      
    
    #Method to print the Complex Number
    def printNumber(self):
        print(str(self.RealPart) + " + i* " + str(self.ImaginaryPart))    
#End of the ComplexNumber class

#Application of Setters and Getters in a class
    #Change the real part (setter)
    def change_RealPart(self, real):
        self.RealPart = real
    #Get the real part (getter)
    def get_RealPart(self):
        return self.RealPart
    #Change the imaginary part (setter)
    def change_ImaginaryPart(self, imaginary):
        self.ImaginaryPart = imaginary
    #Get the imaginary part (getter)
    def get_ImaginaryPart(self):
        return self.ImaginaryPart
#Build an object to access into a class
FirstNumber = ComplexNumber(12.0, 4.0)
print ("Official version of the complex number")
#Using a method associated with the object
FirstNumber.printNumber()
#Setter of the RealPart
print("modified complex number (change the value of the RealPart)")
FirstNumber.change_RealPart(25.0)
FirstNumber.printNumber()
#Setter of the ImaginaryPart
print("modified complex number (change the value of the ImaginaryPart)")
FirstNumber.change_ImaginaryPart(7.0)
FirstNumber.printNumber()
#Getter of the RealPart
print("RealPart part in another calculation (Real Part + 10.0)")
print((FirstNumber.get_RealPart()) + 10.0)
#Getter of the ImaginaryPart
print("Imaginary part in another calculation (Imaginary Part + 5.0)")
print((FirstNumber.get_ImaginaryPart()) + 5.0)


#9. REDEFINITION OF MATHEMATICAL OPERATORS WITH OBJECTS
#Let's check an example with the Operators Class
class Operators:
    def __init__(self,list):
        self.list = list  #return the values in a list form
    def visualization(self):
        print(self.list)
#Buil methods with mathematical operators
    def __add__ (self, integer):
        new = []
        for x in range(len(self.list)):
            new.append(self.list[x] + integer)
        return new
    def __sub__ (self, integer):
        new = []
        for x in range(len(self.list)):
            new.append(self.list[x] - integer)
        return new
    def __mul__ (self, integer):
        new = []
        for x in range(len(self.list)):
            new.append(self.list[x]*integer)
        return new
    def __floordiv__ (self, integer):
        new = []
        for x in range(len(self.list)):
            new.append(self.list[x] / integer)
        return new
#Build the objects of the class
data = Operators([23, 57, 89, 47])
data.visualization()
print(data + 2)
print(data - 2)
print(data * 2)
print(data // 2)


#10. REDEFINITION OF RELATIONAL OPERATORS WITH OBJECTS
#Let's check an example with Person Class
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
#Buil methods with relational operators
    def __eq__ (self, object2):
        if self.age == object2.age:
            return True
        else:
            return False
    def __ne__ (self, object2):
        if self.age != object2.age:
            return True
        else:
            return False
    def __gt__ (self, object2):
        if self.age > object2.age:
            return True
        else:
            return False
    def __ge__ (self, object2):
        if self.age >= object2.age:
            return True
        else:
            return False
    def __lt__ (self, object2):
        if self.age < object2.age:
            return True
        else:
            return False
    def __le__ (self, object2):
        if self.age <= object2.age:
            return True
        else:
            return False
#Build the objects of the class
person1 = Person ("Lorena", 27)
person2 = Person ("Lucia", 27)
if person1 == person2:
    print("Both people have the same age")
else:
    print("Both people do not have the same age")

#11. OBJECT FILE
#Check an example of the Object File 
file = open ("file.txt", "w+")
content = file.read()
end_of_file = file.tell()
file.write("New Line")
file.seek(end_of_file)
new_content = file.read()
file.close()
print(new_content)