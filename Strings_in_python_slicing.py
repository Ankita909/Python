''' -------------------------------------Strings in Python--------------------------------
 
 A string is a sequence of characters.
 It can be created by enclosing the characters inside a single quote or double quotes.
 Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

 Strings are immutable: This means that the elements of the string cannot e changed once it has been  '''

 # slicing:
 # Python slicing is about obtaining a sub-string from the given string by slicing it respectively from start to end.
 # Python slicing can be done in two ways: slice() Constructor and Extending Indexing.

'''We can access individual characters using indexing and a range of characters using Slicing.
Index starts from 0
Tring to access a character out of index range will raise an index error.
The index must be an int

python allows negative indexing for ita sequences

The index -1 refers to the last item,-2 second last item
For accessing a range in string use slicing operator(colon) '''

s="abcde"
print(s[1:4]) #first char is inclusive but the destination char is not inclusive

print(s[1:5]) 

print(s[:4]) #first position is left empty (it will consider it from 0)

print(s[3:]) #destination position is left empty (will display till last char of the given string)

#by-default the step is considered to be 1
print(s[1:4:2]) #last index here means skipping 2 characters [start index,end index,steps]

#Note: Slicing will not change the original string,it just gives a new string as per the changes applied

print(s) #will give us the original string,no changes are saved in this

# Hence, strings are immutable.

#reversing a string:
print(s[::-1])

#empty string
print(s[0:5:-1]) 

print(s[-1:0:-1])
print(s[-1:0:1])

#similarly licing can be used in lists and tuples 