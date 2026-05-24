# string
name='noor'
print(name)
# user input
name=(input("Enter your name:"))
print("Your name is",name)
# String cancatination
str1="Noor"
str2="Ul"
str3="Huda"
string=str1+" "+str2+" "+str3
print(string)
# slicing
print(string[8])
print(string[1:4])
# negative slicing
print(string[-3:])
print(string.upper())
print(string.lower())
print(string.endswith("a"))
# true
print(string.endswith("or"))
# false
print(string.capitalize())
# Noor ul huda
print(string.replace('Huda','Eman'))
# Noor Ul Eman
print(string.find("Ul"))
# 5
print(string.count("o"))
# 2
