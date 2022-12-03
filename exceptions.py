class FornecedorException(Exception):
    ...

class FornecedorNotFoundError(FornecedorException):
    def __init__(self):
        self.status_code = 404
        self.detail = "FORNECEDOR_NAO_ENCONTRADO"


class FornecedorAlreadyExistError(FornecedorException):
    def __init__(self):
        self.status_code = 409
        self.detail = "FORNECEDOR_DUPLICADO"
        
class FuncionarioException(Exception):
    ...

class FuncionarioNotFoundError(FuncionarioException):
    def __init__(self):
        self.status_code = 404
        self.detail = "FUNCIONARIO_NAO_ENCONTRADO"


class FuncionarioAlreadyExistError(FuncionarioException):
    def __init__(self):
        self.status_code = 409
        self.detail = "FUNCIONARIO_DUPLICADO"
        
class RemedioException(Exception):
    ...

class RemedioNotFoundError(RemedioException):
    def __init__(self):
        self.status_code = 404
        self.detail = "REMEDIO_NAO_ENCONTRADO"


class RemedioAlreadyExistError(RemedioException):
    def __init__(self):
        self.status_code = 409
        self.detail = "REMEDIO_DUPLICADO"
        
class ClienteException(Exception):
    ...

class ClienteNotFoundError(ClienteException):
    def __init__(self):
        self.status_code = 404
        self.detail = "CLIENTE_NAO_ENCONTRADO"


class ClienteAlreadyExistError(ClienteException):
    def __init__(self):
        self.status_code = 409
        self.detail = "CLIENTE_DUPLICADO"
        
class ClientePreferencialException(Exception):
    ...

class ClientePreferencialNotFoundError(ClientePreferencialException):
    def __init__(self):
        self.status_code = 404
        self.detail = "CLIENTE_PREFERENCIAL_NAO_ENCONTRADO"


class ClientePreferencialAlreadyExistError(ClienteException):
    def __init__(self):
        self.status_code = 409
        self.detail = "CLIENTE_PREFERENCIAL_DUPLICADO"

class ProdutoException(Exception):
    ...

class ProdutoNotFoundError(ProdutoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "PRODUTO_NAO_ENCONTRADO"


class ProdutoAlreadyExistError(ProdutoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "PRODUTO_DUPLICADO"
        
class UsuarioException(Exception):
    ...

class UsuarioNotFoundError(UsuarioException):
    def __init__(self):
        self.status_code = 404
        self.detail = "USUARIO_NAO_ENCONTRADO"


class UsuarioAlreadyExistError(UsuarioException):
    def __init__(self):
        self.status_code = 409
        self.detail = "EMAIL_DUPLICADO"

