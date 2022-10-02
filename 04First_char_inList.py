'''Write a program that forms a list of first character of every word in another List'''
letter = []
list_of = ["Hello","World","Programming","king"]

# for i in range(len(list_of)):
#     word = list_of[i]
#     print(word[0])

for word in list_of:
    letter.append(word[0])
print(letter)
