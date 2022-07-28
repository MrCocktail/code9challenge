
#suppose we don't have enough time to scan
#all the ports but we know an algorithm that will allow us to access the open port quickly
#We know that the port which is open is equal to the sum of all its components and we multiply 
#the final value by the first element to 
#find the index of the port


ip_address = input("Please, enter the IP Adress: ")
a = ip_address.split(".") #We remove the dots in the string in order to better perform the calculs
b = "".join(a)
total = 0 
for i in b:
    total += int(i)
total_value = total * int(b[0])
print("The open port's ID is ", total_value)
