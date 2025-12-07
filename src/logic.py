def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "empate :("
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "usuario"
    else:
        return "computadora"