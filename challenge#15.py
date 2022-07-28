'''I have two strings and I'm going to display elements that are in the middle'''
a = "hidden"
b = "modpass"
la = len(a)
lb = len(b)
xla = int(round(la/2,1))
xlb = int(round(lb/2,1))
print(a[xla], b[xlb])