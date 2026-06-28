import streamlit as st

st.set_page_config(page_title="Semana 1: Setup & Git", page_icon="📚", layout="wide")

st.title("Semana 1: Introdução ao Projeto e Setup")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Apresentação do dataset de telemetria APM (latência, CPU, RAM). Escalas de medição (Nominal, Ordinal, Intervalar e Razão).</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS Pricing Calculator e estrutura geral de cobrança (Pay-as-you-go, Free Tier).</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Cultura DevOps. Introdução ao versionamento de código com Git.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Realizar o fork do repositório, clonar localmente e configurar o ambiente virtual do Python (pip install -r requirements.txt).")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")
st.info("ℹ️ Semana de Setup. Nenhuma função de código estatístico é validada nesta semana.")
