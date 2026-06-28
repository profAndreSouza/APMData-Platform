import streamlit as st

st.set_page_config(page_title="Semana 14: Observabilidade", page_icon="📈", layout="wide")

st.title("Semana 14: Observabilidade & Otimização de Custos (FinOps)")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Análise crítica consolidada das métricas da infraestrutura e relatórios de APM.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS Well-Architected Framework: Foco total no pilar de **Cost Optimization** (Otimização de Custos).</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Monitoramento e observabilidade: Conceitos de exportação de métricas com Prometheus e Grafana.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Revisar a arquitetura da aplicação para identificar desperdícios de custos em instâncias sobredimensionadas. Preparar o relatório final de FinOps com estimativas de custos.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")
st.success("✅ Dashboard consolidado! O repositório está pronto para a entrega final de produção.")
