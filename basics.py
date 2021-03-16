# Michael Cahill
# Python basics
# 2021-03-15

#print("Hello World")

a = 1
b = 1.0
s = "Hello, World from a string"
t = '"Hello", from a different string'
 
#print(a, b , s, t)

#print(s[0:2]) # print char up to 2

# String Slice
#print(s[3:10:2]) # print char starting at 3 and finishing at 10 but in every 2

# Lists
x = [1, 2, 3, "Hello", 1.0]
#print(x)
#print(x[0]) # Prints first
#print(x[2]) # Prints third
#print(x[-1]) # Prints last item in list

for i in x[::2]:
    print(i)
    print(i + i)