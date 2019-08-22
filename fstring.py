from datetime import datetime

first_name = 'Srdjan'
last_name = 'Milenkovic'

sentance = "My name is {} {}".format(first_name, last_name)
print (sentance)    # My name is Srdjan Milenkovic

# fstring , variablu odmah stavljamo u placeholder , pocinje sa f , format je  > f'string{}' <

sentance = f'My name is {first_name.upper()} {last_name.upper()}'
print (sentance)    # My name is SRDJAN MILENKOVIC   (dodao upper() method )

## Fstring dictionary

person = {'name': 'Jan', 'age': '23'}
sen = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sen)   # My name is Jan and I am 23 years old

sent = f"My name is {person['name']} and i am {person['age']} old"   # mora " na pocetku i kraju zbog ' u sred stringa
print (sent)    #My name is Jan and i am 23 old

# Calculacije u okviru fstring-a

calc = f'4 times 11 is equal to {4 * 11}'
print (calc)   #4 times 11 is equal to 44

for n in range(1,11):
    s = f'The value is {n}'
    print (s)   # The value is 1 ; The value is 2; The value is 3;  itd

birthday = datetime(1984, 4, 11)
se = f'Srdjan has a birthday on {birthday:%B %d, %Y}'      # date time formating %B - mesec , %d - dan m=, %Y - godina
print (se)      #Srdjan has a birthday on April 11, 1984
