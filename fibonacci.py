def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    return result


if __name__ == "__main__":
    prueba_fib = ''
    for i in range(1,11):
        result = fib(i)
        if prueba_fib == "":
            prueba_fib = str(result)
        else:
            prueba_fib += ",%s" % (result)
    print(prueba_fib)
