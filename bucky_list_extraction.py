# LIST EXTRACTION

grades = [1,8,8,8,5]

def drop_first_last_then_average_middle(list):
    first, *middle, last = list
    avg = sum(middle) / len(middle)
    return avg

print(drop_first_last_then_average_middle(grades))




## ZIP

first_names = ["Joe" , "Peter", "Glenn", "Cleveland", "Lois"]
last_names = ["Swanson" , "Griffin", "Quagmire", "Brown", "Griffin"]

names = zip(first_names,last_names)             # join two lists into a list of TUPLES

for a, b in names:
    print(a, "'s last name is ", b)