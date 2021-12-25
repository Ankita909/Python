import numpy as np
#help(np.linspace)
x=np.linspace(2.0,3.0,num=5)
print(x)

y=np.linspace(2.0,3.0,num=5,endpoint=False) #excluding endpoint
print(y)

z=np.linspace(1,150,num=4,dtype=int)
print(z)

a=np.linspace(1,10)
print(a)

b=np.linspace(2.0,3.0,num=5,retstep=True)
print(b)
