#---------------File handling in python--------------------
'''
What is a file?
FIle is a named location on disk to store related information.
It is used to permanently store data in a non-volatile memory.(eg,Hard Disk)
In order to read or write to files we use the following process:

Open the file
Read or write to the file(perform operation)
Close the file
'''
file = open('desktop/qwik.txt', 'w')     #open the file named records.txt in write mode
file.write('hello')                #write the text 'hello' to the file
file.close()                       #close the file

file = open('desktop/qwik.txt', 'r')

output = file.read()

print(output)

file.close()



