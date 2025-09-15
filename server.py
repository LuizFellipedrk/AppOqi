from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.models.config.database import get_db, criar_bd
from src.infra.sqlalchemy.models.schemas.schema import Produto
from src.infra.sqlalchemy.models.repositorios.produto import RepositorioProduto

criar_bd()
app = FastAPI()


@app.post("/produtos", response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get("/produtos", response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos
