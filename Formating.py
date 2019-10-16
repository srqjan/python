import datetime

#https://www.youtube.com/watch?v=vTX3IwquFkc&list=PLaL2yxczKLcDWDRB0ZrxsuKlupJU0Njje&index=7
pearson = {'name': 'John', 'age': 23}    # Dictionary


# primitivno
sentance = 'My name is ' + pearson['name'] + 'and I am ' + str(pearson['age']) + 'years old'
print(sentance)      # My name is Johnand I am 23years old
# Formating string ( moze i sa f-string-om )
sen1 = 'My name is {} and i am {} years old'.format(pearson['name'], pearson['age'])
print (sen1) #My name is John and i am 23 years old
sen2 = 'My name is {0} and i am {0} years old'.format(pearson['name'], pearson['age']) # 0 je prvi parametar ('name') a 1 je drugi ('age')

# Pristupas razlicitim key-evima dictionary-ja , jako korisno , isto je sa listom
sen3 = 'My name is {0[name]} and i am {0[age]} years old'.format(pearson) #  0 = pearson ,
print (sen3) # My name is John and i am 23 years old

l3 = ['John', 23]
senl3 = 'My name is {0[0]} and i am {0[1]} years old'.format(l3)   # 0 = l3 , [0] = John , [1] = 23
print(senl3)   #My name is John and i am 23 years old

# Unpacking list and dict and formating ( prefered way to do formating )
sent5 = 'My name is {name} and i I am {age} old'.format(**pearson)  # unpacking dict (or list )
print(sent5)  # My name is John and i I am 23 old


class Pearson():
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instance
p1 = Pearson('Jack', 24)

sen4 = 'My name is {0.name} and i am {0.age}'.format(p1)  # 0 = p1 , pristupas p1.name i p1.age
print(sen4)  # My name is Jack and i am 24

# FORMATING NUMBERS

for i in range(1, 11):
    s = 'The value is {}'.format(i) # {:02} - dve decimale ,
    print (s)

# Datumi

date = datetime.datetime(2016, 9, 24, 12, 30, 45)
s1 = '{:%B %d %Y}'.format(date)  # : znaci formating, %B mesec , %d dan , %Y godina
print (s1)   # September 24 2016


