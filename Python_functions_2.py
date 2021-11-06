print("-----------------------------------------Calling the Function---------------------------------------")

def greet(name,dish="Pasta"):
    print('Good Morning!', name)
    print('Please have your..',dish)

greet('Ankita')

print("------------------------------------------Returning from the Functions-----------------------------")
'''The return statement is used to exit a function and go back to the place from where it was called.'''

# Syntax: return [expression_list]

def sum_of_list(a):
    print('Calculating...')
    return sum(a)

marks= [20,40,60,60,70,90]
sum_of_marks=sum_of_list(marks)

print('My sum of marks:', sum_of_marks)

