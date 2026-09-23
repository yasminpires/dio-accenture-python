from abc import ABC, abstractmethod

# Classe abstrata para padronizar colaboradores
class Colaborador(ABC):
    @abstractmethod
    def exibir_info(self):
        pass


# Classe concreta para Analista
class Analista(Colaborador):
    def __init__(self, nome):
        self.nome = nome

    def exibir_info(self):
        # Retorna a informaçãp do analista
        return f"Analista: {self.nome}"


# Leitura do nome do analista
nome_analista = input()

# Criação do objeto Analista
analista = Analista(nome_analista)

# Exibe as informações
print(analista.exibir_info())