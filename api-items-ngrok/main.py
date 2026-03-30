from datetime import datetime
from typing import List

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# URL de la base de datos SQLite
DATABASE_URL = "sqlite:///./items.db"
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de tabla en la base de datos
class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


# Crear la tabla si no existe
Base.metadata.create_all(bind=engine)


# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ItemCreate(BaseModel):
    name: str
    price: float

class ItemRead(BaseModel):
    id: int
    name: str
    price: float
    created_at: datetime

    class Config:
        orm_mode = True

app = FastAPI()


# Endpoint POST que permita agregar una o más filas a la tabla.
@app.post("/items/", response_model=List[ItemRead])
def create_items(
    items: List[ItemCreate], 
    db: Session = Depends(get_db),
):
    db_items = []
    for item in items:
        db_item = ItemDB(
            name=item.name,
            price=item.price,
            created_at=datetime.utcnow(),
        )
        db.add(db_item)
        db_items.append(db_item)

    db.commit()

    for db_item in db_items:
        db.refresh(db_item)

    return db_items


# Endpoint GET que permita leer los datos de la tabla.
@app.get("/items/", response_model=List[ItemRead])
def read_items(db: Session = Depends(get_db)):
    items = db.query(ItemDB).all()
    return items

