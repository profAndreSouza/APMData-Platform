"""
Módulo de Testes de Hipóteses de APM.
Implementação de referência para a branch de exemplo.
"""
from scipy import stats

def teste_shapiro_wilk(valores: list[float]) -> tuple[float, float, bool]:
    """
    Executa o teste de Shapiro-Wilk para verificar se as latências da API seguem uma distribuição normal.
    """
    if len(valores) < 3:
        return 0.0, 1.0, True
    stat, p_val = stats.shapiro(valores)
    return stat, p_val, bool(p_val >= 0.05)


def teste_kolmogorov_smirnov(valores: list[float]) -> tuple[float, float, bool]:
    """
    Executa o teste de Kolmogorov-Smirnov comparando os tempos de resposta com a distribuição normal padronizada.
    """
    if len(valores) == 0:
        return 0.0, 1.0, True
    
    # Padronização dos dados (Z-score)
    mean = sum(valores) / len(valores)
    variance = sum((x - mean) ** 2 for x in valores) / len(valores)
    std = variance ** 0.5
    
    if std == 0:
        return 0.0, 1.0, True
        
    z_scores = [(x - mean) / std for x in valores]
    stat, p_val = stats.kstest(z_scores, 'norm')
    return stat, p_val, bool(p_val >= 0.05)


def teste_qui_quadrado_associacao(tabela_contingencia: list[list[int]]) -> tuple[float, float, bool]:
    """
    Realiza o teste do Qui-Quadrado para verificar se há associação entre duas variáveis categóricas.
    """
    stat, p_val, dof, expected = stats.chi2_contingency(tabela_contingencia)
    # Se p_valor < 0.05, há associação estatisticamente significativa
    ha_associacao = bool(p_val < 0.05)
    return stat, p_val, ha_associacao
