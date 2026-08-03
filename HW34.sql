-- ============================================================
-- საშინაო დავალება — ბიბლიოთეკის მონაცემთა ბაზა (PostgreSQL)
-- ============================================================

-- ------------------------------------------------------------
-- 1. ცხრილის შექმნა (CREATE TABLE)
-- ------------------------------------------------------------
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    publish_year INTEGER,
    pages INTEGER,
    price NUMERIC(8, 2)
);

-- ------------------------------------------------------------
-- 2. მინიმუმ 15 ჩანაწერის დამატება (INSERT INTO)
-- ------------------------------------------------------------
INSERT INTO books (title, author, genre, publish_year, pages, price) VALUES
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937, 310, 35.00),
('Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 'Fantasy', 1997, 223, 28.50),
('1984', 'George Orwell', 'Dystopian', 1949, 328, 22.00),
('Dune', 'Frank Herbert', 'Sci-Fi', 1965, 412, 45.00),
('Project Hail Mary', 'Andy Weir', 'Sci-Fi', 2021, 496, 38.00),
('Klara and the Sun', 'Kazuo Ishiguro', 'Sci-Fi', 2021, 320, 32.00),
('The Midnight Library', 'Matt Haig', 'Fantasy', 2020, 304, 29.00),
('Atomic Habits', 'James Clear', 'Self-Help', 2018, 320, 40.00),
('To Kill a Mockingbird', 'Harper Lee', 'Classic', 1960, 281, 18.00),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 1925, 180, 15.00),
('The Silent Patient', 'Alex Michaelides', 'Thriller', 2019, 336, 27.00),
('Babel', 'R.F. Kuang', 'Fantasy', 2022, 544, 42.00),
('Tomorrow, and Tomorrow, and Tomorrow', 'Gabrielle Zevin', 'Fiction', 2022, 416, 34.00),
('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 'History', 2011, 443, 36.00),
('The Alchemist', 'Paulo Coelho', 'Fiction', 1988, 208, 19.50);

-- ------------------------------------------------------------
-- 3. SELECT მოთხოვნები
-- ------------------------------------------------------------

-- 3.1 ყველა წიგნი
SELECT * FROM books;

-- 3.2 მხოლოდ წიგნის დასახელება და ავტორი
SELECT title, author FROM books;

-- 3.3 ყველა წიგნი, რომლის ფასი 30 ლარზე მეტია
SELECT * FROM books WHERE price > 30;

-- 3.4 ყველა წიგნი, რომლის გამოცემის წელი არის 2020 ან უფრო ახალი
SELECT * FROM books WHERE publish_year >= 2020;

-- 3.5 ყველა წიგნი, რომლის ჟანრია "Fantasy"
SELECT * FROM books WHERE genre = 'Fantasy';

-- 3.6 ყველა წიგნი, რომლის გვერდების რაოდენობა 300-ზე მეტია
SELECT * FROM books WHERE pages > 300;

-- 3.7 ყველა წიგნი, რომელიც დალაგებულია ფასის ზრდადობით
SELECT * FROM books ORDER BY price ASC;

-- 3.8 ყველა წიგნი, რომელიც დალაგებულია გამოცემის წლის კლებადობით
SELECT * FROM books ORDER BY publish_year DESC;

-- ------------------------------------------------------------
-- 4. მონაცემების განახლება (UPDATE)
-- ------------------------------------------------------------

-- 4.1 ერთ-ერთი წიგნის ფასის შეცვლა
UPDATE books SET price = 25.00 WHERE id = 1;

-- 4.2 ერთ-ერთი წიგნის ჟანრის შეცვლა
UPDATE books SET genre = 'Epic Fantasy' WHERE id = 2;

-- 4.3 ერთ-ერთი წიგნის გვერდების რაოდენობის შეცვლა
UPDATE books SET pages = 350 WHERE id = 3;

-- ------------------------------------------------------------
-- 5. მონაცემების წაშლა (DELETE)
-- ------------------------------------------------------------

-- 5.1 ერთი კონკრეტული წიგნის წაშლა
DELETE FROM books WHERE id = 10;

-- 5.2 ყველა წიგნი, რომლის გამოცემის წელი 2000-ზე ნაკლებია
DELETE FROM books WHERE publish_year < 2000;

-- ------------------------------------------------------------
-- 6. დამატებითი მონაცემები (DELETE-ის შემდეგ კიდევ 5 წიგნი)
-- ------------------------------------------------------------
INSERT INTO books (title, author, genre, publish_year, pages, price) VALUES
('Fourth Wing', 'Rebecca Yarros', 'Fantasy', 2023, 528, 44.00),
('Yellowface', 'R.F. Kuang', 'Fiction', 2023, 320, 31.00),
('Demon Copperhead', 'Barbara Kingsolver', 'Fiction', 2022, 560, 39.00),
('Sea of Tranquility', 'Emily St. John Mandel', 'Sci-Fi', 2022, 272, 26.00),
('Iron Flame', 'Rebecca Yarros', 'Fantasy', 2023, 624, 48.00);

-- ------------------------------------------------------------
-- 7. საბოლოო შემოწმება (დარჩენილი ყველა ჩანაწერი)
-- ------------------------------------------------------------
SELECT * FROM books;

-- ------------------------------------------------------------
-- 8. ცხრილის წაშლა (გაუშვით მხოლოდ ბოლოს!)
-- ------------------------------------------------------------
DROP TABLE books;