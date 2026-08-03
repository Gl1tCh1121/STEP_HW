from typing import Generator, List
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Boolean, Column, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# Database Setup
DATABASE_URL = "sqlite:///./trips.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


# SQLAlchemy Model
class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String(100), nullable=False)
    country = Column(String(50), nullable=False)
    days = Column(Integer, nullable=False)
    budget = Column(Integer, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)


Base.metadata.create_all(bind=engine)


# Pydantic Schemas
class TripCreate(BaseModel):
    destination: str
    country: str
    days: int
    budget: int
    is_completed: bool = False


class TripResponse(TripCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


# Dependency
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


# 1. Create Trip
@app.post(
    "/trips", response_model=TripResponse, status_code=status.HTTP_201_CREATED
)
def create_trip(trip: TripCreate, db: Session = Depends(get_db)):
    db_trip = Trip(**trip.model_dump())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip


# 2. Get All Trips
@app.get("/trips", response_model=List[TripResponse])
def get_trips(db: Session = Depends(get_db)):
    stmt = select(Trip)
    return db.scalars(stmt).all()


# 3. Get Trip by ID
@app.get("/trips/{trip_id}", response_model=TripResponse)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    stmt = select(Trip).where(Trip.id == trip_id)
    trip = db.scalar(stmt)
    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found"
        )
    return trip


# 4. Update Trip
@app.put("/trips/{trip_id}", response_model=TripResponse)
def update_trip(
    trip_id: int, updated_trip: TripCreate, db: Session = Depends(get_db)
):
    stmt = select(Trip).where(Trip.id == trip_id)
    db_trip = db.scalar(stmt)
    if not db_trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found"
        )

    for key, value in updated_trip.model_dump().items():
        setattr(db_trip, key, value)

    db.commit()
    db.refresh(db_trip)
    return db_trip


# 5. Delete Trip
@app.delete("/trips/{trip_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    stmt = select(Trip).where(Trip.id == trip_id)
    db_trip = db.scalar(stmt)
    if not db_trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found"
        )

    db.delete(db_trip)
    db.commit()
    return None