#I ask the user to enter a sentence and I use my own technique to put it in <title> format 
#without going through Python's <title> function
name = "hello world, you're mine"
name_split = name.split(" ")
a = name_split[0][0].upper() + name_split[0][1:].lower()
e = len(name_split)
ch =""
y =-1
for i in name_split:
    y+=1 
    x = str(name_split[y][0]).upper() + str(name_split[y][1:]).lower() 
    ch += x + " "

print(ch)