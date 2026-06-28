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
st.subheader("💡 Guia de Teoria e Interpretação (APM)")

st.markdown("""
#### 📐 Coeficiente de Correlação de Pearson
*   **Teoria**: Mede o grau e a direção da relação linear entre duas variáveis quantitativas contínuas. O coeficiente $r$ varia de -1 (correlação linear negativa perfeita) a +1 (correlação linear positiva perfeita), com 0 indicando nenhuma correlação linear.
*   **Na Aplicação (APM - Consumo de Hardware)**: Avalia o impacto do tráfego na máquina. Ao calcular a correlação entre a taxa de requisições por segundo (Req/s) e a porcentagem de uso de CPU, uma correlação próxima de +1 prova que a carga do servidor está respondendo diretamente ao uso dos clientes, sinalizando comportamento previsível e indicando que otimizações de código ou escalabilidade horizontal (Auto-Scaling) resolverão problemas de sobrecarga.
""")
