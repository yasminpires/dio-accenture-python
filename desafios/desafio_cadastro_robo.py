class Robo:
    def __init__(self, nome: str, tarefa: str):
        self.nome = nome
        self.tarefa = tarefa

    def descricao(self) -> str:
        # Retorna a descrição do robô
        return f"Robo {self.nome} executa {self.tarefa}"

def main():
        entrada = input().strip()
        partes = entrada.split(maxsplit=1)

        if len(partes) != 2:
            print("Entrada inválida")
            return

        nome, tarefa = partes

        # Cria um objeto da classe Robo
        robo = Robo(nome, tarefa)

        # Exibe a descrição do robô
        print(robo.descricao())


if __name__ == "__main__":
    main() 