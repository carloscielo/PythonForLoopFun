# 4} tuple unpacking during iteration

mylist = [(1,2),(3,4),(5,6)]

#here is the normal unpacking of a list:
for element in mylist:
    print(element)

print()
print()

#if you want to access the values directly you can do as follows:

for a,b in mylist:
    print(a,b)

#remember all tuples must be the same shape for you to do this
#remember how you unpack your tuples depends on their structure in the list