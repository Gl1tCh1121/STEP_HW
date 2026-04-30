# N1

num = int(input("Write positive whole number: "))

while num > 0:
    print(num)
    num -= 1

print("text")


# N2

summ = 0
while True:
    numbers = int(input("Write whole numbers: "))
    summ += numbers
    if numbers == 0:
        break 

print(summ)

# N3

sec_num = 11

while True:
    guess_num = int(input("Guess the number: "))
    if guess_num > sec_num:
        print("Too high")
    elif guess_num < sec_num:
        print("Too low")
    else:
        print("Correct")
        break



# N4 

vowels = ["a", "e", "i","o", "u"]
filtered_text = ""
text = input("Text: ")

for ch in text:
    if ch not in vowels:
        filtered_text += ch
    
print(filtered_text)


# N5

for i in range(0, 9):
    print(i)

for i in range(5, 15):
    print(i)

for i in range(0, 20, 2):
    print(i)

for i in range(10, 1, -1):
    print(i)