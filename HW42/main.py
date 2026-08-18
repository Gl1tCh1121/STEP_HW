from typing import List

from database import get_db
from fastapi import Depends, FastAPI, HTTPException, status
from models import Trip
from schemas import TripCreate, TripResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

app = FastAPI()


@app.post(
    "/trips", response_model=TripResponse, status_code=status.HTTP_201_CREATED
)
def create_trip(trip_in: TripCreate, db: Session = Depends(get_db)):
    db_trip = Trip(**trip_in.model_dump())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip


@app.get("/trips", response_model=List[TripResponse])
def get_trips(db: Session = Depends(get_db)):
    return db.scalars(select(Trip)).all()


@app.get("/trips/{trip_id}", response_model=TripResponse)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.scalar(select(Trip).where(Trip.id == trip_id))
    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found"
        )
    return trip


@app.put("/trips/{trip_id}", response_model=TripResponse)
def update_trip(
    trip_id: int, trip_in: TripCreate, db: Session = Depends(get_db)
):
    trip = db.scalar(select(Trip).where(Trip.id == trip_id))
    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found"
        )

    for key, value in trip_in.model_dump().items():
        setattr(trip, key, value)

    db.commit()
    db.refresh(trip)
    return trip


@app.delete("/trips/{trip_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.scalar(select(Trip).where(Trip.id == trip_id))
    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Trip not found"
        )

    db.delete(trip)
    db.commit()
    return None