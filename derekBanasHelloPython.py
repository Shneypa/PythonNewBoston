
import random
import sys
import os

print('Hello World')

#Comment

'''
Multiline
comment
'''

name = "Derek"

print(name)

# DATA TYPES:  Numbers String Lists Tuples Dictionaries

# OPERATORS   + - * / ** (exponential multiplication)   // (floor division. divides then rounds down)

print('5 ** 3 = ', 5 ** 3, ' (exponential multiplication. raises to the power of... ) ')
print('50 // 14 = ', 50//14, ' (floor division. discards remainder) ')

quote = "\"Its a quote\" and the BACKSLASH helps us write qoutes"
print(quote)

multi_line_qoute = '''and we can join with
 another string'''

new_string = quote + ' ' + multi_line_qoute
print(new_string)

#formatting strings when printing:
print("%s %s %s" % ('I like the quote', quote, new_string))

print("I don't like the ", end = '')
print("newlines")

print("\n" * 5)
print("^^ those were 5 new lines")



#
#
#
# LISTS
#
#
#

print('\n', 'LISTS: ')

grocery_list = ['Juice', 'Tomatoes', "Peaches", 'Milk']
print("First item in list: ", grocery_list[0])

grocery_list[0] = "Green Juice"
print("First item in list after change: ", grocery_list[0])

print("List elements 1:3  (up to 3) ",grocery_list[1:3])

other_events = ['Wash car', 'Pick up kids','Cash check']

print("\n", 'Lists of lists: ')
to_do_list = [other_events, grocery_list]
print(to_do_list)

print("Use 3rd element from second list: \n to_do_list[1][2] = ", (to_do_list[1][2]))

grocery_list.append("Onions")
print(to_do_list)

grocery_list.insert(1, "Pickle")
print(to_do_list)

grocery_list.remove('Pickle')
print(to_do_list)

grocery_list.sort()
print(to_do_list)

grocery_list.reverse()
print(to_do_list)

del grocery_list[1]
print(to_do_list)

# join 2 lists into 1 list
to_do_list2 = other_events + grocery_list
print(to_do_list2)

# print list length, max element and min element  (alphabetically for strings)
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

print("\n" * 5)


#
#
#
# TUPLES
#
# (can't change once made)
#

print('\n', 'TUPLES: ')

pi_tuple = (1,4,25,63,7)

#converting tuple to list:
new_list = list(pi_tuple)

# converting list to tuple:
new_tuple = tuple(new_list)

print(len(pi_tuple))
print(min(pi_tuple))

print("\n" * 5)


#
#
#
# DICTIONARIES
#
# (can't be joined like lists)
#
# (stores as separate value pairs,   prints pairs in random order)

print('\n', 'DICTIONARIES: \n')

# enter KEY : VALUE
super_villains = {'Fiddler' : "Joe Satriani" , 'Jason' : "Misha Kasatkin", 'Chupakabra' : 'Musya the dog'}

print(super_villains['Chupakabra'])

super_villains['Jason'] = 'Jason Statham'

print(super_villains['Jason'])

print(len(super_villains))

print(super_villains.get("Chupakabra"))

print(super_villains.keys())

print(super_villains.values())


print("\n" * 5)


#
#
#
# CONDITIONALS
#
#
#
#

print('\n', 'CONDITIONALS: \n')

# if else elif

age = 66

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')

if age >= 21 :
    print('You can drive a Truck!')
elif age >= 16 :
    print('You can drive a car')
else:
    print("Not old enough to drive!")


if ((age >= 1) and (age <= 18)) :
    print("Your age is between 1 and 18 ")
elif ((age == 21) or (age >= 65)) :
    print("You are 21 or 65+")
elif not (age == 30) :
    print("You're not getting a birthday celebration, sorry")
else :
    print("Lets celebrate ")

print("\n" * 5)


#
#
#
# FOR LOOPS
#
#
#
#

print('\n', 'FOR LOOPS: \n')

for  x in range(0, 10):             # 0 up to 10   (0 to 9 )
    print(x, ' ', end = "")

print("\n")

for y in grocery_list :
    print(y, " ", end = "")

print("\n")

for x in [2,4,6,8,10]:
    print(x)

print("\n")

# For Lists of Lists :

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y], " ", end="")

print("\n")


print("\n" * 5)


#
#
#
# WHILE LOOPS
#
#
#
#

print('\n', 'WHILE LOOPS: \n')

random_number = random.randrange(0,100)

while (random_number != 15) :
    print (random_number)
    random_number = random.randrange(0,100)

i = 0

while (i <= 20):
    if(i % 2 == 0):
        print(i, " ", end = "")
    elif (i == 9):
        break
    i += 1

print("\n" * 5)


#
#
#
# Defining FUNCTIONS
#
#
#
#

print('\n', 'DEFINING FUNCTIONS: \n')

def addNumbers(first, second):
    sum = first + second
    return sum

print(addNumbers(1,181))

print("\n" * 5)


#
#
#
# READING USER INPUT
#
#
#
#

print('\n', 'READING USER INPUT: \n')

# print ('What is your name?')

# name = sys.stdin.readline()

print ('Hello, ', name)

print("\n" * 5)


#
#
#
# STRING MANIPULATION
#
#
#
#

print('\n', 'STRING MANIPULATION: \n')

long_string = "Pink Floyd - The final cut"

print(long_string[0:4])

print(long_string[-5:])     # five last characters

print(long_string[:-5])     # up to five last characters

print( long_string[:4] + " panther.")

# !!! FORMATTING
print ("%c is my %s letter and  my %d number and %.5f" % (long_string[0], long_string[5:10], 100, 100.123456789))

print (long_string.capitalize())

print (long_string.find("Floyd"))

print(long_string.isalnum())

print (len(long_string))

print (long_string.replace("Floyd", "Panther"))

print (long_string.strip())

word_list = long_string.split(" ")

print(word_list)

print("\n" * 5)


#
#
#
# OPEN / CLOSE FILE
#
#
#
#

print('\n', 'OPEN / CLOSE FILE: \n')

# open or create a file      "wb" means we can write into it later
test_file = open("test.txt", "wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("Add this text to the file\n", "UTF-8"))

test_file.close()

                            # "r+"  is  read - write  mode
test_file = open("test.txt", "r+")

text = test_file.read()

print (text)

test_file.close()


#  os.remove("test.txt")