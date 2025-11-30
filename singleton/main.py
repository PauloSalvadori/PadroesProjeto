from configuracoes import GerenciadorConfiguracoes

def demo_singleton():
    c1 = GerenciadorConfiguracoes()
    c2 = GerenciadorConfiguracoes()

    print("c1 é c2:", c1 is c2)

    c1.definir("tema", "escuro")
    c2.definir("idioma", "pt-BR")

    print("Configurações de c1:", c1.todas())
    print("Configurações de c2:", c2.todas())

if __name__ == "__main__":
    demo_singleton()