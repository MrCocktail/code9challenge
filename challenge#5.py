#I have a string containing numbers separated by spaces. 
#I will calculate the product of the sum of each digit that composes each of the numbers
a = "5 45 123 12"
a = a.split()
str_count = len(a)
lis = []
y = 0

while y < str_count:
    z = 0
    for i in a[y]:
        z += int(i)
    
    lis.append(z)       
    y += 1

from functools import reduce
final_value = reduce(lambda a,b: a*b, lis)
print(final_value)