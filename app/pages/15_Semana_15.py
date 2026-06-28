import streamlit as st

st.set_page_config(page_title="Semana 15: Apresentação Final", page_icon="🎓", layout="wide")

st.title("Semana 15: Defesa Final de Produção & FinOps")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Defesa do Projeto Integrador</h3>
    <p>Apresentação final do painel de monitoramento de APM rodando em produção na nuvem da AWS, com todos os algoritmos estatísticos preenchidos e validados pela esteira de CI/CD automatizada no GitHub Actions, acompanhado da estimativa e defesa de custos (FinOps) do sistema.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Entrega Final")
st.info("Apresentar a arquitetura completa ao professor e à banca. Demonstrar a esteira rodando em tempo real com commit provocando o auto-deploy.")

st.subheader("🔍 Status do Semestre")
if st.button("🎉 Concluir Semestre e Gerar Celebração!"):
    st.balloons()
    st.success("Parabéns a toda a turma! O projeto integrador APMData foi entregue com excelência na nuvem!")
