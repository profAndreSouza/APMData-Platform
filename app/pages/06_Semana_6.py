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
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> Amazon RDS PostgreSQL. Comparativo de custo: rodar banco no EC2 (IaaS) vs RDS (PaaS).</p>
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
st.header("🧬 Conteúdo Estatístico Detalhado")

# Amostras para demonstração
latencias_normais = [120.0, 122.0, 118.0, 121.0, 119.0, 120.0, 123.0, 117.0, 121.0, 119.0]
st.write(f"**Conjunto de Teste de Latências Quase Estáveis em ms (n=10):** `{latencias_normais}`")

# Card do Shapiro-Wilk
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Teste de Shapiro-Wilk")
        st.markdown("""
        **Conceito**: É o teste estatístico mais poderoso para verificar se uma amostra de dados numéricos provém de uma distribuição normal (gaussiana). 
        
        *   **Hipótese Nula ($H_0$)**: A distribuição dos dados é Normal.
        *   **Hipótese Alternativa ($H_1$)**: A distribuição dos dados **não** é Normal.
        
        **Fórmula Matemática**:
        $$W = \\frac{\\left(\\sum_{i=1}^{n} a_i x_{(i)}\\right)^2}{\\sum_{i=1}^{n} (x_i - \\bar{x})^2}$$
        onde $x_{(i)}$ representa os dados ordenados e $a_i$ são constantes obtidas de covariâncias normais.
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_shap != "NotImplemented":
            try:
                stat, p_val, eh_normal = teste_shapiro_wilk(latencias_normais)
                st.info(f"💡 **Estatística W**: `{stat:.4f}` | **p-valor**: `{p_val:.4f}`")
                if eh_normal:
                    st.success("🟢 Decisão Estatística: Falha em rejeitar H0 (Os dados seguem distribuição Normal!)")
                else:
                    st.error("🔴 Decisão Estatística: Rejeita H0 (Os dados NÃO seguem distribuição Normal!)")
            except Exception as e:
                st.error(f"Erro no cálculo: {e}")
        else:
            st.warning("⚠️ Aguardando implementação para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado**:
        Como o p-valor obtido (**~0.817**) é maior que o nível de significância padrão de **0.05**, não podemos rejeitar a hipótese de normalidade. Isso indica que as oscilações de latência observadas decorrem apenas de ruídos naturais estáveis da rede, sem gargalos anormais ativos.
        
        Se o p-valor fosse menor que 0.05 (rejeitando a normalidade), isso sinalizaria que a média aritmética do tempo de resposta da API seria enganosa, e o time de SRE deveria obrigatoriamente guiar suas análises e alertas de infraestrutura utilizando percentis (como o P95 e P99).
        """)
