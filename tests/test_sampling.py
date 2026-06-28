import pytest
from app.core.sampling import (
    amostragem_aleatoria_simples,
    amostragem_sistematica,
    amostragem_estratificada
)

def test_amostragem_aleatoria_simples():
    dados = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    amostra = amostragem_aleatoria_simples(dados, 5, seed=42)
    assert len(amostra) == 5
    for item in amostra:
        assert item in dados

def test_amostragem_sistematica():
    dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # N=12, n=4 -> passo k = 3
    # ponto_partida = 0 -> índices selecionados: 0, 3, 6, 9
    amostra = amostragem_sistematica(dados, 4, ponto_partida=0)
    assert amostra == [1, 4, 7, 10]

def test_amostragem_estratificada():
    dados = [
        {"sensor_id": "sensor_A", "valor": 10},
        {"sensor_id": "sensor_A", "valor": 12},
        {"sensor_id": "sensor_A", "valor": 11},
        {"sensor_id": "sensor_A", "valor": 13},
        {"sensor_id": "sensor_A", "valor": 14},
        {"sensor_id": "sensor_B", "valor": 20},
        {"sensor_id": "sensor_B", "valor": 21},
        {"sensor_id": "sensor_B", "valor": 22},
        {"sensor_id": "sensor_B", "valor": 23},
        {"sensor_id": "sensor_B", "valor": 24},
    ]
    # proporção de 40% (2 amostras por sensor, pois cada sensor possui 5 itens)
    amostra = amostragem_estratificada(dados, "sensor_id", 0.40, seed=42)
    assert len(amostra) == 4
    contagem = {}
    for item in amostra:
        sensor = item["sensor_id"]
        contagem[sensor] = contagem.get(sensor, 0) + 1
    assert contagem["sensor_A"] == 2
    assert contagem["sensor_B"] == 2
