import pytest
from app.core.stats import (
    calcular_media,
    calcular_mediana,
    calcular_moda,
    calcular_percentil,
    calcular_amplitude,
    calcular_variancia,
    calcular_desvio_padrao
)

def test_calcular_media():
    assert calcular_media([10.0, 20.0, 30.0]) == 20.0
    assert pytest.approx(calcular_media([1.5, 2.5, 3.5]), 0.001) == 2.5

def test_calcular_mediana_impar():
    assert calcular_mediana([3.0, 1.0, 2.0]) == 2.0

def test_calcular_mediana_par():
    assert calcular_mediana([1.0, 2.0, 3.0, 4.0]) == 2.5

def test_calcular_moda():
    assert calcular_moda([1, 2, 2, 3]) == [2.0]
    # Caso bimodal
    assert sorted(calcular_moda([1, 1, 2, 2, 3])) == [1.0, 2.0]

def test_calcular_percentil():
    dados = [15, 20, 35, 40, 50]
    assert pytest.approx(calcular_percentil(dados, 40), 0.001) == 29.0
    assert pytest.approx(calcular_percentil(dados, 50), 0.001) == 35.0

def test_calcular_amplitude():
    assert calcular_amplitude([5, 10, 15, 3]) == 12.0

def test_calcular_variancia_amostral():
    dados = [10, 12, 23, 23, 16, 23, 21, 16]
    # Variância amostral (divisor N-1)
    assert pytest.approx(calcular_variancia(dados, amostral=True), 0.001) == 27.42857

def test_calcular_variancia_populacional():
    dados = [10, 12, 23, 23, 16, 23, 21, 16]
    # Variância populacional (divisor N)
    assert pytest.approx(calcular_variancia(dados, amostral=False), 0.001) == 24.0

def test_calcular_desvio_padrao():
    dados = [10, 12, 23, 23, 16, 23, 21, 16]
    var_amostral = calcular_variancia(dados, amostral=True)
    import math
    assert pytest.approx(calcular_desvio_padrao(dados, amostral=True), 0.001) == math.sqrt(var_amostral)
