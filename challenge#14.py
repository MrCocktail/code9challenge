''' I have these inputs and outputs:
a = 2                 4
b = 16         

a = 3                 4
b = 24

a = 1                 0.5
b = 1
I will create code to get these outputs '''
def calcul(a, b):
    total = (b/a) / 2
    return total
print(calcul(a=1, b=1))