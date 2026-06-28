"""
Módulo de Estatística Descritiva e Tendência Central para APM.
Estes exercícios devem ser preenchidos pelos alunos nas Semanas 2 e 3.
"""

def calcular_media(valores: list[float]) -> float:
    """
    Calcula a latência/métrica média da API.
    Regra: Não utilize funções prontas do Python (como sum() ou statistics.mean).
    
    Exemplo:
    >>> calcular_media([120.0, 150.0, 300.0])
    190.0
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")


def calcular_mediana(valores: list[float]) -> float:
    """
    Calcula a latência mediana (P50) dos tempos de resposta.
    Regra: Implemente a ordenação manual ou use sorted(), mas não utilize statistics.median.
    Trate listas de tamanho par e ímpar separadamente.
    
    Exemplo:
    >>> calcular_mediana([300.0, 100.0, 150.0])
    150.0
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")


def calcular_moda(valores: list[float]) -> list[float]:
    """
    Retorna uma lista contendo a(s) moda(s) dos códigos de status ou latências.
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")


def calcular_percentil(valores: list[float], p: float) -> float:
    """
    Calcula o percentil 'p' (ex: 95 para P95, 99 para P99) dos tempos de resposta.
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")


def calcular_amplitude(valores: list[float]) -> float:
    """
    Retorna a diferença entre a maior e a menor latência da lista.
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")


def calcular_variancia(valores: list[float], amostral: bool = True) -> float:
    """
    Calcula a variância amostral ou populacional para medir o Jitter (oscilação).
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")


def calcular_desvio_padrao(valores: list[float], amostral: bool = True) -> float:
    """
    Calcula o desvio padrão com base na variância do tempo de resposta.
    """
    # TODO: O aluno deve implementar a lógica aqui
    raise NotImplementedError("Método não implementado.")
