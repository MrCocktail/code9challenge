#I have a string and i remove the semicolon and all the characters before
a = "mwen la; m ap manje"
x = a.split(";")
v = x.remove(x[0])
print("".join(x))