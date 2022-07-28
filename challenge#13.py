'''I have a sequence with length L, containing integers ranging from 0 to L-1.
I will do an iteration and at each turn of the loop,
I'll reverse my sequence while forcing the last element to remain static.
Finally, I will have a completely knocked down list after suffering L-1 knockdowns.
Before, I had recovered the index of an element that I display again once the program has been fully executed.'''
mylist = [0,1,2,3,4,5,6,7]
l = len(mylist) 
i = 0
print("N=3, index: ", mylist.index(3))
newlist = []

while i < l:
    inv = mylist[::-1]
    last_idx = inv[-1]
    newlist.append(last_idx)
    inv.remove(last_idx)
    mylist = inv
    
    i += 1

newlist = newlist[::-1]
print(newlist)
print("N=3, new index: ", newlist.index(3))
