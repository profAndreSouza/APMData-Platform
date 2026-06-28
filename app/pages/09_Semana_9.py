import streamlit as st

st.set_page_config(page_title="Semana 9: Séries Temporais & Serverless", page_icon="⚡", layout="wide")

st.title("Semana 9: Sazonalidade & Custos Serverless")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Séries Temporais: Componentes temporais (tendência, sazonalidade, ruído) aplicados ao tráfego de requisições.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS Lambda & API Gateway. Análise de custos comparativa: Serverless vs Servidor Dedicado 24/7.</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Deploy Serverless: Automatizar o deploy de funções Lambda pelo GitHub Actions.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Desenvolver uma função simples em Python para rodar como Lambda na AWS. Estimar o custo de rodar essa função comparado a manter uma instância EC2 rodando direto.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")
st.info("ℹ️ Atividade validada por meio de entrega dos relatórios de custos e códigos Serverless no repositório.")
