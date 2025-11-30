# estrategia_frete.py
class EstrategiaFrete:
    """Interface base para estratégias de frete."""
    def calcular(self, peso: float) -> float:
        raise NotImplementedError