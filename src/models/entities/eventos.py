from src.models.configs.base import Base
from sqlalchemy import Column, String, Integer
class Eventos(Base):
    __tablename__ = 'eventos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    descricao = Column(String)
    data = Column(String)
    local = Column(String)
    def __init__(self, nome, descricao, data, local):
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.local = local
    def __repr__(self):
        return f'Eventos({self.nome}, {self.descricao}, {self.data}, {self.local})'
