import pytest
import pandas as pd
import numpy as np
from app.core.time_series import (
    calcular_correlacao_pearson,
    calcular_correlacao_spearman,
    decompor_serie_temporal,
    ajuste_regressao_linear
)

def test_calcular_correlacao_pearson():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    assert pytest.approx(calcular_correlacao_pearson(x, y), 0.001) == 1.0
    
    # Inversa
    y_inv = [10, 8, 6, 4, 2]
    assert pytest.approx(calcular_correlacao_pearson(x, y_inv), 0.001) == -1.0

def test_calcular_correlacao_spearman():
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 30, 25]  # Não perfeitamente linear, mas monotônica
    # Spearman deve ser próximo de 1.0 (ou exatamente correspondente)
    val = calcular_correlacao_spearman(x, y)
    assert val > 0.8

def test_decompor_serie_temporal():
    # Cria uma série temporal com tendência e sazonalidade explícitas
    tempo = pd.date_range(start="2026-01-01", periods=100, freq="D")
    t = np.arange(100)
    sazonalidade = 10 * np.sin(2 * np.pi * t / 7) # Sazonalidade de 7 dias
    tendencia = 0.5 * t
    ruido = np.random.normal(scale=1, size=100)
    
    valores = tendencia + sazonalidade + ruido
    serie = pd.Series(valores, index=tempo)
    
    tend, saz, res = decompor_serie_temporal(serie, periodo=7)
    assert isinstance(tend, pd.Series)
    assert isinstance(saz, pd.Series)
    assert isinstance(res, pd.Series)
    assert len(tend) == len(serie)

def test_ajuste_regressao_linear():
    x = [1, 2, 3]
    y = [2, 4, 5]
    a, b = ajuste_regressao_linear(x, y)
    # y = 1.5 * x + 0.667
    assert pytest.approx(a, 0.01) == 1.5
    assert pytest.approx(b, 0.01) == 0.667
