from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models.models import Produto as ProdutoModel
from src.infra.sqlalchemy.models.schemas.schema import Produto as ProdutoSchema


class RepositorioProduto:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: ProdutoSchema):
        db_produto = ProdutoModel(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel,
        )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        return self.db.query(ProdutoModel).all()
