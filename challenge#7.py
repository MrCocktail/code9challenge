#I have a string and for each character that precedes a vowel, I will replace it with an asterisk

ch = "Jean David Bruno"
l = len(ch)
u = list(ch)
vow = "a,e,i,o,u,y"
e = 0
while e < l:
    if u[e] in vow:
        u[e-1] = "*"
    e += 1
g = "".join(u)
print(g)