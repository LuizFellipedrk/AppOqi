from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models.config.database import get_db
from src.infra.sqlalchemy.models.schemas.schema import Produto
from src.infra.sqlalchemy.models.repositorios.produto import RepositorioProduto

app = FastAPI()


@app.post("/produtos")
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto().criar(produto)
    return produto_criado


@app.get("/produtos")
def listar_produtos():
    return {"Msg": "Listagem de Produtos"}
