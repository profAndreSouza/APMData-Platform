"""
Módulo de Séries Temporais e Regressão para APM.
Implementação de referência para a branch de exemplo.
"""
import math
from scipy import stats
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

def calcular_correlacao_pearson(x: list[float], y: list[float]) -> float:
    """
    Calcula o coeficiente de correlação de Pearson entre tráfego (Req/s) e consumo de CPU.
    """
    if not x or not y or len(x) != len(y):
        return 0.0
    n = len(x)
    media_x = sum(x) / n
    media_y = sum(y) / n
    
    num = sum((xi - media_x) * (yi - media_y) for xi, yi in zip(x, y))
    den_x = sum((xi - media_x) ** 2 for xi in x)
    den_y = sum((yi - media_y) ** 2 for yi in y)
    
    denominador = math.sqrt(den_x * den_y)
    if denominador == 0.0:
        return 0.0
    return num / denominador


def calcular_correlacao_spearman(x: list[float], y: list[float]) -> float:
    """
    Calcula o coeficiente de correlação de Spearman.
    """
    res = stats.spearmanr(x, y)
    return float(res.statistic)


def decompor_serie_temporal(dados_serie: pd.Series, periodo: int) -> tuple[pd.Series, pd.Series, pd.Series]:
    """
    Decompõe uma série temporal de uso de CPU (Tendência, Sazonalidade e Resíduos).
    """
    res = seasonal_decompose(dados_serie, period=periodo, extrapolate_trend='freq')
    return res.trend, res.seasonal, res.resid


def ajuste_regressao_linear(x: list[float], y: list[float]) -> tuple[float, float]:
    """
    Ajusta a linha de tendência (y = a*x + b) para previsão de uso de CPU/RAM (Capacity Planning).
    """
    if not x or not y or len(x) != len(y):
        return 0.0, 0.0
    n = len(x)
    media_x = sum(x) / n
    media_y = sum(y) / n
    
    num = sum((xi - media_x) * (yi - media_y) for xi, yi in zip(x, y))
    den = sum((xi - media_x) ** 2 for xi in x)
    
    if den == 0.0:
        return 0.0, media_y
        
    a = num / den
    b = media_y - a * media_x
    return a, b
