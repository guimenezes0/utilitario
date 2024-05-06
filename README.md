# 🛠️ Biblioteca de Utilitários em Python - Utilitarios 

## 🌟 Recursos 

A biblioteca Utilitarios inclui uma variedade de funções úteis, desde operações básicas de arquivos até funções mais complexas.

## 💡 Como Instalar 

Para instalar a biblioteca Utilitarios, você pode clonar este repositório para o seu ambiente local. Aqui estão as etapas:

1. Abra o terminal.
2. Navegue até o diretório onde deseja clonar o repositório.
3. Execute o seguinte comando: `git clone <URL do repositório>`

## 🚀 Como Usar 

Depois de clonar o repositório, você pode importar a biblioteca Utilitarios em seu código Python e começar a usar suas funções imediatamente. Aqui está um exemplo:

```python
from utilitarios import Utilitarios

# Ler um arquivo
conteudo = Utilitarios.ler_arquivo('arquivo.txt')
print(conteudo)

# Fazer uma requisição GET e retornar a resposta como JSON
resposta = Utilitarios.requisicao_get('https://api.meusite.com')
print(resposta)
