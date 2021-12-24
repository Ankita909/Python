
import numpy as np
help(np.zeros)

x=np.zeros(6) #by-default float
print(x)

y=np.zeros((3),dtype="int")
print(y)

z=np.zeros([3,4])  #list
print(z)
z=np.zeros((3,4))
print(z) #tuple

# if the order is changed

a=np.zeros(4,order="F")
print(a)

b=np.zeros((3,4),order="F")
print(b)
