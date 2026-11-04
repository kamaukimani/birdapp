from app.db import db 
from sqlalchemy_serializer import SerializerMixin 
from sqlalchemy.orm import Mapped,mapped_column 

class Bird(db.Model,SerializerMixin):
    __tablename__="birds"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    species:Mapped[str]
    image:Mapped[str]

    def __repr__(self):
        return f'<Bird {self.name} | Species: {self.species}>'
