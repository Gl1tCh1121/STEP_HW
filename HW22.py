import json
import os
from dataclasses import asdict, dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    available: bool = True


def save_books(books):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump([asdict(b) for b in books], f, ensure_ascii=False, indent=2)


def load_books():
    if os.path.exists("books.json"):
        with open("books.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book(**item) for item in data]
    return []


def add_book(books):
    title = input("შეიყვანე სახელი: ").strip()
    author = input("შეიყვანე ავტორი: ").strip()
    try:
        year = int(input("შეიყვანე წელი: "))
    except ValueError:
        print("❌ შეცდომა: წელი უნდა იყოს რიცხვი!")
        return

    new_id = max((b.id for b in books), default=0) + 1
    books.append(Book(id=new_id, title=title, author=author, year=year))
    print("✅ წიგნი დაემატა!")


def show_books(books):
    if not books:
        print("ბიბლიოთეკა ცარიელია.")
        return
    for b in books:
        status = "ხელმისაწვდომი" if b.available else "გაცემული"
        print(f"ID: {b.id} | {b.title} | {b.author} | {b.year} | {status}")


def search_books(books):
    query = input("შეიყვანე საძიებო სიტყვა: ").strip().lower()
    found = [b for b in books if query in b.title.lower()]
    if found:
        show_books(found)
    else:
        print("წიგნი ვერ მოიძებნა.")


def rent_book(books):
    try:
        book_id = int(input("შეიყვანე წიგნის ID: "))
    except ValueError:
        print("❌ შეცდომა: ID უნდა იყოს რიცხვი!")
        return

    for b in books:
        if b.id == book_id:
            if b.available:
                b.available = False
                print("✅ წიგნი წარმატებით გაიცა!")
            else:
                print("❌ წიგნი უკვე გაცემულია!")
            return
    print("❌ წიგნი ამ ID-ით ვერ მოიძებნა.")


def return_book(books):
    try:
        book_id = int(input("შეიყვანე წიგნის ID: "))
    except ValueError:
        print("❌ შეცდომა: ID უნდა იყოს რიცხვი!")
        return

    for b in books:
        if b.id == book_id:
            if not b.available:
                b.available = True
                print("✅ წიგნი წარმატებით დაბრუნდა!")
            else:
                print("❌ ეს წიგნი უკვე ბიბლიოთეკაშია!")
            return
    print("❌ წიგნი ამ ID-ით ვერ მოიძებნა.")


def show_stats(books):
    total = len(books)
    available = sum(1 for b in books if b.available)
    rented = total - available
    print(f"სულ წიგნები:   {total}")
    print(f"ხელმისაწვდომი:  {available}")
    print(f"გაცემული:       {rented}")


def main():
    books = load_books()

    while True:
        print("\n--- ბიბლიოთეკის მენიუ ---")
        print("1. წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა სახელით")
        print("4. წიგნის გატანა")
        print("5. წიგნის დაბრუნება")
        print("6. სტატისტიკა")
        print("7. მონაცემების შენახვა")
        print("8. გამოსვლა")

        choice = input("აირჩიე მოქმედება (1-8): ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            show_books(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            rent_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            show_stats(books)
        elif choice == "7":
            save_books(books)
            print("💾 მონაცემები შენახულია!")
        elif choice == "8":
            save_books(books)
            print("ნახვამდის!")
            break
        else:
            print("❌ არასწორი არჩევანი!")


if __name__ == "__main__":
    main()