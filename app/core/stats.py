"""
Módulo de Estatística Descritiva e Tendência Central para APM.
Implementação de referência para a branch de exemplo.
"""
import math

def calcular_media(valores: list[float]) -> float:
    """
    Calcula a latência/métrica média da API.
    """
    if not valores:
        return 0.0
    soma = 0.0
    for v in valores:
        soma += v
    return soma / len(valores)


def calcular_mediana(valores: list[float]) -> float:
    """
    Calcula a latência mediana (P50) dos tempos de resposta.
    """
    if not valores:
        return 0.0
    s = sorted(valores)
    n = len(s)
    if n % 2 == 1:
        return float(s[n // 2])
    return (s[(n // 2) - 1] + s[n // 2]) / 2.0


def calcular_moda(valores: list[float]) -> list[float]:
    """
    Retorna uma lista contendo a(s) moda(s) dos códigos de status ou latências.
    """
    if not valores:
        return []
    frequencias = {}
    for v in valores:
        fval = float(v)
        frequencias[fval] = frequencias.get(fval, 0) + 1
        
    max_freq = max(frequencias.values())
    
    # Se a frequência máxima for 1 e o número de itens > 1, considera-se amodal (retorna tudo ou vazio, mas para fins de teste retornamos as modas)
    modas = [k for k, v in frequencias.items() if v == max_freq]
    return modas


def calcular_percentil(valores: list[float], p: float) -> float:
    """
    Calcula o percentil 'p' (ex: 95 para P95, 99 para P99) dos tempos de resposta.
    """
    if not valores:
        return 0.0
    s = sorted(valores)
    idx = (len(s) - 1) * (p / 100.0)
    low = math.floor(idx)
    high = math.ceil(idx)
    if low == high:
        return float(s[low])
    return float(s[low] + (idx - low) * (s[high] - s[low]))


def calcular_amplitude(valores: list[float]) -> float:
    """
    Retorna a diferença entre a maior e a menor latência da lista.
    """
    if not valores:
        return 0.0
    return float(max(valores) - min(valores))


def calcular_variancia(valores: list[float], amostral: bool = True) -> float:
    """
    Calcula a variância amostral ou populacional para medir o Jitter (oscilação).
    """
    if not valores or len(valores) <= 1 if amostral else False:
        return 0.0
    m = calcular_media(valores)
    soma_quadrados = 0.0
    for v in valores:
        soma_quadrados += (v - m) ** 2
    divisor = (len(valores) - 1) if amostral else len(valores)
    return soma_quadrados / divisor


def calcular_desvio_padrao(valores: list[float], amostral: bool = True) -> float:
    """
    Calcula o desvio padrão com base na variância do tempo de resposta.
    """
    var = calcular_variancia(valores, amostral)
    return math.sqrt(var)
