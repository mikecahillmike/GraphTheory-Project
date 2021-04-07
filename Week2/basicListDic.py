x = [1, 2, 3, "Hello", 1.0]
#print(x)
#print(x[0])# print first
#print(x[2])# print last
#print(x[-1])# print last

#for i in x[::2]:#every second element in list
#    print(i)
#    print(i + i)

#for i in range(10):# return list of numbers from 0-9
#    print(i)

#for i in range(5, 10):# return list of numbers from 5-9
#    print(i)

#for i in range(5, 10, 2):# return list of numbers from 5-19 every second 1
#    print(i)

# Dictionary 

d = {"no_doors": 5, "make": "Dacia", "model": "Duster"} 

print(d["no_doors"])

d["fuel"] = "Petrol"

# Make a list from a list

r = [1,2,3,4]

print(r)

s = [i*i for i in r]

print(s)