import streamlit as st
from utils.helpers import testar_funcao, exibir_codigo_funcao

# Importações do aluno
calcular_variancia = None
calcular_desvio_padrao = None
calcular_amplitude = None
try:
    import core.stats as core_stats
    calcular_variancia = getattr(core_stats, 'calcular_variancia', None)
    calcular_desvio_padrao = getattr(core_stats, 'calcular_desvio_padrao', None)
    calcular_amplitude = getattr(core_stats, 'calcular_amplitude', None)
except ImportError:
    try:
        import app.core.stats as core_stats
        calcular_variancia = getattr(core_stats, 'calcular_variancia', None)
        calcular_desvio_padrao = getattr(core_stats, 'calcular_desvio_padrao', None)
        calcular_amplitude = getattr(core_stats, 'calcular_amplitude', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 3: Variabilidade & Docker", page_icon="⚙️", layout="wide")

st.title("Semana 3: Variabilidade & EC2 Pricing")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Estatística Descritiva: Medidas de Dispersão (Amplitude, Variância, Desvio Padrão) para medir Jitter de latência.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS EC2. Modelos de Compra: On-Demand vs Spot vs Instâncias Reservadas.</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Docker: Criação e execução de containers. Escrita do primeiro Dockerfile.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar as funções `calcular_variancia`, `calcular_desvio_padrao` e `calcular_amplitude` em `app/core/stats.py`. Dockerizar a aplicação Streamlit do APM.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_var = testar_funcao(calcular_variancia, [10.0, 20.0, 30.0])
status_std = testar_funcao(calcular_desvio_padrao, [10.0, 20.0, 30.0])
status_amp = testar_funcao(calcular_amplitude, [10.0, 20.0, 30.0])

# Exibe o código-fonte detectado
exibir_codigo_funcao(calcular_variancia, "calcular_variancia")
exibir_codigo_funcao(calcular_desvio_padrao, "calcular_desvio_padrao")
exibir_codigo_funcao(calcular_amplitude, "calcular_amplitude")

if "NotImplemented" in [status_var, status_std, status_amp]:
    st.error("🔴 PENDENTE: As funções de dispersão ainda não foram totalmente implementadas em `stats.py`.")
else:
    try:
        v_val = calcular_variancia([10.0, 20.0, 30.0], amostral=True)
        if v_val == 100.0:
            st.success("🟢 CONCLUÍDO: Funções de variabilidade e dispersão implementadas corretamente!")
        else:
            st.warning("⚠️ AJUSTES NECESSÁRIOS: Lógica de variância retornando valores incorretos. Verifique o divisor (N-1) na variância amostral.")
    except Exception as e:
        st.error(f"Erro ao validar implementação: {e}")

st.markdown("---")
st.subheader("💡 Guia de Teoria e Interpretação (APM)")

col_th1, col_th2, col_th3 = st.columns(3)
with col_th1:
    st.markdown("""
    #### 📐 Amplitude
    *   **Teoria**: Diferença entre o maior e o menor valor de uma série:
        $$R = x_{max} - x_{min}$$
    *   **Na Aplicação (APM)**: Indica a distância total de tempo de resposta entre a requisição mais lenta e a mais rápida. É útil para detectar a disparidade máxima na experiência dos usuários.
    """)
with col_th2:
    st.markdown("""
    #### 📐 Variância
    *   **Teoria**: Mede o quão dispersos os dados estão em relação à média, calculando a média dos desvios quadráticos:
        $$s^2 = \\frac{\\sum_{i=1}^{n} (x_i - \\bar{x})^2}{n - 1}$$
    *   **Na Aplicação (APM)**: Serve como base matemática para quantificar a oscilação do desempenho, mas sua unidade é em milissegundos elevados ao quadrado ($ms^2$), dificultando a leitura direta.
    """)
with col_th3:
    st.markdown("""
    #### 📐 Desvio Padrão
    *   **Teoria**: É a raiz quadrada da variância, trazendo a dispersão de volta para a unidade original dos dados:
        $$s = \\sqrt{s^2}$$
    *   **Na Aplicação (APM)**: Representa o **Jitter** (oscilação/instabilidade do sistema). Se o desvio for baixo (ex: 5 ms), a API é muito estável. Se for alto (ex: 200 ms), a performance é inconstante e imprevisível.
    """)
