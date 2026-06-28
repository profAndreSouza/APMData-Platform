"""
Módulo de Amostragem de Logs para APM.
Implementação de referência para a branch de exemplo.
"""
import random

def amostragem_aleatoria_simples(dados: list, n: int, seed: int = None) -> list:
    """
    Retorna uma amostra aleatória simples de tamanho 'n' dos logs da API.
    """
    if seed is not None:
        random.seed(seed)
    # Garante que n não exceda o tamanho dos dados
    n_sample = min(n, len(dados))
    return random.sample(dados, n_sample)


def amostragem_sistematica(dados: list, n: int, ponto_partida: int = 0) -> list:
    """
    Realiza uma amostragem sistemática dos logs para reduzir o custo de processamento.
    """
    if not dados or n <= 0:
        return []
    k = len(dados) // n
    amostra = []
    for i in range(n):
        idx = ponto_partida + i * k
        if idx < len(dados):
            amostra.append(dados[idx])
    return amostra


def amostragem_estratificada(dados: list[dict], chave_estrato: str, proporcao: float, seed: int = None) -> list:
    """
    Realiza amostragem estratificada proporcional sobre uma lista de dicionários (estrato por endpoint).
    """
    if seed is not None:
        random.seed(seed)
        
    # Agrupa os dados por estrato
    estratos = {}
    for item in dados:
        val = item.get(chave_estrato)
        if val not in estratos:
            estratos[val] = []
        estratos[val].append(item)
        
    amostra_final = []
    # Para cada grupo/estrato, extrai a amostra proporcional
    for chave, itens in estratos.items():
        n_amostra = int(len(itens) * proporcao)
        if n_amostra > 0:
            amostra_final.extend(random.sample(itens, n_amostra))
            
    return amostra_final
