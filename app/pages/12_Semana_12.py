import streamlit as st

st.set_page_config(page_title="Semana 12: Métricas & Segurança AWS", page_icon="🔒", layout="wide")

st.title("Semana 12: Métricas & Secrets Manager Pricing")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Métricas de erro de predição (MAE, MSE, RMSE) para validar o modelo de capacity planning.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS KMS e Secrets Manager. Custo fixo por segredo ativo e por chamadas à API de chaves.</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Secret Management: Configurar credenciais temporárias OIDC entre GitHub Actions e AWS para evitar chaves expostas.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Configurar o AWS Secrets Manager para gerenciar a senha do RDS. Integrar a leitura do segredo na aplicação Streamlit utilizando o Boto3.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")
st.success("✅ Segurança e segredos integrados! Valide o fluxo de credenciais seguras no pipeline de deploy.")
