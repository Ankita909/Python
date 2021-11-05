#-----------------------------List methods------------------------------------------------

a=[1,2,3,4,5]
a.append(6)   #adds an element(6) as the last element in the list
print(a)

#a[7]=10....................this gives an error because the size of the array is 5,so index out of bound exception

print("-----------------------------------------------------")

a.insert(1,0.5) #(position,element)
print(a)
a.insert(5,'Ankita')
print(a)

print("---------------------------------------------------------")

fruits=["apple","mango","guava","banana","cherry"]
fruits.sort()    #arrange in alphabetical order
print(fruits)

print("-----------------------------------------------------------")

a=[1,2,3,4,5,6,7,8,9]
a.pop(2)  #removes the element of this particular index
print(a)

a.clear()  #empty list
print(a)

print("-----------------------------------------------------------")
fruits.reverse()  #reverses the list
print(fruits)

print("-----------------------------------------------------------")

print(fruits.index('apple'))  #returns the position index
print(fruits.count('cherry'))  #returns the number of times this particular element is present in the list,ie,frequency