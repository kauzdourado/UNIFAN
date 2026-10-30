from repositorio import RepositorioClientes
from menu import Menu

if __name__ == "__main__":
    repo = RepositorioClientes()
    
    sistema_menu = Menu(repo)
    
    sistema_menu.executar()