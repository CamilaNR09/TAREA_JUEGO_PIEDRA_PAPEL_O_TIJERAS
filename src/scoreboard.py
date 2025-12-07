class Scoreboard:
    def __init__(self):
        self.usuario = 0
        self.computadora = 0
        self.empates = 0

    def actualizar (self, resultado):
        if resultado == "usuario":
            self.usuario += 1
        elif resultado == "computadora":
            self.computadora += 1
        elif resultado == "empate":
            self.empates += 1

    def mostrar(self):
        print(f"Usuario: {self.usuario} | Computadora: {self.computadora} | Empate: {self.empates}")
        