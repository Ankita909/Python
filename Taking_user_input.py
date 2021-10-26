# input function is used for taking the inputs from user

# Taking input from user
name=input()
print('Your name is ',name)


print('----------------------')


#adding two numbers by taking the numbers from user

a=input()
b=input()

#checking the type  of data the function can pass
print(type(a))
print(type(b))

c=a+b
print(c)
''' this will concat the numbers entered ,the reason being that the input function passes only strings through it and not integers .So it is considering the numbers entered for a and b to be strings '''


