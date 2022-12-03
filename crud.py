from sqlalchemy.orm import Session
from sqlalchemy import and_
from exceptions import ClientePreferencialAlreadyExistError, ClientePreferencialNotFoundError, FuncionarioAlreadyExistError, FuncionarioNotFoundError, RemedioAlreadyExistError, RemedioNotFoundError, ProdutoAlreadyExistError, ProdutoNotFoundError, FornecedorNotFoundError, FornecedorAlreadyExistError, ClienteNotFoundError, ClienteAlreadyExistError, UsuarioAlreadyExistError, UsuarioNotFoundError
import models, schemas, bcrypt

def check_usuario(db: Session, usuario: schemas.UsuarioLoginSchema):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if db_usuario is None:
        return False
    return bcrypt.checkpw(usuario.senha.encode('utf8'), db_usuario.senha.encode('utf8'))
    
def get_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).get(usuario_id)
    if db_usuario is None:
        raise UsuarioNotFoundError
    return db_usuario

def get_all_usuarios(db: Session, offset: int, limit: int):
    return db.query(models.Usuario).offset(offset).limit(limit).all()

def get_usuario_by_email(db: Session, usuario_email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == usuario_email).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = get_usuario_by_email(db, usuario.email)
    # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
    usuario.senha = bcrypt.hashpw(usuario.senha.encode('utf8'), bcrypt.gensalt())
    if db_usuario is not None:
        raise UsuarioAlreadyExistError
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioCreate):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db_usuario.nome = usuario.nome
    db_usuario.email = usuario.email
    if usuario.senha != "":
        # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
        db_usuario.senha = bcrypt.hashpw(usuario.senha.encode('utf8'), bcrypt.gensalt())
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db.delete(db_usuario)
    db.commit()
    return

#Fornecedor
def create_fornecedor(db: Session, fornecedor: schemas.FornecedorCreate):
    db_fornecedor= models.Fornecedor(**fornecedor.dict())
    db.add(db_fornecedor)
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor   
    
def get_fornecedor_by_email(db: Session, fornecedor_email: str):  
    return db.query(models.Fornecedor).filter(models.Fornecedor.email== fornecedor_email).first()
    
def get_fornecedor_by_id(db: Session, fornecedor_id: int):
    db_fornecedor = db.query(models.Fornecedor).get(fornecedor_id)
    if db_fornecedor is None:
        raise FornecedorNotFoundError
    return db_fornecedor
    
def get_all_fornecedores(db: Session, offset: int, limit: int):
    return db.query(models.Fornecedor).offset(offset).limit(limit).all()
    
def update_fornecedor(db: Session, fornecedor_id: int, fornecedor: schemas.FornecedorCreate):
    db_fornecedor = get_fornecedor_by_id(db, fornecedor_id)
    db_fornecedor.nome = fornecedor.nome
    db_fornecedor.email = fornecedor.email
    db_fornecedor.fixo = fornecedor.fixo
    db_fornecedor.celular = fornecedor.celular
    db_fornecedor.cnpj = fornecedor.cnpj
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor

def delete_fornecedor_by_id(db: Session, fornecedor_id: int):
    db_fornecedor = get_fornecedor_by_id(db, fornecedor_id)
    db.delete(db_fornecedor)
    db.commit()
    return
    
#ClientePreferencial
def create_clientepreferencial(db: Session, clientepreferencial: schemas.ClientePreferencialCreate):
    db_clientepreferencial= models.ClientePreferencial(**clientepreferencial.dict())
    db.add(db_clientepreferencial)
    db.commit()
    db.refresh(db_clientepreferencial)
    return db_clientepreferencial  
    
def get_clientepreferencial_by_email(db: Session, clientepreferencial_email: str):  
    return db.query(models.ClientePreferencial).filter(models.ClientePreferencial.email== clientepreferencial_email).first()
    
def get_clientepreferencial_by_id(db: Session, clientepreferencial_id: int):
    db_clientepreferencial = db.query(models.ClientePreferencial).get(clientepreferencial_id)
    if db_clientepreferencial is None:
        raise ClientePreferencialNotFoundError
    return db_clientepreferencial
    
def get_all_clientespreferenciais(db: Session, offset: int, limit: int):
    return db.query(models.ClientePreferencial).offset(offset).limit(limit).all()
    
def update_clientepreferencial(db: Session, clientepreferencial_id: int, clientepreferencial: schemas.ClientePreferencialCreate):
    db_clientepreferencial = get_clienepreferencial_by_id(db, clientepreferencial_id)
    db_clientepreferencial.nome = clientepreferencial.nome
    db_clientepreferencial.email = clientepreferencial.email
    db_clientepreferencial.fixo = clientepreferencial.fixo
    db_clientepreferencial.celular = clientepreferencial.celular
    db_clientepreferencial.cpf = clientepreferencial.cpf
    db_clientepreferencial.desconto = clientepreferencial.desconto
    db.commit()
    db.refresh(db_clientepreferencial)
    return clientepreferencial

def delete_clientepreferencial_by_id(db: Session, clientepreferencial_id: int):
    db_clientepreferencial = get_clienepreferencial_by_id(db, clientepreferencial_id)
    db.delete(db_clientepreferencial)
    db.commit()
    return
    
#Cliente
def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente= models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def get_cliente_by_email(db: Session, cliente_email: str):  
    return db.query(models.Cliente).filter(models.Cliente.email== cliente_email).first()
    
def get_cliente_by_id(db: Session, cliente_id: int):
    db_cliente = db.query(models.Cliente).get(cliente_id)
    if db_cliente is None:
        raise ClienteNotFoundError
    return db_cliente
    
def get_all_clientes(db: Session, offset: int, limit: int):
    return db.query(models.Cliente).offset(offset).limit(limit).all()
    
def update_cliente(db: Session, cliente_id: int, cliente: schemas.ClienteCreate):
    db_cliente = get_cliente_by_id(db, cliente_id)
    db_cliente.nome = cliente.nome
    db_cliente.email = cliente.email
    db_cliente.fixo = cliente.fixo
    db_cliente.celular = cliente.celular
    db_cliente.cpf = cliente.cpf
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente_by_id(db: Session, cliente_id: int):
    db_cliente = get_cliente_by_id(db, cliente_id)
    db.delete(db_cliente)
    db.commit()
    return

#Funcionario
def create_funcionario(db: Session, cliente: schemas.FuncionarioCreate):
    db_funcionario= models.Funcionario(**funcionario.dict())
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario

def get_funcionario_by_email(db: Session, funcionario_email: str):  
    return db.query(models.Funcionario).filter(models.Funcionario.email== funcionario_email).first()
    
def get_funcionario_by_id(db: Session, funcionario_id: int):
    db_funcionario = db.query(models.Funcionario).get(funcionario_id)
    if db_funcionario is None:
        raise FuncionarioNotFoundError
    return db_funcionario
    
def get_all_funcionarios(db: Session, offset: int, limit: int):
    return db.query(models.Funcionario).offset(offset).limit(limit).all()
    
def update_funcionario(db: Session, funcionario_id: int, funcionario: schemas.FuncionarioCreate):
    db_funcionario = get_funcionario_by_id(db, funcionario_id)
    db_funcionario.nome = funcionario.nome
    db_funcionario.email = funcionario.email
    db_funcionario.fixo = funcionario.fixo
    db_funcionario.celular = funcionario.celular
    db_funcionario.cpf = funcionario.cpf
    db_funcionario.cargahoraria = funcionario.cargahoraria
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario

def delete_funcionario_by_id(db: Session, funcionario_id: int):
    db_funcionario = get_funcionario_by_id(db, funcionario_id)
    db.delete(db_funcionario)
    db.commit()
    return

#Produto
def create_produto(db: Session, produto: schemas.ProdutoCreate):
    db_produto= models.Produto(**produto.dict())
    db.add(produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto
    
def get_produto_by_tipo(db: Session, produto_tipo: str):  
    return db.query(models.Produto).filter(models.Produto.tipo== produto_tipo).first()
    
def get_produto_by_id(db: Session, produto_id: int):
    db_produto = db.query(models.Produto).get(produto_id)
    if db_produto is None:
        raise ProdutoNotFoundError
    return db_produto
    
def get_all_produtos(db: Session, offset: int, limit: int):
    return db.query(models.Produto).offset(offset).limit(limit).all()
    
def update_produto(db: Session, produto_id: int, produto: schemas.ProdutoCreate):
    db_produto = get_produto_by_id(db, produto_id)
    db_produto.nome = produto.nome
    db_produto.tipo = produto.tipo
    db_produto.valor = produto.valor
    db_produto.quantidade = produto.quantidade
    db.commit()
    db.refresh(db_produto)
    return db_produto

def delete_produto_by_id(db: Session, produto_id: int):
    db_produto = get_produto_by_id(db, produto_id)
    db.delete(db_produto)
    db.commit()
    return
    
#Remedio
def create_remedio(db: Session, remedio: schemas.RemedioCreate):
    db_remedio= models.Remedio(**remedio.dict())
    db.add(remedio)
    db.commit()
    db.refresh(db_remedio)
    return db_remedio
    
def get_remedio_by_tipo(db: Session, remedio_tipo: str):  
    return db.query(models.Remedio).filter(models.Remedio.tipo== remedio_tipo).first()
    
def get_remedio_by_id(db: Session, remedio_id: int):
    db_remedio = db.query(models.Remedio).get(remedio_id)
    if db_remedio is None:
        raise RemedioNotFoundError
    return db_remedio
    
def get_all_remedios(db: Session, offset: int, limit: int):
    return db.query(models.Remedio).offset(offset).limit(limit).all()
    
def update_remedio(db: Session, remedio_id: int, remedio: schemas.RemedioCreate):
    db_remedio = get_remedio(db, remedio_id)
    db_remedio.nome = remedio.nome
    db_remedio.tipo = remedio.tipo
    db_remedio.valor = remedio.valor
    db_remedio.quantidade = remedio.quantidade
    db_remedio.tarja = remedio.tarja
    db.commit()
    db.refresh(db_remedio)
    return db_remedio

def delete_remedio_by_id(db: Session, remedio_id: int):
    db_remedio = get_remedio_by_id(db, remedio_id)
    db.delete(db_remedio)
    db.commit()
    return