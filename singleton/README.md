# Padrão de Projeto Criacional: Singleton

O código presente nesta pasta se baseia no conteúdo do site "Refactoring Guru", referenciado no link abaixo:  
https://refactoring.guru/pt-br/design-patterns/singleton

## Linguagem de programação usada

Para realizar a implementação deste padrão de projeto foi utilizada a linguagem **Python** no VSCode.  
Para executar o código, é necessário instalar:

- **Python 3.10+**  
- Extensão **Python** no VSCode

Após instalar, basta abrir o arquivo e clicar no botão **Run**.

---

## Utilização da LLM

Foi utilizada a LLM **ChatGPT** para obter auxílio na estruturação da implementação, explicações do padrão e correção de erros.

---

## O que é o padrão Singleton e o que ele resolve?

O Singleton é um padrão de projeto **criacional** que garante que uma classe possua **apenas uma única instância** durante toda a execução da aplicação.

Ele resolve problemas como:

- múltiplas instâncias desnecessárias de um recurso global;
- inconsistência de dados compartilhados;
- desperdício de memória;
- gerenciamento complicado de estados globais.

Com o Singleton, toda vez que a classe for instanciada, a mesma instância será retornada.

---

## Exemplo de implementação

Neste projeto, o Singleton foi utilizado para implementar um **Gerenciador de Configurações**.  
A aplicação pode acessar ou alterar configurações através de uma única instância, garantindo consistência entre todos os módulos.

---

## Explicação do código

### **configuracoes.py**
- Implementa o Singleton usando o método `__new__()`;
- Armazena configurações em um dicionário interno;
- Sempre retorna a mesma instância, independente de quantas vezes seja criado.

### **main.py**
- Cria duas instâncias e demonstra que ambas referenciam o mesmo objeto;
- Altera configurações e mostra que todos os acessos compartilham os mesmos valores.