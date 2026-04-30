# N1

age = int(input("რამდენი წლის ხარ? "))

if age <=12:
    print("თქვენ ხართ: ბავშვი")
elif age <=19:
    print("თქვენ ხართ: თინეიჯერი")
elif age <=64:
    print("თქვენ ხართ: ზრდასრული")
else:
    print("თქვენ ხართ: უფროსი")


# N2

score = int(input("score: "))
attendance = int(input("attendance: "))

if score > 60 and attendance > 75:
    print("ჩააბარა")
else:
    print("ვერ ჩააბარა")


# N3 

student = input("ხარ სტუდენტი?(yes/no) ")
member = input("ხარ წევრი?(yes/no) ")

if student == "yes": student = True
else: student = False
if member == "yes": member = True
else: member = False

if student and member:
    print("გაქვს დამატებითი ფასდაკლება")
elif student or member:
    print("გაქვს ფასდაკლება")
else:
    print("ფასდაკლება არ გაქვს")


# N4


username = input("Username: ")

if 2 < len(username) < 21 and username.isalnum():
    print("username სწორია")
else:
    print("username არასწორია")