# 6} converting nested loops into list comprehension

fruits = ['apple', 'orange', 'pear' ,'pineapple', 'durazno']

numbers = [4,5]

out = []

for fruit in fruits:
    for number in numbers:
        out.append(f'{fruit}-{number}')
print(out)

print()
print()

#the nested for loop can be converted into a list comprehension:
x = [f'{fruit}-{number}' for fruit in fruits for number in numbers]
print(x)

