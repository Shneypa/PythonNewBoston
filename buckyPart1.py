


# Tutorial 14.    Assigning a DEFAULT value to an argument.         To avoid null errors later...

def get_gender(sex = "unknown"):            # assgning default value

    if sex is "m":
        sex = "male"
    elif sex is "f":
        sex = "female"
    print(sex)                              # or add to database

get_gender("m")
get_gender("f")
get_gender()




# Tutorial 16.      KEYWORD arguments

def simple_sentence(name="Ivanov", action="bought", what="dog"):
    print(name, action, what)

simple_sentence()
simple_sentence("Petrov", "bought", "car")
simple_sentence(name = "Obama", what = "a red carpet")




# Tutorial 17.      FLEXIBLE number of arguments

def add_numbers(*args):

    sum = 0

    for x in args:
        sum += x

    print(sum)

add_numbers(1,2,5,34,75,43,34)



# Tutorial 18.     UNPACKING  arguments         from  a List

def health_calculator (age, fitness_per_week, cigarettes_smoked_per_week, drinks_per_week):

    health_rating = (100 - age) + fitness_per_week * 20 - cigarettes_smoked_per_week - drinks_per_week * 4

    print(health_rating)


paul_data = [35, 3, 60, 6]

health_calculator(paul_data[0], paul_data[1], paul_data[2], paul_data[3])

health_calculator(*paul_data)                                            # automatically "unpacks" arguments from a list



# Tutorial 19.   SETS

#   SETS are collections of items ( but can't have duplicates ! )

set_a = {'onions', 'broccoli', 'beer', 'beer', 'milk', 'apples', 'eggs', 'eggs'}                # CURLYBRACES {}

print (set_a)



if 'broccoli' in set_a:                                                 # check if an item is IN the set
    print("You already have broccoli!")
else :
    print("Lets get that tasty brocoli!")





# Tutorial 20.   DICTIONARIES

#   DICTIONARIES are collections of VALUE PAIRS

classmates = {"Lucy": "stupid bitch", "Dodger": "cool guy", "Mark": "communist", "John":'hippie'}

print(classmates)                               # print all data of dictionary
print(classmates["Mark"])                       # print the value of specific KEY

print("\n")

for k, v in classmates.items():                 # loop through all  keys and their values
    print(k + " is a " + v)



print("\n")




# Tutorial 21.      using   MODULES


import utility

utility.print_version()