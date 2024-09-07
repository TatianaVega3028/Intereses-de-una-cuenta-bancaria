class CuentaBancaria:
    def __init__(self, saldo_inicial: float):

        self.saldo = saldo_inicial

    def calcular_saldo_final(self):

        if self.saldo < 10000:
            self.saldo = self.saldo * (1 + 0.03)
        else:
            self.saldo = self.saldo * (1 + 0.04)
        return self.saldo

    def mostrar_saldo(self):

        saldo_final = self.calcular_saldo_final()
        print(f"El saldo final después de un año es: {saldo_final:.2f}")


class Banco:
    def __init__(self):
        self.iniciar()

    def iniciar(self):
        saldo_inicial = float(input("Ingrese el saldo inicial: "))

        cuenta = CuentaBancaria(saldo_inicial)

        cuenta.mostrar_saldo()


if __name__ == "__main__":
    Banco()
