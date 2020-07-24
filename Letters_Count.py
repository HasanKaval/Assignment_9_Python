sentence = (input("Please enter a sentence : ")).lower()
letter_dic = {}

for i in sentence :
    counter = 0
    for j in sentence :
        if i == j :
            counter += 1
    item = {i:counter}
    letter_dic.update(item)
print(letter_dic)
