# frete_expresso.py
from estrategia_frete import EstrategiaFrete

class FreteExpresso(EstrategiaFrete):
    def calcular(self, peso: float) -> float:
        return peso * 1.5