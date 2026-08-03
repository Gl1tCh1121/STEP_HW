from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload

# 5. ბაზის ინიციალიზაცია (SQLite)
Base = declarative_base()
engine = create_engine('sqlite:///online_shop.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Customer Model
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    orders = relationship("Order", back_populates="customer")

# 2. Order Model
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")

# 3. Product Model
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    order_items = relationship("OrderItem", back_populates="product")

# 4. OrderItem Model
class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, default=1)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

# 5. ცხრილების შექმნა
Base.metadata.create_all(engine)

# 6. მონაცემების დამატება (Customers & Products)
c1 = Customer(name="John", email="john@gmail.com")
c2 = Customer(name="Anna", email="anna@gmail.com")
c3 = Customer(name="Kate", email="kate@gmail.com")
c4 = Customer(name="Bob", email="bob@gmail.com")
c5 = Customer(name="Patrick", email="patrick@gmail.com")

p1 = Product(name="Laptop", price=1000)
p2 = Product(name="Phone", price=800)
p3 = Product(name="Keyboard", price=50)
p4 = Product(name="Mouse", price=25)
p5 = Product(name="Monitor", price=300)
p6 = Product(name="Headphones", price=100)
p7 = Product(name="Tablet", price=400)
p8 = Product(name="Camera", price=600)

session.add_all([c1, c2, c3, c4, c5, p1, p2, p3, p4, p5, p6, p7, p8])
session.commit()

# 7. & 8. შეკვეთების და პროდუქტების დამატება
o1 = Order(customer=c1)
o2 = Order(customer=c1)
o3 = Order(customer=c2)
o4 = Order(customer=c3)
o5 = Order(customer=c4)

session.add_all([o1, o2, o3, o4, o5])
session.commit()

items = [
    OrderItem(order=o1, product=p1, quantity=1),  # Laptop
    OrderItem(order=o1, product=p4, quantity=2),  # Mouse
    OrderItem(order=o2, product=p2, quantity=1),  # Phone
    OrderItem(order=o2, product=p6, quantity=1),  # Headphones
    OrderItem(order=o3, product=p3, quantity=1),  # Keyboard
    OrderItem(order=o4, product=p5, quantity=1),  # Monitor
    OrderItem(order=o5, product=p7, quantity=1),  # Tablet
]

session.add_all(items)
session.commit()

# 9. SELECT ოპერაციები

# 9.1 ყველა მომხმარებელი
print("--- 1. ყველა მომხმარებელი ---")
customers = session.query(Customer).all()
for customer in customers:
    print(f"ID: {customer.id}\nName: {customer.name}\nEmail: {customer.email}\n")

# 9.2 კონკრეტული მომხმარებლის (John) ყველა შეკვეთა (joinedload-ით)
print("--- 2. John-ის შეკვეთები ---")
john = session.query(Customer).options(joinedload(Customer.orders)).filter_by(name="John").first()
print(f"Customer: {john.name}\n")
for order in john.orders:
    print(f"Order ID: {order.id}")
    print(f"Order Date: {order.order_date.strftime('%Y-%m-%d %H:%M:%S')}\n")

# 9.3 კონკრეტული შეკვეთის (Order 1) ყველა პროდუქტი
print("--- 3. Order ID: 1-ის პროდუქტები ---")
order_1 = session.query(Order).filter_by(id=1).first()
print(f"Order ID: {order_1.id}\n")
for item in order_1.order_items:
    print(f"{item.product.name}")
    print(f"Quantity: {item.quantity}\n")

# 10. ახალი შეკვეთის დამატება ORM ურთიერთობებით
print("--- 10. ახალი შეკვეთის დამატება ---")
new_order = Order(
    customer=c5,  # Patrick
    order_items=[
        OrderItem(product=p3, quantity=1),  # Keyboard
        OrderItem(product=p4, quantity=1),  # Mouse
        OrderItem(product=p8, quantity=1)   # Camera
    ]
)
session.add(new_order)
session.commit()
print(f"ახალი შეკვეთა წარმატებით დაემატა ID: {new_order.id}-ით!\n")

# 11. UPDATE - პროდუქტის ფასის შეცვლა
print("--- 11. პროდუქტის ფასის განახლება ---")
laptop = session.query(Product).filter_by(name="Laptop").first()
print(f"Laptop\nOld price: {laptop.price}")

laptop.price = 1200
session.commit()

print(f"New price: {laptop.price}")

# სესიის დახურვა
session.close()