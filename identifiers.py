# Identifiers in Python

name="Ankita Kshatriya"
age=20

print (name)
print(age)

# Valid identifiers

Name="Ankita"
last_name="Kshatriya"
age=20
_country="India"
name2="Ankita2"

print(Name,last_name,age,_country,name2)

# Invalid identifiers
2name="Ankita"    # starts with a number
country$ ="India"  # dollar sign is not permissible(only alphanumeric and Underscore is permissible)
break="hello" # because break is a reserved word that is , a keyword in python

print(2name,country$,break)
