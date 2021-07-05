def es_primo(number: int) -> bool:
    contador: int = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        elif number % i == 0:
            contador += 1
        else:
            pass
    if contador == 0:
        return True
    else:
        return False


def run():
    numero: int = int(input("Ingresa un numero: "))
    primo: bool = es_primo(numero)
    if primo:
        print("Es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    run()
