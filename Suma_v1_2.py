class OperacionesAritmeticas:

    def calcularSuma(self, sumando1, sumando2):
        sumando1 + sumando2
        return sumando1 + sumando2

    def leerSumandos(self):
        sumando1 = int(input("Ingrese primer sumando: "))
        sumando2 = int(input("Ingrese segundo sumando: "))
        return sumando1, sumando2


if __name__ == '__main__':
    operacion = OperacionesAritmeticas()
    sumando1, sumando2 = operacion.leerSumandos()
    print(f"{sumando1} + {sumando2} = {operacion.calcularSuma(sumando1, sumando2)}")
