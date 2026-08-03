-- ==========================================
-- 1. მონაცემთა ბაზის სტრუქტურა (ნორმალიზაცია 3NF)
-- ==========================================

-- 1.1 Customers (მომხმარებლები)
CREATE TABLE Customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100)
);

-- 1.2 Categories (კატეგორიები)
CREATE TABLE Categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- 1.3 Products (პროდუქტები)
CREATE TABLE Products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category_id INT,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);

-- 1.4 Orders (შეკვეთები)
CREATE TABLE Orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

-- 1.5 OrderItems (შეკვეთის დეტალები/პროდუქტები რაოდენობით)
CREATE TABLE OrderItems (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);


-- ==========================================
-- 2. მონაცემების შევსება (INSERT DATA)
-- ==========================================

INSERT INTO Customers (id, name, phone, email) VALUES
(1, 'გიორგი ბერიძე', '555111111', 'giorgi@mail.com'),
(2, 'ნინო კაპანაძე', '555222222', 'nino@mail.com'),
(3, 'ლევან გელაშვილი', '555333333', 'levan@mail.com');

INSERT INTO Categories (id, name) VALUES
(1, 'Electronics'),
(2, 'Furniture');

INSERT INTO Products (id, name, category_id, price) VALUES
(1, 'Laptop', 1, 3200.00),
(2, 'Mouse', 1, 80.00),
(3, 'Keyboard', 1, 150.00),
(4, 'Chair', 2, 420.00),
(5, 'Desk', 2, 850.00),
(6, 'Monitor', 1, 900.00);

INSERT INTO Orders (id, customer_id, order_date) VALUES
(1, 1, '2026-06-01'),
(2, 2, '2026-06-03'),
(3, 3, '2026-06-05'),
(4, 1, '2026-06-10');

INSERT INTO OrderItems (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(3, 4, 4),
(3, 5, 1),
(4, 6, 2);


-- ==========================================
-- 3. JOIN მოთხოვნები (QUERIES)
-- ==========================================

-- 1. შეკვეთების სრული ინფორმაცია
SELECT 
    o.id AS OrderID,
    c.name AS CustomerName,
    c.email AS Email,
    p.name AS ProductName,
    p.price AS Price,
    oi.quantity AS Quantity,
    o.order_date AS OrderDate
FROM Orders o
JOIN Customers c ON o.customer_id = c.id
JOIN OrderItems oi ON o.id = oi.order_id
JOIN Products p ON oi.product_id = p.id;

-- 2. მომხმარებლების და მათი პროდუქტების სია
SELECT DISTINCT 
    c.name AS CustomerName,
    p.name AS ProductName
FROM Customers c
JOIN Orders o ON c.id = o.customer_id
JOIN OrderItems oi ON o.id = oi.order_id
JOIN Products p ON oi.product_id = p.id;

-- 3. პროდუქტების სია და მათი მყიდველები
SELECT 
    p.name AS ProductName,
    p.price AS Price,
    c.name AS CustomerName
FROM Products p
JOIN OrderItems oi ON p.id = oi.product_id
JOIN Orders o ON oi.order_id = o.id
JOIN Customers c ON o.customer_id = c.id;

-- 4. შეკვეთის დეტალები
SELECT 
    o.id AS OrderID,
    c.name AS CustomerName,
    p.name AS ProductName,
    oi.quantity AS Quantity,
    o.order_date AS OrderDate
FROM Orders o
JOIN Customers c ON o.customer_id = c.id
JOIN OrderItems oi ON o.id = oi.order_id
JOIN Products p ON oi.product_id = p.id;

-- 5. პროდუქტი და მისი კატეგორია
SELECT 
    p.name AS ProductName,
    cat.name AS Category
FROM Products p
JOIN Categories cat ON p.category_id = cat.id;

-- 6. Electronics კატეგორიის პროდუქტები
SELECT 
    p.name AS ProductName,
    cat.name AS Category,
    p.price AS Price
FROM Products p
JOIN Categories cat ON p.category_id = cat.id
WHERE cat.name = 'Electronics';

-- 7. კონკრეტული მომხმარებლის შეკვეთები (გიორგი ბერიძე)
SELECT 
    o.id AS OrderID,
    c.name AS CustomerName,
    p.name AS ProductName,
    oi.quantity AS Quantity
FROM Orders o
JOIN Customers c ON o.customer_id = c.id
JOIN OrderItems oi ON o.id = oi.order_id
JOIN Products p ON oi.product_id = p.id
WHERE c.name = 'გიორგი ბერიძე';

-- 8. კონკრეტულ დღეს გაკეთებული შეკვეთები (2026-06-05)
SELECT 
    o.order_date AS OrderDate,
    c.name AS CustomerName,
    p.name AS ProductName,
    oi.quantity AS Quantity
FROM Orders o
JOIN Customers c ON o.customer_id = c.id
JOIN OrderItems oi ON o.id = oi.order_id
JOIN Products p ON oi.product_id = p.id
WHERE o.order_date = '2026-06-05';

-- 9. მომხმარებლების სრული შესყიდვების ისტორია
SELECT 
    c.name AS CustomerName,
    c.email AS Email,
    p.name AS ProductName,
    oi.quantity AS Quantity
FROM Customers c
JOIN Orders o ON c.id = o.customer_id
JOIN OrderItems oi ON o.id = oi.order_id
JOIN Products p ON oi.product_id = p.id;

-- 10. პროდუქტები, რომლებიც ერთზე მეტი რაოდენობით არის შეძენილი
SELECT 
    c.name AS CustomerName,
    p.name AS ProductName,
    oi.quantity AS Quantity
FROM OrderItems oi
JOIN Orders o ON oi.order_id = o.id
JOIN Customers c ON o.customer_id = c.id
JOIN Products p ON oi.product_id = p.id
WHERE oi.quantity > 1;