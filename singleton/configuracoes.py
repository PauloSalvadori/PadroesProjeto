"""
Gerenciador de Configurações - Exemplo do padrão Singleton.
"""

class GerenciadorConfiguracoes:
    """Singleton responsável por armazenar configurações da aplicação."""
    
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._dados = {}
        return cls._instancia

    def definir(self, chave: str, valor):
        self._dados[chave] = valor

    def obter(self, chave: str, padrao=None):
        return self._dados.get(chave, padrao)

    def todas(self):
        return dict(self._dados)