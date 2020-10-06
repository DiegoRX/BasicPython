print('We are going to compare the age of 2 people')
name_1 = input('Type the name of the first person: ')
num_1 = int(input('Type the age: '))
name_2 = input('Type the name of the second person: ')
num_2 = int(input('Type the age: '))

if num_1 > num_2:
    print(f'{name_1} is older than {name_2}')
elif num_1 < num_2:
    print(f'{name_2} is older than {name_1}')
else:
    print(f'{name_1} and {name_2} are the same age.')