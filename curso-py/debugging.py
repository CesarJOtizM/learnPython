def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    while True:
        try:
            num = int(input('Enter a number: '))
            if num < 0:
                raise Exception('Negative number is not valid')
            print(divisors(num))
            print('[!] Finish...')
            break
        except ValueError:
            print('[!] Solo puedes añadir números')
        except Exception:
            print('[!] El numero no puede ser negativo')


if __name__ == '__main__':
    run()
