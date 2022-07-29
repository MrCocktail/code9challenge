'''I have a string that represents a set of encrypted letters that form a word. 
I have to create an algorithm that can decrypt all this
Each character is composed of 3 or 4 subcharacters. 
The first tells us which way we should go through the alphabet from the last. 
Note that the characters in the middle tell us how many steps we should take this course in order to find the hidden letter.
For example: >3A gives the letter D, knowing that A represents the element 0 in the alphabet. 
Okay, let's code !!!'''

import string
hidden_word = ">7L <2Q <8N >16D >3T <6G >17A <5J"
hidden_word = hidden_word.split()
lis = []
alphabets = string.ascii_uppercase

for i in hidden_word:
    if i[0] == ">":
        id = alphabets.index(i[-1].upper()) + int(i[1:-1])
        word = alphabets[id]
        lis.append(word)
    if i[0] == "<":
        id = alphabets.index(i[-1].upper()) - int(i[1:-1])
        word = alphabets[id]
        lis.append(word)
print("".join(lis))