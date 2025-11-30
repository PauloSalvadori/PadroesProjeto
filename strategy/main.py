# main.py
from calculadora_frete import CalculadoraFrete
from frete_normal import FreteNormal
from frete_expresso import FreteExpresso
from frete_internacional import FreteInternacional

def demo_strategy():
    calc = CalculadoraFrete(FreteNormal())
    print("Frete Normal (5kg):", calc.calcular(5))

    calc.definir_estrategia(FreteExpresso())
    print("Frete Expresso (5kg):", calc.calcular(5))

    calc.definir_estrategia(FreteInternacional())
    print("Frete Internacional (5kg):", calc.calcular(5))

if __name__ == "__main__":
    demo_strategy()