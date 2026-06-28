import streamlit as st
from utils.helpers import testar_funcao, exibir_codigo_funcao

# Importações do aluno
calcular_media = None
calcular_mediana = None
try:
    import core.stats as core_stats
    calcular_media = getattr(core_stats, 'calcular_media', None)
    calcular_mediana = getattr(core_stats, 'calcular_mediana', None)
except ImportError:
    try:
        import app.core.stats as core_stats
        calcular_media = getattr(core_stats, 'calcular_media', None)
        calcular_mediana = getattr(core_stats, 'calcular_mediana', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 2: Tendência Central", page_icon="📊", layout="wide")

st.title("Semana 2: Tendência Central & IAM")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Estatística Descritiva: Medidas de Tendência Central (Média, Mediana, Moda, Percentil, Quartil) sobre latências.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS Global Infrastructure (Regiões e AZs). Segurança e acesso seguro com AWS IAM (Políticas e Roles).</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Fluxos de Git e colaboração (Pull Requests, Code Review, Commits semânticos).</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar as funções `calcular_media` e `calcular_mediana` no arquivo `app/core/stats.py` sem usar funções de agregação prontas (ex: `sum()` ou `statistics.median()`).")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_media = testar_funcao(calcular_media, [10.0, 20.0, 30.0])
status_mediana = testar_funcao(calcular_mediana, [10.0, 20.0, 30.0])

# Exibe o código-fonte detectado
exibir_codigo_funcao(calcular_media, "calcular_media")
exibir_codigo_funcao(calcular_mediana, "calcular_mediana")

if status_media == "NotImplemented" or status_mediana == "NotImplemented":
    st.error("🔴 PENDENTE: As funções `calcular_media` ou `calcular_mediana` ainda não foram implementadas no arquivo `stats.py`.")
else:
    # Rodar testes de veracidade
    try:
        m_val = calcular_media([10.0, 20.0, 30.0])
        med_val = calcular_mediana([1.0, 3.0, 2.0])
        
        if m_val == 20.0 and med_val == 2.0:
            st.success("🟢 CONCLUÍDO: As funções `calcular_media` e `calcular_mediana` foram implementadas e retornam valores corretos!")
        else:
            st.warning("⚠️ AJUSTES NECESSÁRIOS: As funções foram criadas mas a lógica matemática está retornando valores incorretos.")
    except Exception as e:
        st.error(f"Erro ao validar implementação: {e}")

st.markdown("---")
st.subheader("💡 Guia de Teoria e Interpretação (APM)")

col_th1, col_th2 = st.columns(2)
with col_th1:
    st.markdown("""
    #### 📐 Média Aritmética
    *   **Teoria**: É a soma de todas as observações dividida pelo número total de elementos:
        $$\\bar{x} = \\frac{\\sum_{i=1}^{n} x_i}{n}$$
    *   **Na Aplicação (APM)**: Representa a latência média das requisições. Contudo, ela é muito sensível a *outliers* (valores extremos). Se uma única chamada travar por 10 segundos devido a um timeout de banco de dados, a latência média subirá drasticamente, mesmo que 99% das outras requisições tenham sido respondidas em 20 ms.
    """)
with col_th2:
    st.markdown("""
    #### 📐 Mediana (P50)
    *   **Teoria**: É o valor central que divide o conjunto de dados ordenados ao meio (50% menores e 50% maiores).
    *   **Na Aplicação (APM)**: Representa o tempo de resposta típico do usuário comum. Por ignorar extremos, se o servidor tiver alguns travamentos isolados, a mediana permanecerá baixa, mostrando a latência real da maioria estável dos acessos.
    """)
