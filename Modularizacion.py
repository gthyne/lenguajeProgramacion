def suma(a,b):
    return a + b
def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: division por cero"
    
    # contenido del archivo principal.py
    import funciones
    #Ejemplos de uso de las ffunciones del modulo
    resultado_suma = function.suma(5, 3)
    print("suma:", resultado_suma)

    resultado_resta = function.resta(10, 7)
    print("suma:", resultado_resta) 

    resultado_resta = function.multiplicacion(4, 6)
    print("multiplicacion:", resultado_multiplicacion)

    resultado_resta = function.division(8, 2)
    print("division:", resultado_division)

