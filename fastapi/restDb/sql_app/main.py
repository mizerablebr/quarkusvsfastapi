from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/person/", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_name(db, name=person.name)
    if db_person:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_person(db=db, person=person)


@app.get("/person/", response_model=List[schemas.Person])
def read_people(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    people = crud.get_people(db, skip=skip, limit=limit)
    return people


@app.get("/person/{person_name}", response_model=schemas.Person)
def read_person_by_name(person_name: str, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_name(db, name=person_name)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person
