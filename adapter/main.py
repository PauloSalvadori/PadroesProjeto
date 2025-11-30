# main.py
from pagamento_adapter import PagamentoAdapter
from sistema_antigo import SistemaPagamentoAntigo

def demo_adapter():
    antigo = SistemaPagamentoAntigo("BR-999")
    adapter = PagamentoAdapter(antigo)

    resultado = adapter.processar_pagamento(120.50)
    print("Resultado retornado ao sistema moderno:", resultado)

if __name__ == "__main__":
    demo_adapter()