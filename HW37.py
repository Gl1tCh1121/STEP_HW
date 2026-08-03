from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# 1. Engine Creation
DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"
engine = create_engine(DATABASE_URL)


# 2. Base Class Creation
class Base(DeclarativeBase):
    pass


# 3. Book Model Definition
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(255))
    publish_year: Mapped[int]


# 4. Table Creation
Base.metadata.create_all(engine)

# 5. Session Setup
Session = sessionmaker(bind=engine)
session = Session()

# 6. Data Insertion
books = [
    Book(title="To Kill a Mockingbird", author="Harper Lee", publish_year=1960),
    Book(
        title="The Go-Programming Language",
        author="Alan Donovan",
        publish_year=2015,
    ),
    Book(title="Designing Data-Intensive Applications", author="Martin Kleppmann", publish_year=2017),
    Book(title="Clean Code", author="Robert C. Martin", publish_year=2008),
    Book(title="Atomic Habits", author="James Clear", publish_year=2018),
]

session.add_all(books)
session.commit()

# 7. SELECT Operations
# Fetch all books
all_books = session.scalars(select(Book)).all()

# Fetch one book by ID
book_by_id = session.get(Book, 1)

# Fetch books published after 2015
recent_books = session.scalars(
    select(Book).where(Book.publish_year > 2015)
).all()

# 8. UPDATE
book_to_update = session.get(Book, 1)
if book_to_update:
    book_to_update.author = "Nelle Harper Lee"
    session.commit()

# 9. DELETE
book_to_delete = session.get(Book, 2)
if book_to_delete:
    session.delete(book_to_delete)
    session.commit()

# 10. Session Close
session.close()