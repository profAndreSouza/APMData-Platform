import streamlit as st
from utils.helpers import testar_funcao

# Importações do aluno
amostragem_sistematica = None
try:
    import core.sampling as core_sampling
    amostragem_sistematica = getattr(core_sampling, 'amostragem_sistematica', None)
except ImportError:
    try:
        import app.core.sampling as core_sampling
        amostragem_sistematica = getattr(core_sampling, 'amostragem_sistematica', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 4: Amostragem & Redes", page_icon="🌐", layout="wide")

st.title("Semana 4: Amostragem & Custos de Rede")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Métodos de Amostragem (Aleatória, Sistemática, Estratificada) para otimização de processamento de logs.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS VPC (Virtual Private Cloud), Security Groups e **Data Transfer Costs** (custos de tráfego entre AZs e IPs públicos).</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Docker Compose: Orquestração de múltiplos containers (App Streamlit + Banco PostgreSQL local).</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar as funções de `amostragem_sistematica` e `amostragem_estratificada` em `app/core/sampling.py` para reduzir a base de análise do APM.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_sis = testar_funcao(amostragem_sistematica, [1, 2, 3, 4, 5, 6], 2)

if status_sis == "NotImplemented":
    st.error("🔴 PENDENTE: Algoritmo `amostragem_sistematica` pendente de implementação em `sampling.py`.")
else:
    try:
        amostra = amostragem_sistematica([1, 2, 3, 4, 5, 6, 7, 8], 2, ponto_partida=0)
        if amostra == [1, 5]:
            st.success("🟢 CONCLUÍDO: Algoritmo de Amostragem Sistemática validado com sucesso!")
        else:
            st.warning(f"⚠️ AJUSTES NECESSÁRIOS: Amostragem retornou {amostra} mas o esperado para passo k=4 era [1, 5].")
    except Exception as e:
        st.error(f"Erro ao validar implementação: {e}")
