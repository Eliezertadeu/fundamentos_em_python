class Calculadora:

    # def __init__(self):
    #     pass

    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

calc = Calculadora()
print(calc.mult(10, 2))
print(calc.soma(22, 22))
print(calc.sub(22, 10))
