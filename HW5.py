# N1

list1 = [2, 3, 4, 5, 6, 7]
sum_num = 0

for n in list1:
    sum_num += n


print("დავალება 1: ")
print()
print(sum_num)
print()
print()



# N2


list2 = [2, 3, 4, 5, 6, 7]
min_num = list2[0]
max_num = list2[0]

for n in list2:
    if min_num > n: min_num = n
    if max_num < n: max_num = n


print("დავალება 2: ")
print()
print(min_num)
print(max_num)
print()
print()


# N3 


list3 = [2, 3, 4, 5, 6, 7, 9, 11, 0]

odd_list = []
even_list = []

for n in list3:
    if n % 2 == 0: even_list.append(n)
    else: odd_list.append(n)


print("დავალება 3: ")
print()
print(odd_list)
print(even_list)
print()
print()



# N4

list4 = ["Hello", "world"]

my_tuple = tuple(list4)


print("დავალება 4: ")
print()
print(list4)
print(my_tuple)
print()
print()



# N4 მეორე გზა 

my_tuple2 = (*list4,)

print("დავალება 4 მეორე გზა: ")
print()
print(list4)
print(my_tuple2)
print()
print()

# N5 

list5 = [2, 3, 4, 4, 6, 6, 9, 9, 2]

unique_list = list(set(list5))


print("დავალება 5: ")
print()
print(list5)
print(unique_list)
print()
print()


# N5 მეორე გზა


my_unique_list = []

for n in list5:
    if n not in my_unique_list: my_unique_list.append(n)


print("დავალება 5 მეორე გზა: ")
print()
print(list5)
print(my_unique_list)
print()
print()