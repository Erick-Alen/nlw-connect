from src.models.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Inscritos(Base):
    __tablename__ = "Inscritos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    link = Column(String)
    evento_id = Column(Integer, ForeignKey("Eventos.id"))

    def __init__(self, nome, email, evento_id):
        self.nome = nome
        self.email = email
        self.evento_id = evento_id

    def __repr__(self):
        return f"Inscritos({self.nome}, {self.email}, {self.evento_id})"
