# N1 

def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:

        print("Error: There is no item with this index")

    except TypeError:

        print("Error: Index must be an integer")



# N2

def safe_get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Error: Key '{key}' doesn't exist")
        return None


# N3

try:
    user_input = input("Enter a number: ")
    number = float(user_input)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"The square of {number} is {number ** 2}")
    
finally:
    print("ოპერაცია დასრულებულია")