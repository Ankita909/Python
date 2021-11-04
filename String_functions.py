#---------------------------------------- Python String Methods--------------------------------------

# isalpha() :checks whether the given string has only alphabets

password="ankita123"
name="hello"
print(password.isalpha()) #checks whether the given string has only alphabets
print(name.isalpha())

#----------------------------------------------------------------------------------------------

# isdigit() :checks whether the given string has only numbers

passw="12345"
print(passw.isdigit())

#------------------------------------------------------------------------------------------------

# islower() :checks whether the given string is in lowercase
s="ANKITA"
v="ankita"
print(s.islower())
print(v.islower())

#--------------------------------------------------------------------------------------------------

# isupper() :checks whether the given string is in uppercase
w="ANKITA"
t="ankita"
print(w.isupper())
print(t.isupper())

#---------------------------------------------------------------------
# to print the strings in uppercase and lowercase resp
name="ANKITA"
name2="ankita"
print(name.lower())
print(name2.upper())

#-------------------------lstrip()  and rstrip()---------------------

x="       hello      "
print(x.lstrip())
print(x.rstrip())
print(x)  #this means that strings are immutable,whatever be the changes priginal string will remain the name