'''I have a list of numbers.
I will display in two different ways the smallest and the largest number 
without going through the min() and max() methods of python'''
numb = [1,7,2,12,3,6,-1,5]

def minimum():
    global numb
    min = numb[0]
    for i in numb:
        if i < min:
            min = i
    return min

def maximum():
    max = numb[0]
    for i in numb:
        if i > max:
            max = i
    return max

print("The min is:", minimum(),"/ The max is:", maximum())


'''
#The second method:

l = len(numb)
lis = []
def minimum():
    x = 0
    while x < l:
        lis.append(numb[0])
        for i in numb:       
            if i < lis[-1]:
                lis.append(i)
        x += 1
    return lis[-1]

def maximum():
    x = 0
    while x < l:
        lis.append(numb[0])
        for i in numb:       
            if i > lis[-1]:
                lis.append(i)
        x += 1
    return lis[-1]
    
print("The min is:", minimum(),"/ The max is:", maximum())
'''