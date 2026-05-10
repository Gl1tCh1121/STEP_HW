# N1

def find_min_max(*args):
    return min(args), max(args)


result = find_min_max(2, 5, 8, 7, 3, 25, 16)

print()
print("დავალება 1")
print()
print(result)
print()


# N2 

def calculate(*args, operation):
    summ = 0
    if operation == "sum":
        for n in args:
            summ += n
    elif operation == "max":
        summ = max(args)
    elif operation == "min":
        summ = min(args)
    else:
        summ = 1
        for n in args:
            summ *= n

    return summ

print()
print("დავალება 2")
print()
result2 = calculate(2, 5, 8, 7, 3, 25, 16, operation="sum")
print(result2)
print()


# N3

def format_user(first_name, last_name, **kwargs):

    return f"{first_name} {last_name} | age: {kwargs['age']}, job: {kwargs['job']} "


result3 = format_user("John", "Doe", age=25, job="Developer")
print()
print("დავალება 3")
print()
print(result3)
print()


# N4


def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return (a//b, a%b)



result4 = safe_divide(10, 2)
print()
print("დავალება 4")
print()
print(result4)
print()
