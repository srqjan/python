#https://www.youtube.com/watch?v=3dt4OGnU5sM&t=143

# Want 'n' for 'n' in nums
numms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = []
for num in numms:
    list.append(num)          # update ( dodaje )  u list ( list = [] )

print(list)        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehansions
l = [n for n in numms]
print(l)               # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Want n*n for n in nums
l1 = []
for n in numms:
    l1.append(n*n)
print(l1)              # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List comprehensions
l11 = [n*n for n  in numms]
print(l11)                   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# n for n in numms if n is even ( deljiv )
l2 = []
for n in numms:
    if n%2 == 0:
        l2.append(n)
print(l2)              #[2, 4, 6, 8, 10]

#List comrehensions
l22 = [n for n in numms if n%2 == 0]    # [2, 4, 6, 8, 10]
print(l22)

# Nested loop
# Want (letter, num) pair for each letter in abcd and each number in 0123
l3 = []
for letter in 'abcd':
    for n in range(4):       # 0,1,2,3
        l3.append((letter, n))            # append tuple (letter, num) to l3

print (l3) # [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

# list comrehentions
l33 = [(letter, num) for letter in 'abcd' for num in range (4)]  # letter , num mora da se matchuje sa letter ,num in for loop
print (l33)  # [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]


## DICTIONARY COMPREHENSIONS - Napravi dict od dve list-e , pre toga zip dve liste

names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']
par = zip(names, heros)
print(par)   # [('Bruce', 'Batman) , ('Clark', 'Superman') , ('Peter', 'Spiderman')]

# I want a DICT ( name: hero )
my_dict = {}
for name, hero in zip(names, heros):
    my_dict [name] = hero

print (my_dict)   # {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman'}

# Dict comrehensions
dict1 = {name: hero for name , hero in zip(names, heros) if name != 'Peter'}  # is not Petar exlude from dict
print(dict1)       # {'Bruce': 'Batman', 'Clark': 'Superman'}

# PASS LIST TO THE FUNCTION WITH MAP #  You can pass one or more iterable to the map() function.
# Returns a list of the results after applying the given function
# to each item of a given iterable (list, tuple etc.)
# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print q(result)