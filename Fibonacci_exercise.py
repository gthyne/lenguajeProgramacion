def fibonacci (n):
    if n<= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    numero_terminos = 10
    print("serie de fibonacci:")
    for i in range(numero_terminos):
        print(fibonacci(i))

        numeros = [1,2,3,4,5]
        print("lista original:", numeros)
        print("primer elemento:", numero[0])
        print("primer elemento:", numero[-1])