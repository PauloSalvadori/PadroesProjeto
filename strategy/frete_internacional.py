# frete_internacional.py
from estrategia_frete import EstrategiaFrete

class FreteInternacional(EstrategiaFrete):
    def calcular(self, peso: float) -> float:
        return 20.0 + peso * 3