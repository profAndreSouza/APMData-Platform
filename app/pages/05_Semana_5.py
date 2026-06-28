import streamlit as st

st.set_page_config(page_title="Semana 5: Visualização & CI", page_icon="📈", layout="wide")

st.title("Semana 5: Visualização & S3 Lifecycle Pricing")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Geração de visualizações gráficas (linhas, dispersão, histograma de tempos de resposta e boxplots).</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS S3. Precificação por classe de armazenamento e regras de ciclo de vida (Life Cycle Policies) para arquivamento barato de logs.</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Integração Contínua (CI): Configurar o primeiro workflow no GitHub Actions para rodar checagens linter na API.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Concluir os gráficos de telemetria do Dashboard e ativar a esteira de CI com Linter (Black/Flake8) disparando no git push.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")
st.success("✅ Dashboard estruturado! Certifique-se de que a automação do GitHub Actions (.github/workflows/ci.yml) está rodando sem erros no GitHub.")
