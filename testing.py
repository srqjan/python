#### L I S T S  #############
numbers = [1, 3, 4, 5, 6, 9]
numbers.insert(2, 23)          # insert broj 23 na poziciju 2 (sada je tu 4 )  # [1, 3, 23, 4, 5, 6, 9]
numbers.remove(3)              # remove 3 #  [1, 23, 4, 5, 6, 9]

numbers.pop()                  # brise poslednju poziciju (9)  # [1, 23, 4, 5, 6]
numbers.sort()               # prvo sortiras ( od najmanjeg ka najvecem )
print(numbers)
numbers.reverse()            # sort od najveceg ka najmanjem ( posle numbers.sort )

print(numbers)               # pa print  ne radi print(numbers.sort()) , vraca object None
#numbers.clear()                # brise sve u listi  #
numbers2 = numbers.copy()      # kopiras listu u novu listu numbers2

#### NADJI UNIQ - REMOVE DUPLICATE

num = [1, 1, 3, 3, 4, 5,5]
uniq = []      # init empty list
for n in num:
    if n not in uniq:
        uniq.append(n)
print(uniq)                 # [1, 3, 4, 5]

# Unpacking list
coord = [1, 4, 6]
x, y, z = coord    # x = 1, y = 2, z = 3 # Unpacking
##### T U P L E  #############
coordinates = (1, 2, 3)
x, y, z = coordinates    # x = 1, y = 2, z = 3 # Unpacking


###### DICT

customer = {
    "name" : "John Smith",
    "age" : "30",
    "is_verified": True
}

print(customer["name"])            # John Smith
print(customer.get("age"))         # 30           # drugi nacin da se pristupi u element dict je preko .get methoda

# Update element of dictionary
customer["name"] = "Jack Smith"

#### SPLIT STRING AND ASSIGN
str1 = 'John-Doe-70000'
str2 = 'Steve Be 60000'
first, last, pay = str1.split('-')   # split on " - " and assign to variable
fr, la, pa = str2.split(' ')         # split on space '  " and assig to variable 
print(first, last, pay)    # John Doe 70000
print(fr, la, pa)        # Steve Be 60000