import streamlit as st
from utils.helpers import testar_funcao, exibir_codigo_funcao

# Importações do aluno
calcular_media = None
calcular_mediana = None
try:
    import core.stats as core_stats
    calcular_media = getattr(core_stats, 'calcular_media', None)
    calcular_mediana = getattr(core_stats, 'calcular_mediana', None)
except ImportError:
    try:
        import app.core.stats as core_stats
        calcular_media = getattr(core_stats, 'calcular_media', None)
        calcular_mediana = getattr(core_stats, 'calcular_mediana', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 2: Tendência Central", page_icon="📊", layout="wide")

# Custom CSS para estética premium
st.markdown("""
<style>
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    .metric-title {
        color: #ff5722;
        font-weight: bold;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Semana 2: Tendência Central & IAM")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Estatística Descritiva: Medidas de Tendência Central (Média, Mediana, Moda, Percentil, Quartil) sobre latências.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS Global Infrastructure (Regiões e AZs). Segurança e acesso seguro com AWS IAM (Políticas e Roles).</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Fluxos de Git e colaboração (Pull Requests, Code Review, Commits semânticos).</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar as funções `calcular_media` e `calcular_mediana` no arquivo `app/core/stats.py` sem usar funções de agregação prontas (ex: `sum()` ou `statistics.median()`).")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_media = testar_funcao(calcular_media, [10.0, 20.0, 30.0])
status_mediana = testar_funcao(calcular_mediana, [10.0, 20.0, 30.0])

# Exibe o código-fonte detectado
exibir_codigo_funcao(calcular_media, "calcular_media")
exibir_codigo_funcao(calcular_mediana, "calcular_mediana")

if status_media == "NotImplemented" or status_mediana == "NotImplemented":
    st.error("🔴 PENDENTE: As funções `calcular_media` ou `calcular_mediana` ainda não foram implementadas no arquivo `stats.py`.")
else:
    try:
        m_val = calcular_media([10.0, 20.0, 30.0])
        med_val = calcular_mediana([1.0, 3.0, 2.0])
        if m_val == 20.0 and med_val == 2.0:
            st.success("🟢 CONCLUÍDO: As funções `calcular_media` e `calcular_mediana` foram implementadas e retornam valores corretos!")
        else:
            st.warning("⚠️ AJUSTES NECESSÁRIOS: As funções foram criadas mas a lógica matemática está retornando valores incorretos.")
    except Exception as e:
        st.error(f"Erro ao validar implementação: {e}")

st.markdown("---")
st.header("🧬 Conteúdo Estatístico Detalhado")

# Amostra para demonstração
dados_exemplo = [100.0, 150.0, 120.0, 900.0, 130.0]
st.write(f"**Conjunto de Dados de Exemplo (Latências da API em ms):** `{dados_exemplo}`")

# 1. Card da Média
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Média Aritmética")
        st.markdown("""
        **Conceito**: Representa o ponto de equilíbrio matemático do conjunto de dados, calculado somando todos os valores e dividindo pelo total de observações.
        
        **Fórmula Matemática**:
        $$\\bar{x} = \\frac{\\sum_{i=1}^{n} x_i}{n}$$
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_media != "NotImplemented":
            try:
                res_media = calcular_media(dados_exemplo)
                st.info(f"💡 **Média Calculada**: `{res_media:.2f} ms`")
            except Exception as e:
                st.error(f"Erro ao calcular: {e}")
        else:
            st.warning("⚠️ Aguardando implementação da função para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado (Interpretação)**:
        O resultado da média foi fortemente puxado pelo valor de **900 ms** (um pico isolado de lentidão). Perceba que a média calculada (~280 ms) é significativamente maior do que 4 das 5 observações reais. Isso demonstra o risco de usar apenas a média aritmética no monitoramento de APM, pois outliers isolados mascaram o comportamento típico da aplicação.
        """)

# 2. Card da Mediana
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Mediana (P50)")
        st.markdown("""
        **Conceito**: Representa o valor central que divide o conjunto de dados ordenados exatamente em duas partes iguais (50% das observações menores e 50% maiores).
        
        **Fórmula Matemática**:
        $$Mediana = x_{\\frac{n+1}{2}} \\quad \\text{(para } n \\text{ ímpar)}$$
        $$Mediana = \\frac{x_{\\frac{n}{2}} + x_{\\frac{n}{2} + 1}}{2} \\quad \\text{(para } n \\text{ par)}$$
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_mediana != "NotImplemented":
            try:
                res_mediana = calcular_mediana(dados_exemplo)
                st.info(f"💡 **Mediana Calculada**: `{res_mediana:.2f} ms`")
            except Exception as e:
                st.error(f"Erro ao calcular: {e}")
        else:
            st.warning("⚠️ Aguardando implementação da função para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado (Interpretação)**:
        O cálculo ordenou os dados para `[100, 120, 130, 150, 900]` e pegou o valor central **130 ms**. Isso mostra que 50% dos usuários acessaram a API em até 130 ms. A mediana é imune a picos isolados (como o de 900 ms), tornando-se uma métrica muito mais fiel para representar a experiência padrão do usuário em sistemas de APM.
        """)
