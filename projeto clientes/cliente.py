import uuid

class Cliente:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, email: str, telefone: str, cliente_id: str = None):
        self.id = cliente_id if cliente_id else str(uuid.uuid4())[:8]
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf} | Nascimento: {self.data_nascimento} | E-mail: {self.email} | WhatsApp: {self.telefone}"