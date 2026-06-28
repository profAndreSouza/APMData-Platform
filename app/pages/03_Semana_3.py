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
st.header("🧬 Conteúdo Estatístico Detalhado")

# Amostras para demonstração
dados_estaveis = [120.0, 125.0, 118.0, 122.0, 120.0]
dados_instaveis = [50.0, 450.0, 20.0, 600.0, 80.0]
st.write(f"**Conjunto de Dados (Latências Instáveis em ms):** `{dados_instaveis}`")

# 1. Amplitude
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Amplitude (R)")
        st.markdown("""
        **Conceito**: É a diferença absoluta entre o maior e o menor valor de uma amostra, mostrando a extensão total da variação de latência.
        
        **Fórmula Matemática**:
        $$R = x_{max} - x_{min}$$
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_amp != "NotImplemented":
            try:
                res_amp = calcular_amplitude(dados_instaveis)
                st.info(f"💡 **Amplitude Calculada**: `{res_amp:.2f} ms`")
            except Exception as e:
                st.error(f"Erro: {e}")
        else:
            st.warning("⚠️ Aguardando implementação para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado**:
        A amplitude de **580 ms** reflete a disparidade máxima entre o melhor cenário (20 ms) e o pior cenário (600 ms) enfrentado pelos usuários. Embora seja simples de calcular, ela é muito limitada porque desconsidera a distribuição de todos os outros valores intermediários.
        """)

# 2. Variância
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Variância Amostral")
        st.markdown("""
        **Conceito**: Mede a dispersão dos dados calculando a média dos desvios elevados ao quadrado em relação à média geral. A elevação ao quadrado evita que desvios positivos e negativos se cancelem.
        
        **Fórmula Matemática**:
        $$s^2 = \\frac{\\sum_{i=1}^{n} (x_i - \\bar{x})^2}{n - 1}$$
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_var != "NotImplemented":
            try:
                res_var = calcular_variancia(dados_instaveis, amostral=True)
                st.info(f"💡 **Variância Calculada**: `{res_var:.2f} ms²`")
            except Exception as e:
                st.error(f"Erro: {e}")
        else:
            st.warning("⚠️ Aguardando implementação para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado**:
        O cálculo resultou em **67.300 ms²**. Note que a variância está expressa em milissegundos elevados ao quadrado ($ms^2$). Como essa unidade não corresponde ao mundo real de APM (ninguém mede tempo ao quadrado), a variância serve essencialmente como degrau intermediário para chegarmos ao desvio padrão.
        """)

# 3. Desvio Padrão
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Desvio Padrão Amostral")
        st.markdown("""
        **Conceito**: É a raiz quadrada da variância. Ele traz a medida de dispersão de volta para a mesma unidade física do conjunto de dados original.
        
        **Fórmula Matemática**:
        $$s = \\sqrt{s^2}$$
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_std != "NotImplemented":
            try:
                res_std = calcular_desvio_padrao(dados_instaveis, amostral=True)
                st.info(f"💡 **Desvio Padrão Calculado**: `{res_std:.2f} ms`")
            except Exception as e:
                st.error(f"Erro: {e}")
        else:
            st.warning("⚠️ Aguardando implementação para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado**:
        O desvio padrão de **259.42 ms** mede diretamente a volatilidade ou o **Jitter** do servidor. Isso indica que, embora a média aritmética desse conjunto seja de 240 ms, as respostas reais tendem a variar em torno de +/- 259 ms para cima ou para baixo, indicando uma infraestrutura altamente instável e de péssima qualidade de serviço (QoS).
        """)
