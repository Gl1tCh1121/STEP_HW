# N1

var_int = 5
print(type(var_int))

var_float = 5.5
print(type(var_float))

var_str = "five"
print(type(var_str))

var_bool = True
print(type(var_bool))


# N2

answer = int(input("Whats your birth year? "))
print(2025 - answer)


# N3
def numtype(num):
    def oddeven(num):
        if num % 2 == 0:
            return "Odd: False Even: True"
        return "Odd: True Even: False"
    
    if num == 0:
        return "Negative: False Positive: False Zero: True | Odd: False Even: False"
    elif num > 0:
        return f"Negative: False Positive: True Zero: False | {oddeven(num)}"
    else:
        return f"Negative: True Positive: False Zero: False | {oddeven(num)}"


answer2 = int(input("Write random number: "))
print(numtype(answer2))


