# a, b=c=7, 8
# print(a)
# print(b)
# print(c)
# a=b, c = 4, 2
#print(a, b, c)
# ----> swapping of variables
a = 7
b = 5



temp=a #temp=7
a=b
#a=5
b=temp #b=7
# a=5, b=7

print(a, b)
# a=a+b #a=12
# b=a-b #b=12-7=5
# a=a-b #a=12-5=7
# print(a, b)
# a, b=b, a # only in python # print(a, b)

# a=a*b #a=35
# b=a/b #b=35/7 = 5.0
# a=a/b #a=35/5= 7.0
# print(int(a), int(b))

#id() --> used to find the memory address of the variable
a = 7
b = 8
print(id(a))
print(id(b))
#-----> Keywords
# Keywords are reserved words which provides special meaning to
# compiler or interpretor
import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(type(keyword.kwlist))
# To check if the string is keyword or not
# print(keyword.iskeyword("sai"))
# False
# if = 8
# print(if)
# error coz if is a keyword

#!----> literals
# Literal is the constant value asssigned to a variable
# A variable is considers to be constant when it is defines
# in caps
#a= 78# a is variable
#A=78# A is constant

# hash() --> it creates a hast value for constant datatypes and
# provides error for non constant datatypes
#n1 = 89+7j
#print(hash(n1))

#f1 = [7, 8, 9]
#print(hash(f1)) # error --> list is non-constant or mutable datatype

# a = 9
# b = 9
# b = 90
# print(id(a))
# print(id(b))


#-> Operators
# ? Opeartors are symbols which is used to perform various opearions
# ? bewtween 2 or more operands
# Arithmatic
# Assignment
# Logical I
# Relational or comparison
# Bitwise
# Identity
# Membership

# todo -- Arithmatic --> +, -, *, /,%, //, **
# Eg:1
# a = 8
# b = 6
# c = 9
# print(a+b+c):
# input() --> used to get the runtime input
n1 = input("Enter the value: ")
print(n1)


# input() --> used to get the runtime input
# eval() --> used to get the runtime values of all datatype


# n1 = eval(input("Enter the value: "))
# print(type(n1))


#a = 4
#b = 2
#print(a/b) # is used to get the quotient value
#print(a%b) # is used to get the remainder value


#! //--> floor devision
# a 765433
# b = 19
# print(a//b) # -> the output will be inn integer & the output will be # based on floor value
#! ** --> used for power of a number
# print(2**4) # --> 16
#! Assignment -->
# a= 8
# a+=2
# print(a)
# a=30
# a-=5
# print(a)




#! comparison --> ==, >, <, =, <=, >=
# a = 8
# b = 7
# print(a>b) # True
# a = 9
# b = 5
# print(a==b)
#! Bitwise operator -->



a = 7
b = 4
print(a&b)
# 2^4 2^3 2^2 2^1 2^0
#8421
# 0111
#0100
#--> 7
# --> 4 &
# ----------------
# 0100I

#~ --->
# a = 9876
# print(~a)
# a = 9
# 128 64 32 16 8 4 2 1
#0 10 0 1 0 0 1 # --> 9


#! Identity operator
# ? It is used to compare the memory location that the values # ? are stored
# is, is not
a = 8
b = 8
# print(a is b)
# print(a==b)
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is not b)

#! Membership operator
# in, not in
# 11 = [7,8,9,0, 6, 5]
# num = 55
# print(num in 11)
# print(num not in 11)
# num = 678
# print(8 in num) # error

# eg:4
# a = 0
# a = None
# a=False
# a=""
# if a:
# I print("yes")
# else:
# print("no")

# a number is even or odd
n = int(input("enter the number: "))
if n % 2==0:
     print(n, "is even")
else: 
    print(n, "is odd")

# sum:2
# name, age, nationality
# 18 above, Indian
    
name = input("Enter the name: ")
age = int(input("enter the age: "))
nationality=input("enter the nation: ")
if age>=18 and nationality=="Indian": print("eligible for vote")
else:
  print("not eligible")



