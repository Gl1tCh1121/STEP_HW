import time


# N1

def check_positive(func):
    def wrapper(*args, **kwargs):
        for num in args:
            if isinstance(num, (int, float)) and num < 0:
                return "მხოლოდ დადებით რიცხვებზე ხდება მოქმედება"
        
        return func(*args, **kwargs)
    return wrapper

@check_positive
def calculate(*args, operation):
    result = 0
    if operation == "sum":
        result = sum(args)
    elif operation == "diff":
        result = args[0]
        for n in args[1:]:
            result -= n  
    elif operation == "max":
        result = max(args)
    elif operation == "min":
        result = min(args)
    elif operation == "mult":
        result = 1
        for n in args:
            result *= n
    elif operation == "div":
        result = args[0]
        for n in args[1:]:
            result /= n
    else:
        return "არასწორი ოპერაცია"

    return result

print("დავალება N1")
print()
print(calculate(5, 4, operation="mult"))  
print(calculate(5, -4, operation="mult"))
print()


# N2

def format(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        arguments = str(args[0])
        for n in args[1:]:
            arguments += f" და {n}"

        return (f"function called '{func.__name__}', with attributes {arguments}, returned {result}")
    return wrapper

@format
def multiply(*args):
    result = 1
    for n in args:
        result *= n
    return result
@format
def divide(*args):

    result = args[0]
    for n in args[1:]:
        result /= n
    return result

print("დავალება N2")
print()
print(multiply(15, 5))  
print(divide(15, 5))
print()


# N3 


def repeat(times, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
                if i < times - 1:
                    time.sleep(delay)
        return wrapper
    return decorator

@repeat(times=3, delay=3)
def hello_world():
    print("Hello World!")

print("დავალება N3")
print()
hello_world()
print()


# M4

current_user = {
    "username": "giorgi",
    "role": "user"  
}

def role_required(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):

            if current_user.get("role") in required_role:
                return func(*args, **kwargs)
            else:
                print("Permission denied!")

        return wrapper
    return decorator

@role_required(("admin", "user"))
def delete_user(user_id):
    print(f"User with id {user_id} has been deleted.")


@role_required(("admin", "editor"))
def edit_user(user_id):
    print(f"User with id {user_id} has been updated.")


@role_required(("admin", "user"))
def create_user(first_name):
    print(f"User {first_name} has been created.")


print("დავალება N4")
print()
delete_user(42)  
edit_user(42)    
create_user("Giorgi")