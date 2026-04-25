# N1

name, surname = input("Write your full name: ").upper().split(" ")
print(F"{name[0]}. {surname[0]}.")

# N2

rotate = input("Write one word: ")
print(rotate[::-1])

# N3

sentence = input("Write sentence: ")
word1, word2 = input("Write which word to replace: ").split(" ")
sentence = sentence.replace(word1, word2)
print(sentence)