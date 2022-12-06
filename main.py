from fastapi import FastAPI, Depends, HTTPException, status, Body
from typing import Union
from sqlalchemy.orm import Session 
import crud, models, schemas 
from database import SessionLocal, get_db, engine
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer
from exceptions import RemedioException, FuncionarioException, ClientePreferencialException, FornecedorException, ClienteException, ProdutoException

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# usuário

@app.get("/api/usuarios/{usuario_id}", response_model=schemas.Usuario)
def get_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/usuarios", response_model=schemas.PaginatedUsuario)
def get_all_usuarios(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_usuarios = crud.get_all_usuarios(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_usuarios}
    return response

@app.post("/api/usuarios", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_usuario(db, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/usuarios/{usuario_id}", response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_usuario(db, usuario_id, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/usuarios/{usuario_id}")
def delete_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)


# login
@app.post("/signup", tags=["usuario"])
async def create_usuario_signup(usuario:schemas.UsuarioCreate=Body(...), db:Session= Depends(get_db)):
	try:
		crud.create_usuario(db, usuario)
		return signJWT(usuario.email)
	except UsuarioExceptio as cie:
		raise HTTPException(**cie.__dict__)

@app.post("/login", tags=["usuario"])
async def user_login(usuario: schemas.UsuarioLoginSchema= Body(...), db: Session= Depends(get_db)):
	if crud.check_usuario(db, usuario):
		return signJWT(usuario.email)
	return {"error": "E-mail ou senha incorretos!"}

#Fornecedor
#, dependencies=[Depends(JWTBearer())]
@app.post("/fornecedores", response_model=schemas.Fornecedor)
def create_fornecedor(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_fornecedor(db, fornecedor)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.put("/fornecedores/{fornecedor_id}", response_model=schemas.Fornecedor)
def update_fornecedor(fornecedor_id: int, fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_fornecedor(db, fornecedor_id, fornecedor)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.delete("/fornecedores/{fornecedor_id}")
def delete_fornecedor_by_id(fornecedor_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_fornecedor_by_id(db, fornecedor_id)
    except FornecedorException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.get("/fornecedores", response_model=schemas.PaginatedFornecedor)
def get_all_fornecedores(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_fornecedores = crud.get_all_fornecedores(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_fornecedores}
    return response
        
#Cliente
    
@app.post("/clientes", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_cliente(db, cliente)
    except ClienteException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.put("/clientes/{cliente_id}", response_model=schemas.Cliente)
def update_cliente(cliente_id: int, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_cliente(db, cliente_id, cliente)
    except ClienteException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.delete("/clientes/{cliente_id}")
def delete_cliente_by_id(cliente_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_cliente_by_id(db, cliente_id)
    except ClienteException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.get("/clientes", response_model=schemas.PaginatedCliente)
def get_all_clientes(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_clientes = crud.get_all_clientes(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_clientes}
    return response
    
#Funcionario
    
@app.post("/funcionarios", response_model=schemas.Funcionario)
def create_funcionario(funcionario: schemas.FuncionarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_funcionario(db, funcionario)
    except FuncionarioException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.put("/funcionarios/{funcionario_id}", response_model=schemas.Funcionario)
def update_funcionario(funcionario_id: int, funcionario: schemas.FuncionarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_funcionario(db, funcionario_id, funcionario)
    except FuncionarioException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.delete("/funcionarios/{funcionario_id}")
def delete_funcionario_by_id(funcionario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_funcionario_by_id(db, funcionario_id)
    except FuncionarioException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.get("/funcionarios", response_model=schemas.PaginatedFuncionario)
def get_all_funcionarios(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_funcionarios = crud.get_all_funcionarios(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_funcionarios}
    return response

#ClientePreferencial
    
@app.post("/clientespreferenciais", response_model=schemas.ClientePreferencial)
def create_clientepreferencial(clientepreferencial: schemas.ClientePreferencialCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_clientepreferencial(db, clientepreferencial)
    except ClientePreferencialException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.put("/clientespreferenciais/{clientepreferencial_id}", response_model=schemas.ClientePreferencial)
def update_clientepreferencial(clientepreferencial_id: int, clientepreferencial: schemas.ClientePreferencialCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_clientepreferencial(db, clientepreferencial_id, clientepreferencial)
    except ClientePreferencialException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.delete("/clientespreferenciais/{clientepreferencial_id}")
def delete_clientepreferencial_by_id(clientepreferencial_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_clientepreferencial_by_id(db, clientepreferencial_id)
    except ClientePreferencialException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.get("/clientespreferenciais", response_model=schemas.PaginatedClientePreferencial)
def get_all_clientespreferenciais(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_clientespreferenciais = crud.get_all_clientespreferenciais(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_clientespreferenciais}
    return response
        
#Produto
    
@app.post("/produtos", response_model=schemas.Produto)
def create_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_produto(db, produto)
    except ProdutoException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.put("/produtos/{produto_id}", response_model=schemas.Produto)
def update_produto(produto_id: int, produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_produto(db, produto_id, produto)
    except ProdutoException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.delete("/produtos/{produto_id}")
def delete_produto_by_id(produto_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_produto_by_id(db, produto_id)
    except ProdutoException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.get("/produtos", response_model=schemas.PaginatedProduto)
def get_all_produtos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_produtos = crud.get_all_produtos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_produtos}
    return response
    
#Remedio
    
@app.post("/remedios", response_model=schemas.Remedio)
def create_remedio(remedio: schemas.RemedioCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_remedio(db, remedio)
    except RemedioException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.put("/remedios/{remedio_id}}", response_model=schemas.Remedio)
def update_remedio(remedio_id: int, remedio: schemas.RemedioCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_remedio(db, remedio_id, remedio)
    except RemedioException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.delete("/remedios/{remedio_id}")
def delete_remedio_by_id(remedio_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_remedio_by_id(db, remedio_id)
    except RemedioException as cie:
        raise HTTPException(**cie.__dict__)
        
@app.get("/remedios", response_model=schemas.PaginatedRemedio)
def get_all_remedios(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_remedios = crud.get_all_remedios(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_remedios}
    return response
