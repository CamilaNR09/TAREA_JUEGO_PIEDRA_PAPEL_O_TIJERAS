from logic import determinar_ganador
from random_gen import jugada_computadora
from scoreboard import Scoreboard

def jugar():
    marcador = Scoreboard()

    while True:
        usuario = imput ("Elije piedra, papel o tijeras (o SALIR para terminar el juego): ").lower()
        if usuario == "SALIR":
            print ("\nJuego Terminado")
            marcador.mostrar()
            break
        if usuario not in ["piedra, papel o tijeras"]:
            print ("Entrada invalida. Intenta de nuevo. ")
            continue
        computadora = jugada_computadora()
        print ("Tu elegiste: {usuario}")
        print ("La computadora eligió: {computadora}")

        resultado = determinar_ganador(usuario, computadora)

        if resultado == "empate":
            print("EMPATE!")
        elif resultado == "usuario":
            print ("GANASTE, FELICITACIONES")
        else:
            print("perdiste :(")

        marcador.actualizar(resultado)
        marcador.mostrar()
    if __name__ == "__main__":
        jugar()