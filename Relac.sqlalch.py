from datetime import date

from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean

engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
#teste = 5


class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    birthday = Column(Date)
    cpf = Column(String(11), unique=True)

    def __repr__(self) -> str:
        return f"Pessoa(name={self.name})"

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key= True)
    name = Column(String (20))
    description = Column (String(50))
    is_perishable = Column (Boolean, default= False)

    def __repr__(self) -> str:
        return f"Categoria(name={self.description})"


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    is_active = Column(Boolean, default=True)
    pessoa_id = Column(Integer, ForeignKey(Pessoa.id))
    pessoa = relationship("Pessoa", backref="pessoas")
    categoria_id = Column(Integer, ForeignKey(Categoria.id))
    categoria = relationship("Categoria", backref="categorias")

    def __repr__(self) -> str:
        return f"Produto(name={self.name})"





Base.metadata.create_all(engine)


p1 = Pessoa(name="Leonardo", age=25, birthday=date(2020, 1, 20), cpf="322335345342323")
p2 = Pessoa(name="Val", age=22, birthday=date(2019, 3, 23), cpf="4242234234424")
p3 = Pessoa(name="Hudson", age=29, birthday=date(1992, 3, 7), cpf="2324353534532323")
pd1 = Produto(name="Livro", description="Um livro qualquer", price=10.50, pessoa=p1)
pd2 = Produto(name="CD", description="Um cd qualquer", price=20.50, pessoa=p2)
pd3 = Produto(name="Alexa", description="fala pra caramba", price=30.50, pessoa=p3)
categoria1 = Categoria(name = "Eletronicos", description = "Produtos para interação")
categoria2 = Categoria (name = "Laticinios", description = "Produtos alimentícios", is_perishable = True)
categoria3 = Categoria (name = "Açougue", description = "Carnes em geral", is_perishable = True)

session.add_all([p1, p2, p3])

session.commit()