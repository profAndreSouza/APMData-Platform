import streamlit as st
from utils.helpers import testar_funcao, exibir_codigo_funcao

# Importações do aluno
teste_shapiro_wilk = None
try:
    import core.hypothesis as core_hypothesis
    teste_shapiro_wilk = getattr(core_hypothesis, 'teste_shapiro_wilk', None)
except ImportError:
    try:
        import app.core.hypothesis as core_hypothesis
        teste_shapiro_wilk = getattr(core_hypothesis, 'teste_shapiro_wilk', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 6: Normalidade & RDS", page_icon="🧬", layout="wide")

st.title("Semana 6: Normalidade & RDS vs EC2 Pricing")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Teste de hipóteses de aderência (Shapiro-Wilk) para provar se a latência é normal.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> Instanciação de Amazon RDS PostgreSQL. Comparativo de custo: rodar banco no EC2 (IaaS) vs RDS (PaaS).</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Testes unitários de validação estatística integrados na pipeline de CI do GitHub Actions.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar `teste_shapiro_wilk` em `app/core/hypothesis.py`. Conectar a aplicação ao banco de dados Amazon RDS PostgreSQL provisionado.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_shap = testar_funcao(teste_shapiro_wilk, [1.0, 2.0, 3.0, 4.0, 5.0])

# Exibe o código-fonte detectado
exibir_codigo_funcao(teste_shapiro_wilk, "teste_shapiro_wilk")

if status_shap == "NotImplemented":
    st.error("🔴 PENDENTE: Teste de Shapiro-Wilk não implementado em `hypothesis.py`.")
else:
    st.success("🟢 CONCLUÍDO: Função `teste_shapiro_wilk` validada com sucesso!")

st.markdown("---")
st.subheader("💡 Guia de Teoria e Interpretação (APM)")

st.markdown("""
#### 📐 Teste de Normalidade de Shapiro-Wilk
*   **Teoria**: Testa a hipótese nula ($H_0$) de que uma amostra provém de uma população com distribuição normal. Se o valor-p retornado for menor que o nível de significância (alfa = 0.05), rejeitamos $H_0$ e concluímos que os dados não seguem uma distribuição normal.
*   **Na Aplicação (APM - Latência de Resposta)**: Tempos de resposta de software raramente seguem distribuições normais; eles costumam ser log-normais ou multimodais. Provar estatisticamente que a latência não é normal justifica a necessidade de usar **percentis (P95 e P99)** no monitoramento diário em vez de confiar na latência média para avaliar a satisfação real dos usuários da API.
""")
