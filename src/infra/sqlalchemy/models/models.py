from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.models.config.database import Base


class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    detalhes = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    disponivel = Column(Boolean, default=False)
