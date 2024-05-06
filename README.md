# 🛠️ Biblioteca de Utilitários em Python - Utilitarios 

Olá, programadores! Estou animado para compartilhar com vocês a biblioteca de utilitários que desenvolvi em Python. Ela é projetada para tornar seu dia a dia de codificação mais eficiente e agradável.

## 🌟 Recursos 

A biblioteca Utilitarios inclui uma variedade de funções úteis, desde operações básicas de arquivos até funções mais complexas, como:

### Operações de arquivo
- Ler e escrever arquivos e JSONs
- Listar arquivos em um diretório
- Criar um novo diretório

### Funções de rede
- Fazer uma requisição GET para uma URL e retornar a resposta como JSON

### Funções de texto
- Gerar um hash de uma string
- Encontrar todas as ocorrências de um padrão em um texto usando expressões regulares

### Funções de lista
- Remover itens duplicados de uma lista
- Ordenar uma lista em ordem crescente ou decrescente

### Funções de data
- Formatar uma data para uma string
- Obter a data atual

### Funções matemáticas
- Calcular o n-ésimo número na sequência de Fibonacci

## 💡 Como usar 

Você pode importar a biblioteca Utilitarios em seu código Python e começar a usar suas funções imediatamente. Aqui está um exemplo:

```
from utilitarios import Utilitarios

# Ler um arquivo
conteudo = Utilitarios.ler_arquivo('meu_arquivo.txt')

# Fazer uma requisição GET
resposta = Utilitarios.fazer_requisicao_get('https://meu-site.com/api/dados')

# Remover itens duplicados de uma lista
lista_unica = Utilitarios.remover_duplicados([1, 2, 2, 3, 3, 3])

