#----------------------Lists comprehension--------------------------------


'''List comprehension :
It is an elegant and concise way to create a new list from an existing list in Python
It consists of an expression followed by for statement inside square brackets.

Syntax:
new_list=[expression   for item in list   if condition] '''

a=[x for x in range(100)]
print(a)

print("------------------------------------------------------------------------------------------")

# even numbers list
a=[x for x in range(100) if x%2==0]
print(a)
 
print("------------------------------------------------------------------------------------------")
# odd numbers list
b=[x for x in range(100) if x%2==1]
print(b)

print("------------------------------------------------------------------------------------------")

# 3 raise to power x
c=[3**i for i in range(10)]
print(c)
