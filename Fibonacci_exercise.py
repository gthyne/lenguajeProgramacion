def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    # ejemplo de uso
    numero = 5
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")


def fibonacci (n):
    if n<= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    #ejemplo de uso
    numero_terminos = 10
    print("serie de fibonacci:")
    for i in range(numero_terminos):
        print(fibonacci(i))

        numeros = [1,2,3,4,5]
        print("lista original:", numeros)
        print("primer elemento:", numero[0])
        print("primer elemento:", numero[-1])


