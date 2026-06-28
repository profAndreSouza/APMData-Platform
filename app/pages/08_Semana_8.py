import streamlit as st
from utils.helpers import testar_funcao, exibir_codigo_funcao

# Importações do aluno
calcular_correlacao_pearson = None
try:
    import core.time_series as core_time_series
    calcular_correlacao_pearson = getattr(core_time_series, 'calcular_correlacao_pearson', None)
except ImportError:
    try:
        import app.core.time_series as core_time_series
        calcular_correlacao_pearson = getattr(core_time_series, 'calcular_correlacao_pearson', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 8: Correlação & CD EC2", page_icon="🔗", layout="wide")

st.title("Semana 8: Correlação & Custos CloudWatch")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Coeficiente de correlação de Pearson para avaliar a relação linear entre CPU e tráfego.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS CloudWatch Metrics. Custos de observabilidade (precificação de logs por GB ingerido e alarmes).</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Entrega Contínua (CD) simples para EC2: Script SSH para puxar imagens compiladas do Docker Hub.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar `calcular_correlacao_pearson` em `app/core/time_series.py`. Integrar o script de deploy automatizado por SSH na pipeline do GitHub Actions.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_pe = testar_funcao(calcular_correlacao_pearson, [1, 2, 3], [2, 4, 6])

# Exibe o código-fonte detectado
exibir_codigo_funcao(calcular_correlacao_pearson, "calcular_correlacao_pearson")

if status_pe == "NotImplemented":
    st.error("🔴 PENDENTE: Coeficiente de correlação de Pearson não implementado em `time_series.py`.")
else:
    try:
        cor = calcular_correlacao_pearson([1, 2, 3], [2, 4, 6])
        if abs(cor - 1.0) < 0.0001:
            st.success("🟢 CONCLUÍDO: Cálculo de correlação linear (Pearson) validado com sucesso!")
        else:
            st.warning("⚠️ AJUSTES NECESSÁRIOS: O coeficiente de Pearson não retornou 1.0 para dados perfeitamente lineares.")
    except Exception as e:
        st.error(f"Erro ao validar implementação: {e}")

st.markdown("---")
st.header("🧬 Conteúdo Estatístico Detalhado")

# Dados de Exemplo
tráfego_reqs = [10.0, 20.0, 30.0, 40.0, 50.0]
uso_cpu = [12.0, 22.0, 44.0, 61.0, 85.0]

col_data1, col_data2 = st.columns(2)
with col_data1:
    st.write(f"**Variável Independente X (Requisições por segundo):** `{tráfego_reqs}`")
with col_data2:
    st.write(f"**Variável Dependente Y (% Uso de CPU):** `{uso_cpu}`")

# Card da Correlação de Pearson
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Coeficiente de Correlação de Pearson (r)")
        st.markdown("""
        **Conceito**: Mede o grau e a direção da associação linear entre duas variáveis quantitativas contínuas. 
        
        *   **$r = 1$**: Correlação linear positiva perfeita.
        *   **$r = 0$**: Ausência de correlação linear.
        *   **$r = -1$**: Correlação linear negativa perfeita.
        
        **Fórmula Matemática**:
        $$r = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sqrt{\\sum (x_i - \\bar{x})^2 \\sum (y_i - \\bar{y})^2}}$$
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_pe != "NotImplemented":
            try:
                res_cor = calcular_correlacao_pearson(tráfego_reqs, uso_cpu)
                st.info(f"💡 **Pearson (r) calculado**: `{res_cor:.4f}`")
            except Exception as e:
                st.error(f"Erro no cálculo: {e}")
        else:
            st.warning("⚠️ Aguardando implementação para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado**:
        O valor calculado de **~0.992** é extremamente próximo de **1.0**, indicando uma associação linear positiva quase perfeita. Isso prova estatisticamente que o consumo de CPU aumenta em proporção direta à quantidade de chamadas que chegam.
        
        **Importância no APM**:
        Comprova que a infraestrutura se comporta de forma previsível e linear. Caso o tráfego continue aumentando, o consumo de CPU também aumentará de forma correspondente, justificando o provisionamento preventivo de Auto-Scaling horizontal para tratar sobrecargas futuras.
        """)
