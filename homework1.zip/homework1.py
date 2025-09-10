#File: homework1.py

a = 10
print(a)
print(type(a))

b = 1.5
print(b)
print(type(b))

c = 3j
print(c)
print(type(c))

d = "hello"
print(d)
print(type(d))

e = [1, 2, 3]
print(e)
print(type(e))

f = {"name":  "Ellen", "favorite fruit":  "strawberry"}
print(f)
print(type(f))

g = (1, 2)
print(g)
print(type(g))

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))

i = True
print(i)
print(type(i))

j = None
print(j)
print(type(j))

k = [True, "blue", 12]
print(k)
print(type(k))

l = str(14)
print(l)
print(type(l))

m = 1e4
print(m)
print(type(m))

#How many different data types did you find?
#9 different data types

#List all the data types you found.
# int 
# float 
# complex 
# str
# list
# dict 
# tuple
# bool 
# NoneType

#What variables have the same data types?
#Variables e, h, and k are all lists.

#What was the data type of l? Why is it not an integer? What does str() do?
#l is a string and not an integer because str() forcefully changed the type int to type str.

#Look up one more data type not given above. Repeat the same procedure.
#there is a set data type that is not given.

print(10>9) #true 10 is greater than 9

print(10==9) #false 10 does not equal 9

print(10<=9) #false 9 its not bigger or equal to 10

print(bool("abc")) #true string not empty

print(bool(123)) #true int not empty

print(bool(["apple", "cherry", "banana"])) #true list is not empty

print(bool(True)) #true 

print(bool(False)) #false

print(bool(0)) #false 0 is false

print(bool("")) #false empty is false

print(bool(" ")) #true not empty, space is something, true

print(bool(())) #false empty is false

print(bool([])) #false empty is false

print(bool({})) #false empty is false

bool(True and False) #false both arent true

bool(True and True) #true both are true

bool(False and False) #false both are not true

bool(True or False) #true one of them is true

bool(True or True) #true one of them is true

bool(False or False) #false both of them is not true

bool(not(False)) #true opposite of false

bool(not(True)) #false opposite of true

#Questions:

# What pattern do you notice about expressions returning True or False?
# and is true if both is true. 
# if a variable is empty then it is false, else true. 
# or is true if one of them is true.
# not reverses the boolean result.


# Which expression surprised you about its result?
#bool(" "), i thought its empty so it should be false, but apparently space count as something in the string

#Create an expression, not given above, that will return True. Why is it True?
#bool("I like apples"), this is true because the string is not empty

#Create an expression, not given above, that will return False. Why is it False?
#bool(False and True or false), this is false because and has a higher level than or.
# ^ this above would evaluate false and true first --> false, then false or false gives false.

print(10 + 5)   # 15, addition
print(10 - 5)   # 5, subtraction
print(2 * 4)    # 8, multiplication
print(6 / 3)    # 2.0, division that returns float
print(5 % 2)    # 1, gives the remainder of division
print(3 ** 2)   # 9, multiplies exponentially
print(15 // 2)  # 7, floor division, no remainder 

print(5 == 2) # false, 5 equal 2
print(10 != 10) # false, 10 does not equal to 10
print(2 < 5) # true, 5 is greater than 2
print(12 > 5) # true, 12 is greater than 5
print(5 <= 6) # true, 6 is greater than or equal to 5
print(1 >= 10) # false, 1 is greater than or equal to 10

x = 5 # 5
x += 5 # x+5 = 10
x -= 4 # 10-4 = 6
x *= 3 # 6*3 = 18

print(True and True) # true
print(False and False) # false

print(True or False) # true
print(False or False) # false

print(not True) # false
print(not False) # true

print(7 / 2) # 3.5 has remainder
print(7 // 2) # 3 does not have remainder

print(7 % 2) # 1 prints out the remainder only
print(7 // 2) # 3 rounds down the result

print(10 % 3) # 1


# assignment operators
#  x = some number, x+= some number equals to x = x + some number, vice versa

my_string = "hello"

print(my_string)  # hello      
print(my_string[0])    #h 
print(my_string[1])    #e
print(my_string[2])    #l 
print(my_string[3])    #l 
print(my_string[4])    #o 
print(my_string[-1])   #o
print(my_string[1:3])  #el
print(my_string[0:5:2]) #hlo
print(len(my_string))   #5
print(my_string + "goodbye")  #hellogoodbye
print(my_string * 7)    #hellohellohellohellohellohellohello

#slicing happened whenever I printed the string at index (...)

name = "Oski"
print("Hello, my name is", name) #Hello, my name is Oski

name = "Oski"
print(f"Hello, my name is {name}") #Hello, my name is Oski

#the second string differs from the first because the second line of code (aka the F string) evaluates
#whatever is inside the {} as a function, so name becomes Oski. where as the first code just uses print()

#cd
#change directories
#cd python_decal_FA25

#ls
#list files and directories
#ls

#ls -a
#list all files and directories (including the ones hidden)
#ls -a

#mkdir
#makes a new directory
#mkdir steven

#cat
#prints your code in the terminal (every content)
#cat datatypes.py

#pwd
#print working directory
#pwd

#cd ..
#moves 1 directory up
#cd ..

#cd .
#this directory, no effect
#cd .

#cd ~
#takes you to the root directory
#cd ~

#cp
#copies a file or a directory
#cp copy_datatypes.py

#mv
#moves or renames a file or directory
#mv datatypes.py

#rm
#permanently deletes a file
#rm datatypes.py

#clear
#clears the terminal screen
#clear

#grep
#search for patterns or words in a file
#grep "hello" datatypes.py

#3 new commands that is not present
#touch
#creates an empty file
#touch coding.py

#heads
#prints the first line of the file
#heads datatypes.py

#tails
#prints the last line of the file
#tails datatypes.py

#What is the difference between ls and ls -a?
#ls shows files in the directory, ls -a shows files and hidden files in the directory.

#What is a hidden file?
#a hidden file usually starts with . they are system files

#Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.
#ls -l shows the details of the files such as size and date
#rm -r delete a file recursively
#cp -r copies a file recursively

