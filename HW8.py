# N1


def sum_of_digits(n):
    if n < 10:
        return n
    
    return n % 10 + sum_of_digits(n // 10)



result = sum_of_digits(123456)

print()
print("დავალება 1")
print()
print(result)
print()


# N2

iseven = lambda k: k % 2 == 0


print()
print("დავალება 2")
print()
print(iseven(10))
print(iseven(7))
print()


# N3


students = [
    ("Luka", 15, 85),
    ("Ana", 14, 92),
    ("Giorgi", 16, 78),
    ("Nino", 15, 95)
]

sorted_students = sorted(students, key=lambda k: (k[1], k[2]))

print()
print("დავალება 3")
print()
print(sorted_students)
print()




# N4


words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

sorted_words = sorted(words, key=lambda k: len(k), reverse=True)

print()
print("დავალება 4")
print()
print(sorted_words)
print()



# N5


cap_words = list(map(str.capitalize, words))


print()
print("დავალება 5")
print()
print(cap_words)
print()



# N6


numbers = [5, 12, 7, 18, 3, 24, 9]

filtered_numbers = list(filter(lambda k: k > 10 and k % 3 == 0, numbers))


print()
print("დავალება 6")
print()
print(filtered_numbers)
print()



# OPTIONAL TASK
students2 = [
    ("Luka", [85, 90, 78]),
    ("Ana", [92, 88, 95]),
    ("Giorgi", [70, 75, 80]),
    ("Nino", [95, 100, 98])
]

average = list(map(lambda k: (k[0], sum(k[1])/len(k[1])) , students2))

print("საშუალო ქულები")
for name, avg in average:
    print(f"{name}-ს საშუალო ქულაა: {avg:.2f}")
print()


filtered_students = list(filter(lambda k: k[1] >= 85, average))
print("საშუალო ≥ 85-ია")
for name, avg in filtered_students:
    print(f"{name}-ს საშუალო ქულაა: {avg:.2f}")
print()


sorted_students = sorted(average, key = lambda k: k[1], reverse=True)
print("საშუალო ქულის კლებადობით")
for name, avg in sorted_students:
    print(f"{name}-ს საშუალო ქულაა: {avg:.2f}")
print()
