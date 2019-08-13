# Implementa la función fib(n) que retorna el n-ésimo número de la serie
# de Fibonacci:
# fib(1) = 1
# fib(2) = 1
# fib(n) = fib(n - 1) + fib(n - 2), para todo n > 2.


def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


if __name__ == "__main__":
    # Prueba de la función: imprime los primeros 10 números en una línea
    # separados por coma y espacio.
    prueba_fib = ''
    for i in range(1,11):
        result = fib(i)
        if prueba_fib == "":
            prueba_fib = str(result)
        else:
            prueba_fib += ",%s" % (result)
    print(prueba_fib)
