### Class uvek ima veliko pocetno slovo i sluzi za modeliranje stvari , prav;jenje templet-a.
#self.name = name takes the value stored in the parameter name and stores it
#in the variable name

class Dog():
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    #
    def sit(self):

        print(self.name.title() + " " + "is now sitting.")

    def roll_over(self):
        """ Simulate rolling over in response to a command"""
        print(self.name.title() +  " " +"rolled over!")

# Mozemo kreirati koliko god zelimo instanci koristeci jednu class-u
my_dog = Dog('zucko', 6)
your_dog = Dog('Maza', 3)

print("My dog is " + str(my_dog.age)  + "years old")
print("My dog's name is " + my_dog.name.title() + ".")

my_dog.sit()
my_dog.roll_over()

print("Your dog's name is  " + your_dog.name.title() + ".")

your_dog.sit()
your_dog.roll_over()


############## CLASS ATRIBUTES AND METHODS #############################3


class Employee:

    raise_amount = 1.04             # CLASS VARIABLE ( moze se koristiti u instance )
    num_of_emp = 0

    # CLASS ATRIBUTES
    """Initialize name and age attributes"""
    def __init__(self, first, last, pay):
        self.first = first                                  # class atribute
        self.last = last                                    # class atribute
        self.pay = pay                                      # class atribute
        self.email = first + '.' + last + '@company.com'    # class atribute

        Employee.num_of_emp += 1                            # uvecaj za 1 svaki put kad se kreira employee

    # CLASS METHODS ( def )
    def fullname(self):
        return f"{self.first} {self.last}"       # self - odnosi se na sve instance ( emp1 , emp2 .... )

    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amount)


emp1 = Employee('Srdjan', 'Milenkovic', 50000)
emp2 = Employee('Jack', 'Smith', 60000)

print(emp1.email)          # Srdjan.Milenkovic@company.com
print(emp2.last)           # Smith

#Nakon kreiranja class method fullname ,  ,mozemo koristiti method fullname
print(emp1.fullname())        # Srdjan Milenkovic
print(emp2.fullname())        # Jack Smith

print(emp1.raise_amount)        #   1.04     access to the class variable trough instance
print(Employee.raise_amount)    #   1.04     access to the class variable trough class

# __dict__  pretvara class / object / instance u dictionary

print(emp1.__dict__)     # {'first': 'Srdjan', 'last': 'Milenkovic', 'pay': 50000, 'email': 'Srdjan.Milenkovic@company.com'}

print(Employee.num_of_emp)         # 2     jer ima dva kreirana employee emp1 i emp2