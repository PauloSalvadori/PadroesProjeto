# sistema_antigo.py
class SistemaPagamentoAntigo:
    """Sistema legado com interface incompatível."""
    
    def __init__(self, id_mercante: str):
        self.id_mercante = id_mercante

    def realizar_transacao(self, valor: float):
        print(f"[Sistema Antigo] Pagamento de {valor} realizado pelo mercante {self.id_mercante}.")
        return f"TX-{int(valor * 100)}-{self.id_mercante}"