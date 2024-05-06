import os
import json
import hashlib
import re
import requests
from datetime import datetime

class Utilitarios:
    @staticmethod
    def ler_arquivo(caminho):
        with open(caminho, 'r') as arquivo:
            return arquivo.read()

    @staticmethod
    def escrever_arquivo(caminho, conteudo):
        with open(caminho, 'w') as arquivo:
            arquivo.write(conteudo)

    @staticmethod
    def ler_json(caminho):
        with open(caminho, 'r') as arquivo:
            return json.load(arquivo)

    @staticmethod
    def escrever_json(caminho, conteudo):
        with open(caminho, 'w') as arquivo:
            json.dump(conteudo, arquivo)

    @staticmethod
    def listar_arquivos(diretorio):
        return os.listdir(diretorio)

    @staticmethod
    def criar_diretorio(diretorio):
        os.makedirs(diretorio, exist_ok=True)

    @staticmethod
    def requisicao_get(url):
        resposta = requests.get(url)
        return resposta.json()

    @staticmethod
    def gerar_hash(texto):
        return hashlib.sha256(texto.encode()).hexdigest()

    @staticmethod
    def encontrar_ocorrencias(texto, padrao):
        return re.findall(padrao, texto)

    @staticmethod
    def remover_duplicados(lista):
        return list(set(lista))

    @staticmethod
    def ordenar_lista(lista, decrescente=False):
        return sorted(lista, reverse=decrescente)

    @staticmethod
    def formatar_data(data, formato):
        return data.strftime(formato)

    @staticmethod
    def obter_data_atual():
        return datetime.now()

    @staticmethod
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
