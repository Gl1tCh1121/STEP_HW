# N1

list1 = [1,1,2,2,3,3,4,4,5,7,7,8,8,8,9,9,9,9]

dict1 = {}

for n in list1:
    if n not in dict1:
        dict1[n] = 1
    else:
        dict1[n] = dict1[n] + 1 


print(dict1)

print()



# N2

dict2 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

dict2_2 = {
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
}

merged = {}

for key in dict2 | dict2_2:
    if key in dict2 and key in dict2_2:
        merged[key] = [dict2[key], dict2_2[key]]

    elif key in dict2:
        merged[key] = dict2[key]
    else:
        merged[key] = dict2_2[key]


print(merged)

print()



# N3 

dict3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4 }

reversed = {}

for key in dict3:
    reversed[dict3[key]] = key

print(reversed)


# N4 

films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}


print(f"საერთო ფილმები: {list(films1 & films2)}")
print(f"ფილმები, რომლებიც უყვარს მხოლოდ პირველ ადამიანს: {list(films1 - films2)}")
print(f"ფილმები, რომლებიც უყვარს მხოლოდ მეორე ადამიანს: {list(films2 - films1)}")
print(f"ყველა უნიკალური ფილმი: {list(films1 ^ films2)}")


print()



# N5 


info = {
    "კლასი 10A": {
        "გიორგი": {
            "ასაკი": 16,
            "საშუალო_ქულა": 8.7,
            "საგნები": {
                "მათემატიკა": {"ქულა": 9, "გამოცდა": True},
                "ფიზიკა": {"ქულა": 8, "გამოცდა": False},
                "ისტორია": {"ქულა": 9, "გამოცდა": True},
                "ინგლისური": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 92,
            "დამატებითი": ["ფეხბურთი", "პროგრამირება"]
        },
        "ანა": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.4,
            "საგნები": {
                "მათემატიკა": {"ქულა": 10, "გამოცდა": True},
                "ფიზიკა": {"ქულა": 9, "გამოცდა": True},
                "ისტორია": {"ქულა": 8, "გამოცდა": False},
                "ინგლისური": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 98,
            "დამატებითი": ["ცეკვა"]
        },
        "დავით": {
            "ასაკი": 16,
            "საშუალო_ქულა": 7.2,
            "საგნები": {
                "მათემატიკა": {"ქულა": 6, "გამოცდა": False},
                "ფიზიკა": {"ქულა": 7, "გამოცდა": True},
                "ისტორია": {"ქულა": 8, "გამოცდა": True},
                "ინგლისური": {"ქულა": 9, "გამოცდა": False}
            },
            "დასწრება": 75,
            "დამატებითი": ["კალათბურთი", "პროგრამირება"]
        }
    },

    "კლასი 10B": {
        "მარიამ": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.1,
            "საგნები": {
                "მათემატიკა": {"ქულა": 9, "გამოცდა": True},
                "ბიოლოგია": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 95,
            "დამატებითი": ["მუსიკა", "ხატვა"]
        },
        "ლევან": {
            "ასაკი": 16,
            "საშუალო_ქულა": 6.8,
            "საგნები": {
                "მათემატიკა": {"ქულა": 5, "გამოცდა": False},
                "ფიზიკა": {"ქულა": 7, "გამოცდა": False}
            },
            "დასწრება": 60,
            "დამატებითი": []
        }
    }
}

print()
print("1.")
print()
for key in info:
    for name in info[key]:
        print(f"სახელი: {name}, საშუალო ქულა: {info[key][name]['საშუალო_ქულა']}")

print()
print("2.")
print()

best_student = ""
score = 0
for key in info:
    for name in info[key]:
        if info[key][name]['საშუალო_ქულა'] > score:
            best_student = name
            score = info[key][name]['საშუალო_ქულა']

print(best_student)

print()
print("3.")
print()

student_list = []

for key in info:
    for name in info[key]:
        if info[key][name]['დასწრება'] > 90:
            student_list.append(name)

print(student_list)            
      
print()
print("4.")
print()

most_students = ""
most_students_count = 0

for key in info:
    if len(info[key]) > most_students_count:
        most_students = key

print(most_students)

print()
print("5.")
print()

programming_list = []

for key in info:
    for name in info[key]:
        if "პროგრამირება" in info[key][name]['დამატებითი']:
            programming_list.append(name)

print(programming_list)

print()
print("6.")
print()

avg = 0
cnt = 0

for key in info:
    for name in info[key]:
        avg += info[key][name]['დასწრება']
        cnt += 1 

print(avg/cnt)

print()
print("7.")
print()

new_dict = {}

for key in info:
    for name in info[key]:
        new_dict[name] = len(info[key][name]['საგნები'])

print(new_dict)

print()
print("8.")
print()

monst_acitve = []
monst_acitve_cnt = 0

for key in info:
    for name in info[key]:
        if len(info[key][name]['დამატებითი']) > monst_acitve_cnt:
            monst_acitve.clear()
            monst_acitve_cnt = len(info[key][name]['დამატებითი'])
            monst_acitve.append(name)
        elif len(info[key][name]['დამატებითი']) == monst_acitve_cnt:
            monst_acitve.append(name)

print(monst_acitve)