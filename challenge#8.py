from re import X


#I have a string, I remove all white spaces

ch = "        Albert invented the formula E = mc^2   \nHe was very smart       "
x = ch.split(" ")
y = "".join(x)
print(y)