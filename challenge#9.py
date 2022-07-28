#in an inclusive interval, I display the sum of all even numbers

def total_even(a, b):
    tot = 0
    for i in range(a, b+1):
        if i%2==0:
            tot += i
    return tot
print(total_even(0,10))