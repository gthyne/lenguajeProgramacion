class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0  # Atributo privado para el saldo actual

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado {cantidad}.")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.__saldo >= cantidad:
                self.__saldo -= cantidad
                print(f"Se han retirado {cantidad}.")
            else:
                print("No hay saldo suficiente en la cuenta.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")

    def consultar_saldo(self):
        print(f"El saldo actual es de {self.__saldo}.")
        return 