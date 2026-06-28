import streamlit as st

st.set_page_config(page_title="Semana 13: Dashboard Final & IaC", page_icon="🏗️", layout="wide")

st.title("Semana 13: Dashboard Final & Precificação de IaC")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Fechamento do Dashboard APM com as análises preditivas completas.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> Infraestrutura como Código (IaC). Conceitos de provisionamento automatizado.</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Criação de templates do Terraform/CloudFormation para subir a EC2 e o Bucket S3 via pipeline.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Escrever um script simplificado de Terraform (`main.tf`) para provisionar o bucket S3 do projeto e validar a execução sintática no workflow.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")
st.info("ℹ️ Atividade prática avaliada qualitativamente pelo professor via análise do código Terraform submetido.")
