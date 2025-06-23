# 1} for-else and while-else


for i in range (5):
    print(i)
else:
    print('for loop else block runs because break didnt happen \n\n')

# how does a else statement make any sense inside a for loop?

# if the break keyword DOES NOT execute in the block then the else
# statement will run

# if the break keyword DOES execute in the block then the else
# statement will not run

for i in range (5):
    if i == 4:
        print('for loop first block is true,condition is met \n\n')
        break
else:
    print('for loop else block runs because break didnt happen')


#this also works with while loops

i = 0 
while i<3:
    i+=1
else: 
    print('while loop else block runs because break didnt happen \n\n ')


i = 0 
while i<3:
    i+=1
    if i==2:
      print('while loop first block is true,condition is met \n\n')
      break
else: 
    print('while loop else block runs because break didnt happen \n\n ')
