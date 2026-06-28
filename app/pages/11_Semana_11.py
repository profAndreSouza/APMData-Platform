import streamlit as st
from utils.helpers import testar_funcao

# Importações do aluno
ajuste_regressao_linear = None
try:
    import core.time_series as core_time_series
    ajuste_regressao_linear = getattr(core_time_series, 'ajuste_regressao_linear', None)
except ImportError:
    try:
        import app.core.time_series as core_time_series
        ajuste_regressao_linear = getattr(core_time_series, 'ajuste_regressao_linear', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 11: Regressão & Auto-Scaling", page_icon="📈", layout="wide")

st.title("Semana 11: Capacity Planning & Fargate Pricing")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Regressão Linear Simples por Mínimos Quadrados para estimar quando a RAM/disco estourará.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS ELB (Load Balancers) e ASG (Auto Scaling). Fator de precificação do ECS (Fargate) por CPU/RAM hora.</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Deploy de Containers em larga escala: Configuração da esteira para deploy no AWS App Runner ou ECS Fargate.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar `ajuste_regressao_linear` em `app/core/time_series.py`. Rodar o deploy automatizado da aplicação para um serviço gerenciado escalável (App Runner/ECS).")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_reg = testar_funcao(ajuste_regressao_linear, [1, 2, 3], [2, 4, 5])

if status_reg == "NotImplemented":
    st.error("🔴 PENDENTE: Função `ajuste_regressao_linear` pendente em `time_series.py`.")
else:
    try:
        a, b = ajuste_regressao_linear([1, 2, 3], [2, 4, 5])
        if abs(a - 1.5) < 0.01:
            st.success("🟢 CONCLUÍDO: Função de regressão linear preditiva validada com sucesso!")
        else:
            st.warning("⚠️ AJUSTES NECESSÁRIOS: Os coeficientes calculados não batem com o gabarito matemático.")
    except Exception as e:
        st.error(f"Erro ao validar implementação: {e}")
