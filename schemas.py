from datetime import date
from typing import List  
from pydantic import BaseModel

class ClienteBase(BaseModel):
    nome: str
    email: str
    fixo: str
    celular: str
    cpf: str
class ClienteCreate(ClienteBase):
    pass
class Cliente(ClienteBase):
    id: int
    class Config:
        orm_mode= True

class PaginatedCliente(BaseModel):
    limit: int
    offset: int
    data: List[Cliente]
    
class ClientePreferencialBase(BaseModel):
    nome: str
    email: str
    fixo: str
    celular: str
    cpf: str
    desconto: float
class ClientePreferencialCreate(ClientePreferencialBase):
    pass
class ClientePreferencial(ClientePreferencialBase):
    id: int
    class Config:
        orm_mode= True

class PaginatedClientePreferencial(BaseModel):
    limit: int
    offset: int
    data: List[ClientePreferencial]
    
class FuncionarioBase(BaseModel):
    nome: str
    email: str
    fixo: str
    celular: str
    cpf: str
    cargahoraria: str
class FuncionarioCreate(FuncionarioBase):
    pass
class Funcionario(FuncionarioBase):
    id: int
    class Config:
        orm_mode= True

class PaginatedFuncionario(BaseModel):
    limit: int
    offset: int
    data: List[Funcionario]
        
class FornecedorBase(BaseModel):
    nome: str
    email: str
    fixo: str
    celular: str
    cnpj: str
class FornecedorCreate(FornecedorBase):
    pass
class Fornecedor(FornecedorBase):
    id: int
    class Config:
        orm_mode= True
        
class PaginatedFornecedor(BaseModel):
    limit: int
    offset: int
    data: List[Fornecedor]
 
class ProdutoBase(BaseModel):
    nome: str
    tipo: str
    valor: float
    quantidade: int
class ProdutoCreate(ProdutoBase):
    pass
class Produto(ProdutoBase):
    id: int
    class Config:
        orm_mode= True

class PaginatedProduto(BaseModel):
    limit: int
    offset: int
    data: List[Produto]
    
class RemedioBase(BaseModel):
    nome: str
    tipo: str
    valor: float
    quantidade: int
    tarja: str
class RemedioCreate(RemedioBase):
    pass
class Remedio(RemedioBase):
    id: int
    class Config:
        orm_mode= True

class PaginatedRemedio(BaseModel):
    limit: int
    offset: int
    data: List[Remedio]
	
class UsuarioBase(BaseModel):
    nome: str
    email: str
class UsuarioCreate(UsuarioBase):
    senha: str
class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True
class UsuarioLoginSchema(BaseModel):
	email: str
	senha: str
	class Config:
		schema_extra= {"example": {"email": "x@x.com","senha": "pass"}}
		
class PaginatedUsuario(BaseModel):
    limit: int
    offset: int
    data: List[Usuario]