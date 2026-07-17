list_b = [None] * 4
#print(list_b[1])
list_b[0] = '!'
list_b[1] = 'a'
list_b[2] = 'b'
list_b[3] = 'c'
print(list_b[0])
print(list_b[1])
print(list_b[2])

#1a list one data types
years = [1979, 1999, 2019]
#a list of different data types
superList = ['a', "Hello world", 2.9, 78]

print(years[0])
print(years[1])
print(years[2])
print(superList[0])
print(superList[1])
print(superList[2])
print(superList[3])

uberList = ["Not the taxi", 7, [0,1,2,3], 'c', 4.4]

print(uberList[0][0])
print(uberList[0][1])
print(uberList[0][2])
print(uberList[0][3])

print(uberList[2][0])
print(uberList[2][1])
print(uberList[2][2])

superlist = ["abc", "123"]
print(superlist[0][0])
print(superlist[0][1])
print(superlist[0][2])

#code to iterate over a list
loop_list = [12, 13, 54, 7, 91]

# Getting length of list
length = len(loop_list)
i = 0

# Iterating using while loop
while i < length:
    print(loop_list[i])
    i += 1
    
#code to iterate over a list
#using for loop
loop_list = [12, 13, 54, 7, 91]
for i, val in enumerate(loop_list):
    print(i, ",", val)
    
from array import *

def array_list(array_num):
    num_list = array_num.tolist()
    print(num_list)
    
num = array('i', [45,34,67])
array_list(num)
print(num[0])