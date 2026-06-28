"""
Módulo de Testes de Hipóteses de APM.
Estes exercícios devem ser preenchidos pelos alunos nas Semanas 6 e 7.
"""
from scipy import stats

def teste_shapiro_wilk(valores: list[float]) -> tuple[float, float, bool]:
    """
    Executa o teste de Shapiro-Wilk para verificar se as latências da API seguem uma distribuição normal.
    Retorna (estatistica, p_valor, e_normal).
    """
    # TODO: O aluno deve utilizar scipy.stats.shapiro e tomar a decisão
    raise NotImplementedError("Método não implementado.")


def teste_kolmogorov_smirnov(valores: list[float]) -> tuple[float, float, bool]:
    """
    Executa o teste de Kolmogorov-Smirnov comparando os tempos de resposta com a distribuição normal padronizada.
    """
    # TODO: O aluno deve normalizar os valores e aplicar scipy.stats.kstest
    raise NotImplementedError("Método não implementado.")


def teste_qui_quadrado_associacao(tabela_contingencia: list[list[int]]) -> tuple[float, float, bool]:
    """
    Realiza o teste do Qui-Quadrado para verificar se há associação entre Endpoint e erros HTTP 500.
    """
    # TODO: O aluno deve utilizar scipy.stats.chi2_contingency
    raise NotImplementedError("Método não implementado.")
