import numpy as np
help(np.arange)


'''start value is considered in the array but stop value is excluded'''
x=np.arange(1,10) 
print(x)

y=np.arange(4.0)#given is the stop value , start value is by default 0
print(y)

z=np.arange(1,10,2) # start,stop,step
print(z)

t=np.arange(20,dtype="complex")
print(t)

v=np.arange(1,10,2,dtype="float") #all parameters
print(v)
