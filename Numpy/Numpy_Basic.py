
# ----------creating and printing 1-D array---------------
import numpy as np
a=np.array([2,3,4,5])
print(a)

#-----------creating and printing 2-D array--------------
b=np.array([[2,3,4,5],[6,6,7,8]])
print(b)

#-----------------------upcasting----------------------
c=np.array([1,2,3.0])
print(c)

#-----------------------minimum dimension---------------
d=np.array([2,3,4],ndmin=2)
print(d)
e=np.array([2,3,4],ndmin=3)
print(e)
f=np.array([2,3,4],ndmin=1)
print(f)

#-----------Changing the data type of the array------
g=np.array([2,8,16],dtype="complex")
print(g)
h=np.array([(1,2),(3,5)],dtype=[('a','<i4'),('b','<i4')])
print(h['a'])

help(np.array)
