def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError('dividir() deve receber apenas argumentos inteiros')

    try:
        aux = dividendo / divisor
    except:
        print(f"Não foi possível dividir {dividendo} por {divisor}")
        raise

    return aux

def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f'O resultado da divisao de 10 por {divisor} é {resultado}')

""" try:
    testa_divisao(2.5)
except ZeroDivisionError as E:
    print("Erro de divisão por zero!")
except Exception as E:
    print("Tratamento generico!")

print('Programa encerrado') """

try:
    print("o fluxo está aqui")
    raise ValueError
except:
    print("Agora ele foi para cá")

print("E enfim ele continua...")
