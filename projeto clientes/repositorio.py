from cliente import Cliente

class RepositorioClientes:
    def __init__(self):
        self.clientes = []

    def salvar(self, cliente: Cliente):
        if any(c.cpf == cliente.cpf for c in self.clientes):
            return False, "Erro: Já existe um cliente cadastrado com este CPF."
        
        self.clientes.append(cliente)
        return True, "Cliente cadastrado com sucesso!"

    def listar(self):
        return self.clientes

    def buscar(self, termo: str):
        termo = termo.strip().lower()
        resultados = []
        
        for cliente in self.clientes:
            if (termo == cliente.id.lower() or 
                termo in cliente.nome.lower() or 
                termo == cliente.cpf or 
                termo == cliente.email.lower()):
                resultados.append(cliente)
                
        return resultados

    def atualizar(self, identificador: str, novo_nome: str, nova_data_nascimento: str, novo_email: str, novo_telefone: str):
        cliente = self._buscar_por_id_ou_cpf(identificador)
        
        if not cliente:
            return False, "Cliente não encontrado."

        if novo_nome:
            cliente.nome = novo_nome
        if nova_data_nascimento:
            cliente.data_nascimento = nova_data_nascimento
        if novo_email:
            cliente.email = novo_email
        if novo_telefone:
            cliente.telefone = novo_telefone

        return True, "Dados do cliente atualizados com sucesso! (O CPF foi mantido inalterado)."

    def remover(self, identificador: str):
        cliente = self._buscar_por_id_ou_cpf(identificador)
        
        if not cliente:
            return False, "Cliente não encontrado para remoção."
            
        self.clientes.remove(cliente)
        return True, f"Sucesso: Cliente '{cliente.nome}' (ID: {cliente.id}) foi removido da base."

    def _buscar_por_id_ou_cpf(self, identificador: str):
        for cliente in self.clientes:
            if cliente.id == identificador or cliente.cpf == identificador:
                return cliente
        return None