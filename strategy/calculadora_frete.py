# calculadora_frete.py
from estrategia_frete import EstrategiaFrete

class CalculadoraFrete:
    """Classe que utiliza a estratégia escolhida."""
    
    def __init__(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia

    def definir_estrategia(self, nova_estrategia: EstrategiaFrete):
        self.estrategia = nova_estrategia

    def calcular(self, peso: float) -> float:
        return self.estrategia.calcular(peso)