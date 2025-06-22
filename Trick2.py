# 2} break vs continue

#here break and continue are keywords you can put in the middle of 
#your loops

# break --> stops the entire loop
# contine --> doesn't stop the entire loop but SKIPS TO NEXT iteration

fruits = ['apple', 'orange', 'pear' ,'pineapple', 'durazno']

#this loop breaks when finding pineapple and doesnt print it
for fruit in fruits:
    if fruit == 'pineapple':
        break
    print(fruit)


    fruits = ['apple', 'orange', 'pear' ,'pineapple', 'durazno']

print()
print()

#this loop skips when finding pineapple and doesnt print it
for fruit in fruits:
    if fruit == 'pineapple':
        continue
    print(fruit)