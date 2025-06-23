# 3} enumerate & zip

fruits = ['apple', 'orange', 'pear' ,'pineapple', 'durazno']

for i,fruit in enumerate(fruits):
    print(i, fruit)
    
print()
print()
# note of course python indexes at 0    

##Now lets look at the Zip function
  
fruits = ['apple', 'orange', 'pear' ,'pineapple', 'durazno']
prices = [4,5,6,7,8]
letters = 'abcde'


for fruit,price,letter in zip(fruits,prices,letters):
    print(fruit, price, letter)