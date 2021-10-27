#range function

'''Range function is used to generate a sequence of numbers 
For example- range(10) will generate  numbers from 0 to 9(10 numbers)'''

a=range(20)   # will display the range 
print(a)
 
 # will list all the numbers coming in that range
b=list(range(20))  #taking one arg , starting from 0
print(b)

c=list(range(20,30)) # taking two args (starting and ending)
print(c)

d=list(range(2,50,2))  #first arg is the starting number, second arg is the ending number and last arg is the number of steps(how many numbers to skip)
print(d)
