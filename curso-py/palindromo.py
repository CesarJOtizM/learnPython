# def palindromo(palabra: str) -> bool:
#     palabra = palabra.replace(' ', '').lower()
#     if palabra[::] == palabra[::-1]:
#         return True
#     else:
#         return False


# def run() -> None:
#     palabra: str = input("Escribe una palabra: ")
#     es_palindromo: bool = palindromo(palabra)
#     if es_palindromo:
#         print("Es palindromo")
#     else:
#         print("no Es palindromo")


# if __name__ == '__main__':
#     run()

def run():
    def palindrome(string): return string == string[::-1]

    print(palindrome("ana"))


if __name__ == '__main__':
    run()
