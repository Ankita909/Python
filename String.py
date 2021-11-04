''' -------------------------------------Strings in Python--------------------------------
 
 A string is a sequence of characters.
 It can be created by enclosing the characters inside a single quote or double quotes.
 Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

 Strings are immutable: This means that the elements of the string cannot e changed once it has been  '''


name = """Ankita
 Kshatriya"""
paragraph='''This is 
 a multiline 
 string
 paragraph.This is for Testing'''
print(name)
print(paragraph)


#indexing

fruit="Apple"  #index starts from 0 (apple has a range of 0-4)
print(fruit[1])
#print(fruit[5]) this will give an error because there is no fifth index (characters are only till 4th index )

#accessing last character

my_name="Ankita"
print(my_name[5])
print(my_name[-6]) #negative indexing (last character)

