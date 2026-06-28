"""
Módulo de Séries Temporais e Regressão para APM.
Estes exercícios devem ser preenchidos pelos alunos nas Semanas 8, 9, 10 e 11.
"""
import math
from scipy import stats
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

def calcular_correlacao_pearson(x: list[float], y: list[float]) -> float:
    """
    Calcula o coeficiente de correlação de Pearson entre tráfego (Req/s) e consumo de CPU.
    """
    # TODO: O aluno deve implementar a fórmula matemática clássica de Pearson
    raise NotImplementedError("Método não implementado.")


def calcular_correlacao_spearman(x: list[float], y: list[float]) -> float:
    """
    Calcula o coeficiente de correlação de Spearman.
    """
    # TODO: O aluno deve implementar ou usar scipy
    raise NotImplementedError("Método não implementado.")


def decompor_serie_temporal(dados_serie: pd.Series, periodo: int) -> tuple[pd.Series, pd.Series, pd.Series]:
    """
    Decompõe uma série temporal de uso de CPU (Tendência, Sazonalidade e Resíduos).
    """
    # TODO: O aluno deve utilizar a função seasonal_decompose da biblioteca statsmodels
    raise NotImplementedError("Método não implementado.")


def ajuste_regressao_linear(x: list[float], y: list[float]) -> tuple[float, float]:
    """
    Ajusta a linha de tendência (y = a*x + b) para previsão de uso de CPU/RAM (Capacity Planning).
    """
    # TODO: O aluno deve implementar a fórmula MQO clássica
    raise NotImplementedError("Método não implementado.")
