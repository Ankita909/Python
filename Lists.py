#----------------Lists in python----------------------

''' In python programming , a list is created placing all the items(elements) inside a square bracket[], seperated by commas.
It can have any number of items and they may be of different types(int,float,string,etc) ,'''

#   examples: my_list=[]
#             my_list=[1,"Hello",3.4]
#             my_list=[1,"hello",3.4]                  (heterogenous)


my_list=[1,2,3,4,5]
print(my_list)

my_list2=[1,2,3,4,5,"Ankita","Kshatriya"]
print(my_list2)

#type definition not required

name="Ankita"
name=12345
name=[2.5,3,"heeello"] #final value of name (value of name changed)
print(name)  #does not matter what type of data you are giving to the same variable ,it will override .


#---------------------------------------indexing in lists:-------------------------

fruit=["apple","mango","banana","cherry","grapes"]
print(fruit[4])
# print(fruit[7])  list index out of RANGE

#negative indexing
print(fruit[-2])


#----------------------------------slicing in lists------------------------

numbers=[1,2,3,4,5,6,7,8]
print(numbers[2:5])

#reverse list
print(numbers[::-1])

#reverse list by skipping 2 numbers
print(numbers[-1:0:-2])

#modifying the element of list
my_list3=["apple","mango","cherry","banana","guava"]

#change element
my_list3[3]='grapes'
print(my_list3)
#delete element
del my_list3[1]
print(my_list3)

''' we can modify lists....hence they are mutable'''