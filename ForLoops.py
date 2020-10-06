fruits = ['Apple', 'Raspberry', 'Pinneapple']
for fruit in fruits:
        print(fruit)

# Apple
# Raspberry
# Pinneapple

##Iterables


# In Python, an iterable is an object 
# that can be used in a defined loop. 
# If an object is iterable it means that 
# it can be passed as an argument to the 
# iter function. The iterable that is 
# passed as a parameter to the iter 
# function returns an iterator.

fruit = ['Apple', 'Berry', 'Mango']
iterator = iter(fruit)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # StopIteration Error

students = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

#for loop directly on the dictionary
for country in students:
    print(students)

#for loop on keys
for country in students.keys():
    print(students)

#for loop on values
for number_of_students in students.values():
    print(students)

#for loop on items
for country, number_of_students in students.items():
    print(students)


# We can modify the behavior of a for loop through the keywords
# break and continue.

# break ends the loop and allows the rest of the flow of our
# Program.

# continue terminates the current iteration and continues with the next cycle of
# iteration.