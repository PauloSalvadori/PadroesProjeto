# pagamento_adapter.py
from processador_novo import ProcessadorPagamentoNovo
from sistema_antigo import SistemaPagamentoAntigo

class PagamentoAdapter(ProcessadorPagamentoNovo):
    """Adapter que traduz a interface moderna para a interface antiga."""
    
    def __init__(self, sistema_antigo: SistemaPagamentoAntigo):
        self.sistema_antigo = sistema_antigo

    def processar_pagamento(self, valor: float):
        return self.sistema_antigo.realizar_transacao(valor)