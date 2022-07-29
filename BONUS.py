'''This is the reverse of the previous code. 
See challenge#16 in this same GitHub branch. Basically, it's a code that encrypt any word.
Let's have fun !'''
import string
import random
word = "software"
word = word.upper()
lis = []
alphabets = string.ascii_uppercase

for i in word:
    nb = random.randrange(0,26) #The program chooses a random number
    id = alphabets.index(i)     #We take the index of the word's letter in the alphabet
    if id > nb:       
        idx_nb = alphabets[nb]
        x = id - nb             #We calculate the steps
        hidden_word = f">{x}{idx_nb}"
        lis.append(hidden_word)

    if id < nb:     
        idx_nb = alphabets[nb]
        x = nb - id
        hidden_word = f"<{x}{idx_nb}"
        lis.append(hidden_word)

result = " ".join(lis)
print(f'"{result}"')