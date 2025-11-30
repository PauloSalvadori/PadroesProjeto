# frete_normal.py
from estrategia_frete import EstrategiaFrete

class FreteNormal(EstrategiaFrete):
    def calcular(self, peso: float) -> float:
        return 10.0