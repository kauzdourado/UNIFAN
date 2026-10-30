from cliente import Cliente
from repositorio import RepositorioClientes

class Menu:
    def __init__(self, repositorio: RepositorioClientes):
        self.repositorio = repositorio

    def executar(self):
        while True:
            print("\n" + "="*45)
            print("        SISTEMA DE GESTÃO DE CLIENTES")
            print("="*45)
            print("1. Cadastrar novo cliente")
            print("2. Listar todos os clientes")
            print("3. Buscar cliente (ID, Nome, CPF ou E-mail)")
            print("4. Atualizar dados do cliente")
            print("5. Remover cliente")
            print("6. Encerrar a execução")
            print("-" * 45)
            
            opcao = input("Escolha uma opção (1-6): ").strip()
            
            if opcao == "1":
                self._cadastrar()
            elif opcao == "2":
                self._listar()
            elif opcao == "3":
                self._buscar()
            elif opcao == "4":
                self._atualizar()
            elif opcao == "5":
                self._remover()
            elif opcao == "6":
                print("\nEncerrando o sistema. Até logo!")
                break
            else:
                print("\n[Erro] Opção inválida! Por favor, escolha um número de 1 a 6.")

    def _cadastrar(self):
        print("\n--- CADASTRO DE NOVO CLIENTE ---")
        nome = input("Nome completo: ")
        cpf = input("CPF (documento único): ")
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        email = input("E-mail de contato: ")
        telefone = input("Telefone com WhatsApp: ")
        
        novo_cliente = Cliente(nome, cpf, data_nascimento, email, telefone)
        sucesso, mensagem = self.repositorio.salvar(novo_cliente)
        print(f"\n{mensagem}")

    def _listar(self):
        print("\n--- LISTA DE CLIENTES CADASTRADOS ---")
        clientes = self.repositorio.listar()
        
        if not clientes:
            print("Nenhum cliente cadastrado no momento.")
            return
        
        for cliente in clientes:
            print(cliente)

    def _buscar(self):
        print("\n--- BUSCAR CLIENTE ---")
        termo = input("Digite o ID, Nome, CPF ou E-mail para buscar: ")
        resultados = self.repositorio.buscar(termo)
        
        if not resultados:
            print("\nNenhum cliente encontrado com esse termo.")
            return
            
        print(f"\nForam encontrados {len(resultados)} registro(s):")
        for cliente in resultados:
            print(cliente)

    def _atualizar(self):
        print("\n--- ATUALIZAR DADOS DO CLIENTE ---")
        identificador = input("Digite o ID ou CPF do cliente que deseja atualizar: ")
        
        print("(Dica: Deixe em branco caso não queira alterar determinado campo)")
        novo_nome = input("Novo nome: ").strip()
        nova_data_nascimento = input("Nova data de nascimento: ").strip()
        novo_email = input("Novo e-mail: ").strip()
        novo_telefone = input("Novo telefone com WhatsApp: ").strip()
        
        sucesso, mensagem = self.repositorio.atualizar(
            identificador,
            novo_nome if novo_nome else None,
            nova_data_nascimento if nova_data_nascimento else None,
            novo_email if novo_email else None,
            novo_telefone if novo_telefone else None
        )
        print(f"\n{mensagem}")

    def _remover(self):
        print("\n--- REMOVER CLIENTE ---")
        identificador = input("Digite o ID ou CPF do cliente que deseja remover: ")
        
        confirmacao = input(f"Tem certeza que deseja remover o registro '{identificador}'? (s/n): ").strip().lower()
        if confirmacao == 's':
            sucesso, mensagem = self.repositorio.remover(identificador)
            print(f"\n{mensagem}")
        else:
            print("\nOperação de remoção cancelada.")