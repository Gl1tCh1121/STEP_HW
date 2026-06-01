# N1


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        return f"გამარჯობა, მე ვარ {self.first_name} {self.last_name}."

class Student(Person):
    def introduce(self):
        return f"სალამი! მე ვარ სტუდენტი {self.first_name} {self.last_name}."

class Lecturer(Person):
    def introduce(self):
        return f"მოგესალმებით, მე გახლავართ ლექტორი {self.first_name} {self.last_name}."
    


# N2

class Profile:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            return "პაროლი წარმატებით შეიცვალა."
        return "შეცდომა: ძველი პაროლი არასწორია!"
    


# N3



class Product:
    def __init__(self, name, price):
        self.name = name
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("შეცდომა: ფასი არ შეიძლება იყოს უარყოფითი!")
        self.__price = price  




# N4


class CreditCardPayment:
    def pay(self, amount):
        print(f"გადახდილია {amount} ლარი საკრედიტო ბარათით.")

class PayPalPayment:
    def pay(self, amount):
        print(f"გადახდილია {amount} ლარი PayPal-ის საშუალებით.")

class CryptoPayment:
    def pay(self, amount):
        print(f"გადახდილია {amount} ლარი კრიპტოვალუტით.")


# N5


class Car:
    total_cars = 0  # Class variable

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1  # რაოდენობის გაზრდა ყოველი ობიექტის შექმნისას

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars