import pytest
import numpy as np
from app.core import hypothesis

def test_teste_shapiro_wilk_normal():
    # Amostra de distribuição perfeitamente normal
    np.random.seed(42)
    valores = np.random.normal(loc=50, scale=5, size=100).tolist()
    est, p_val, e_normal = hypothesis.teste_shapiro_wilk(valores)
    # Deve ser normal (p >= 0.05)
    assert e_normal is True
    assert p_val >= 0.05

def test_teste_shapiro_wilk_nao_normal():
    # Amostra de distribuição uniforme (não normal)
    np.random.seed(42)
    valores = np.random.uniform(low=10, high=100, size=100).tolist()
    est, p_val, e_normal = hypothesis.teste_shapiro_wilk(valores)
    # Provavelmente rejeitará a normalidade
    assert e_normal is False
    assert p_val < 0.05

def test_teste_qui_quadrado_associacao():
    # Tabela com forte associação
    #              Turno Manhã | Turno Noite
    # Alertas Sim       80     |     10
    # Alertas Não       20     |     90
    tabela = [
        [80, 10],
        [20, 90]
    ]
    est, p_val, ha_associacao = hypothesis.teste_qui_quadrado_associacao(tabela)
    assert ha_associacao is True
    assert p_val < 0.001

