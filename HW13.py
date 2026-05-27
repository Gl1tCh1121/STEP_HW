import csv
import random
from faker import Faker
import os

# N1

def count_file_stats(filename="data.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            
            if not content:
                print("ფაილი ცარიელია.")
                return

            lines_count = len(content.splitlines())
            words_count = len(content.split())
            chars_count = len(content)

            print(f"სტრიქონები: {lines_count}")
            print(f"სიტყვები:   {words_count}")
            print(f"სიმბოლოები: {chars_count}")

    except FileNotFoundError:
        print(f"შეცდომა: ფაილი '{filename}' ვერ მოიძებნა.")
    except Exception as e:
        print(f"მოხდა გაუთვალისწინებელი შეცდომა: {e}")

count_file_stats()



# N2

def append_to_journal(filename="journal.txt"):
    print("ჩაწერეთ თქვენი ჟურნალის პოსტები (დასასრულებლად ჩაწერეთ 'exit'):")
    
    while True:
        entry = input("> ").strip()
        
        if entry.lower() == "exit":
            print("პროგრამა დასრულდა.")
            break
            
        if not entry:
            continue

        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(entry + "\n")
        except IOError:
            print("შეცდომა: ფაილში ჩაწერა ვერ მოხერხდა.")
        except Exception as e:
            print(f"მოხდა შეცდომა: {e}")

append_to_journal()



# N3




def filter_products_by_price(input_file="products.csv", output_file="filtered_products.csv"):
    try:
        min_price = float(input("შეიყვანეთ მინიმალური ფასი: "))
    except ValueError:
        print("შეცდომა: გთხოვთ შეიყვანოთ ვალიდური რიცხვი.")
        return

    try:
        with open(input_file, "r", encoding="utf-8", newline="") as infile:
            reader = csv.DictReader(infile)
            
            if "price" not in reader.fieldnames:
                print("შეცდომა: ფაილში სვეტი 'price' ვერ მოიძებნა.")
                return
            
            filtered_rows = []
            for row in reader:
                try:
                    if float(row["price"]) > min_price:
                        filtered_rows.append(row)
                except ValueError:
                    continue

        with open(output_file, "w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(filtered_rows)
            
        print(f"წარმატებით გაიფილტრა. შედეგი შენახულია '{output_file}'-ში. (ნაპოვნია {len(filtered_rows)} პროდუქტი)")

    except FileNotFoundError:
        print(f"შეცდომა: საწყისი ფაილი '{input_file}' ვერ მოიძებნა.")
    except Exception as e:
        print(f"მოხდა შეცდომა: {e}")

filter_products_by_price()


# N4

FILENAME = "contacts.csv"
FIELDNAMES = ["name", "phone", "email"]

def initialize_file():
    if not os.path.exists(FILENAME):
        try:
            with open(FILENAME, "w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
        except Exception as e:
            print(f"ფაილის ინიციალიზაციის შეცდომა: {e}")

def view_contacts():
    try:
        with open(FILENAME, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
            if not contacts:
                print("\nკონტაქტების სია ცარიელია.")
                return
            
            print("\n--- კონტაქტების სია ---")
            for idx, row in enumerate(contacts, 1):
                print(f"{idx}. სახელი: {row['name']}, ტელ: {row['phone']}, Email: {row['email']}")
    except FileNotFoundError:
        print("\nფაილი არ არსებობს. ჯერ დაამატეთ კონტაქტი.")

def add_contact():
    name = input("შეიყვანეთ სახელი: ").strip()
    phone = input("შეიყვანეთ ტელეფონი: ").strip()
    email = input("შეიყვანეთ ელ-ფოსტა: ").strip()
    
    if not name:
        print("შეცდომა: სახელი არ უნდა იყოს ცარიელი.")
        return

    try:
        with open(FILENAME, "a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writerow({"name": name, "phone": phone, "email": email})
        print("კონტაქტი წარმატებით დაემატა.")
    except Exception as e:
        print(f"ჩაწერის შეცდომა: {e}")

def search_contact():
    search_name = input("შეიყვანეთ საძიებო სახელი: ").strip().lower()
    found = False
    
    try:
        with open(FILENAME, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            print("\n--- ძებნის შედეგები ---")
            for row in reader:
                if search_name in row["name"].lower():
                    print(f"სახელი: {row['name']}, ტელ: {row['phone']}, Email: {row['email']}")
                    found = True
            if not found:
                print("კონტაქტი ამ სახელით ვერ მოიძებნა.")
    except FileNotFoundError:
        print("კონტაქტების ფაილი არ არსებობს.")

def delete_contact():
    delete_name = input("შეიყვანეთ წასაშლელი კონტაქტის ზუსტი სახელი: ").strip()
    updated_contacts = []
    found = False
    
    try:
        with open(FILENAME, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"].lower() == delete_name.lower():
                    found = True  
                else:
                    updated_contacts.append(row)
        
        if not found:
            print(f"შეტყობინება: კონტაქტი სახელით '{delete_name}' ვერ მოიძებნა.")
            return

        with open(FILENAME, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(updated_contacts)
        print(f"კონტაქტი '{delete_name}' წარმატებით წაიშალა.")
        
    except FileNotFoundError:
        print("კონტაქტების ფაილი არ არსებობს.")

def main_menu():
    initialize_file()
    while True:
        print("\n1. ყველა კონტაქტის ნახვა")
        print("2. კონტაქტის დამატება")
        print("3. კონტაქტის ძებნა სახელით")
        print("4. კონტაქტის წაშლა")
        print("5. გამოსვლა")
        
        choice = input("აირჩიეთ მოქმედება (1-5): ").strip()
        
        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("პროგრამა დასრულდა.")
            break
        else:
            print("არასწორი არჩევანი. სცადეთ თავიდან.")

if __name__ == "__main__":
    main_menu()



# N5

FILENAME = "students.csv"
SUBJECTS = ["python", "java", "ruby", "c"]
FIELDNAMES = ["name"] + SUBJECTS

def generate_student_data(filename=FILENAME, num_students=100):
    fake = Faker("ka_GE")
    
    try:
        with open(filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            
            for _ in range(num_students):
                row = {
                    "name": fake.name(),
                    "python": random.randint(0, 100),
                    "java": random.randint(0, 100),
                    "ruby": random.randint(0, 100),
                    "c": random.randint(0, 100)
                }
                writer.writerow(row)
        print(f"წარმატებით დაგენერირდა {num_students} სტუდენტის მონაცემები ფაილში: {filename}")
    except Exception as e:
        print(f"ფაილში ჩაწერისას მოხდა შეცდომა: {e}")

def calculate_statistics(filename=FILENAME):
    try:
        with open(filename, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            
            best_student = None
            max_average = -1
            
            leaders = {subject: {"name": "", "score": -1} for subject in SUBJECTS}
            
            for row in reader:
                name = row["name"]
                
                scores = {sub: int(row[sub]) for sub in SUBJECTS}
                
                avg_score = sum(scores.values()) / len(SUBJECTS)
                
                if avg_score > max_average:
                    max_average = avg_score
                    best_student = name
                    
                for subject in SUBJECTS:
                    if scores[subject] > leaders[subject]["score"]:
                        leaders[subject]["score"] = scores[subject]
                        leaders[subject]["name"] = name
            
            print("\n📊 სტატისტიკა:")
            print("-" * 50)
            if best_student:
                print(f"საუკეთესო სტუდენტი: {best_student} (საშუალო: {max_average:.2f})")
            
            print("\n🏆 ლიდერები საგნების მიხედვით:")
            for subject in SUBJECTS:
                sub_title = subject.capitalize() if len(subject) > 1 else subject.upper()
                print(f"  {sub_title:<8} {leaders[subject]['name']:<22} — {leaders[subject]['score']}")
                
    except FileNotFoundError:
        print(f"შეცდომა: ფაილი '{filename}' სტატისტიკისთვის ვერ მოიძებნა.")
    except Exception as e:
        print(f"სტატისტიკის დამუშავებისას მოხდა შეცდომა: {e}")

if __name__ == "__main__":
    generate_student_data() 
    calculate_statistics() 