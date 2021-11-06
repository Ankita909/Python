#----------Write a function which takes a list of names as argument and greets " Hello Everyone " .-------------


def greet_everyone(names):
    for name in names:
     print("Hello",name)

names=['Ankita','Akash','Srishti','Anshu']
greet_everyone(names)