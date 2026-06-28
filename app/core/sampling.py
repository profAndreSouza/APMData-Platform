"""
Módulo de Amostragem de Logs para APM.
Estes exercícios devem ser preenchidos pelos alunos na Semana 4.
"""
import random

def amostragem_aleatoria_simples(dados: list, n: int, seed: int = None) -> list:
    """
    Retorna uma amostra aleatória simples de tamanho 'n' dos logs da API.
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")


def amostragem_sistematica(dados: list, n: int, ponto_partida: int = 0) -> list:
    """
    Realiza uma amostragem sistemática dos logs para reduzir o custo de processamento.
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")


def amostragem_estratificada(dados: list[dict], chave_estrato: str, proporcao: float, seed: int = None) -> list:
    """
    Realiza amostragem estratificada proporcional sobre uma lista de dicionários (estrato por endpoint).
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")
