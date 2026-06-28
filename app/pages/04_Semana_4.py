import streamlit as st
from utils.helpers import testar_funcao, exibir_codigo_funcao

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

# Exibe o código-fonte detectado
exibir_codigo_funcao(amostragem_sistematica, "amostragem_sistematica")

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

st.markdown("---")
st.header("🧬 Conteúdo Estatístico Detalhado")

# Amostra para demonstração
dados_logs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
st.write(f"**População Completa de Métricas de Latência (12 registros):** `{dados_logs}`")

# Card da Amostragem Sistemática
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Amostragem Sistemática")
        st.markdown("""
        **Conceito**: Seleção de elementos a partir de um intervalo regular fixo chamado **passo** ($k = N/n$). Após a definição de um ponto inicial ($i$), seleciona-se cada $k$-ésimo item para formar a amostra.
        
        **Fórmula Matemática**:
        $$Passo \\ (k) = \\lfloor \\frac{N}{n} \\rfloor$$
        $$Amostra = \\{ x_{i + j \\cdot k} \\} \\quad \\text{para } j = 0, 1, \\dots, n - 1$$
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        st.markdown("Configuração do teste: obter amostra de tamanho **$n = 4$**, partindo do índice **$i = 0$**.")
        if status_sis != "NotImplemented":
            try:
                res_amostra = amostragem_sistematica(dados_logs, 4, ponto_partida=0)
                st.info(f"💡 **Amostra Sistemática Extraída**: `{res_amostra}`")
            except Exception as e:
                st.error(f"Erro no cálculo: {e}")
        else:
            st.warning("⚠️ Aguardando implementação para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado**:
        Com $N = 12$ e $n = 4$, o passo de salto foi calculado como $12 / 4 = 3$. Partindo do índice 0 (valor 10) e somando 3 posições a cada passo, coletamos as latências nos índices: 0 (valor 10), 3 (valor 40), 6 (valor 70) e 9 (valor 100). Isso nos dá a amostra `[10, 40, 70, 100]`.
        
        **Importância no APM**:
        Em produção, armazenar 100% dos logs de requisições acarreta custos enormes na AWS. Ao programar uma amostragem sistemática periódica para capturar apenas uma requisição a cada 3 passagens, reduzimos os dados enviados no pipeline de DevOps em **66%**, mas preservamos a representatividade dos dados para análises estatísticas.
        """)
