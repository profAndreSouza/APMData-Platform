import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Tenta importar os loaders e helpers
from utils.data_loader import gerar_dados_apm
from utils.helpers import obter_readme_markdown, exibir_codigo_funcao

# Tenta importar as funções de ciência de dados dos alunos
core_stats = None
try:
    import core.stats as core_stats
except ImportError:
    try:
        import app.core.stats as core_stats
    except ImportError:
        pass

calcular_media = getattr(core_stats, 'calcular_media', None)
calcular_mediana = getattr(core_stats, 'calcular_mediana', None)
calcular_desvio_padrao = getattr(core_stats, 'calcular_desvio_padrao', None)

core_hypothesis = None
try:
    import core.hypothesis as core_hypothesis
except ImportError:
    try:
        import app.core.hypothesis as core_hypothesis
    except ImportError:
        pass

teste_shapiro_wilk = getattr(core_hypothesis, 'teste_shapiro_wilk', None)

core_time_series = None
try:
    import core.time_series as core_time_series
except ImportError:
    try:
        import app.core.time_series as core_time_series
    except ImportError:
        pass

ajuste_regressao_linear = getattr(core_time_series, 'ajuste_regressao_linear', None)

# Configurações Streamlit
st.set_page_config(
    page_title="APMData Platform - Dashboard Geral",
    page_icon="🖥️",
    layout="wide"
)

st.title("🖥️ APMData - Painel de Observabilidade e Performance")
st.markdown("""
Esta plataforma realiza análises de desempenho em tempo real baseada em métricas de infraestrutura de APIs e servidores.
O painel consome os módulos analíticos construídos nas aulas de **Ciência de Dados** e implantados via pipeline **DevOps** na **AWS (Nuvem)**.
""")

# Carrega e exibe o README
readme_md = obter_readme_markdown()
if readme_md:
    with st.expander("📖 Sobre o Projeto Integrador & Guia de Aulas (README.md)", expanded=False):
        st.markdown(readme_md)

st.markdown("---")

# ---- Carrega Massa de Dados APM ----
df_apm = gerar_dados_apm(150)
valores_latencia = df_apm["tempo_resposta_ms"].tolist()

# ---- Bloco 1: Estatística Descritiva (Módulos Semana 2 e 3) ----
st.header("📊 Métricas de Performance em Tempo Real")

col1, col2, col3 = st.columns(3)

# Média
try:
    media_val = calcular_media(valores_latencia)
    col1.metric("Tempo de Resposta Médio", f"{media_val:.2f} ms", "Módulo: core.stats")
except (NameError, NotImplementedError, TypeError):
    col1.warning("⚠️ Média: `calcular_media` pendente.")
except Exception as e:
    col1.error(f"Erro Média: {e}")

# Mediana (P50)
try:
    mediana_val = calcular_mediana(valores_latencia)
    col2.metric("Latência Mediana (P50)", f"{mediana_val:.2f} ms", "Módulo: core.stats")
except (NameError, NotImplementedError, TypeError):
    col2.warning("⚠️ Mediana: `calcular_mediana` pendente.")
except Exception as e:
    col2.error(f"Erro Mediana: {e}")

# Jitter (Desvio Padrão)
try:
    std_val = calcular_desvio_padrao(valores_latencia)
    col3.metric("Desvio Padrão (Jitter)", f"{std_val:.2f} ms", "Módulo: core.stats")
except (NameError, NotImplementedError, TypeError):
    col3.warning("⚠️ Desvio Padrão: `calcular_desvio_padrao` pendente.")
except Exception as e:
    col3.error(f"Erro Desvio Padrão: {e}")

st.markdown("---")

# ---- Bloco 2: Visualizações Dinâmicas ----
st.header("📈 Telemetria de Infraestrutura")

col_graf1, col_graf2 = st.columns([2, 1])

with col_graf1:
    st.subheader("Tempo de Resposta Histórico")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df_apm["data_hora"], df_apm["tempo_resposta_ms"], label="Latência (ms)", color="#00bcd4")
    ax.axhline(500.0, color="red", linestyle="--", label="Limite SLA Alerta")
    ax.set_ylabel("Tempo de Resposta (ms)")
    ax.set_xlabel("Hora")
    ax.legend()
    st.pyplot(fig)

with col_graf2:
    st.subheader("Uso de Recursos (Distribuição)")
    fig2, ax2 = plt.subplots(figsize=(5, 4.3))
    sns.boxplot(data=df_apm[["uso_cpu_percent", "uso_ram_percent"]], ax=ax2, palette="Set2")
    ax2.set_ylabel("Porcentagem (%)")
    st.pyplot(fig2)

st.markdown("---")

# ---- Bloco 3: Testes de Hipótese e Regressões ----
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Análise de Aderência da Latência")
    try:
        est, p_val, e_normal = teste_shapiro_wilk(valores_latencia)
        st.write(f"- Estatística do teste: `{est:.4f}`")
        st.write(f"- P-Valor: `{p_val:.4e}`")
        if e_normal:
            st.success("✅ Distribuição Normal: A latência se comporta de forma estável (gaussiana).")
        else:
            st.warning("⚠️ Distribuição NÃO Normal: Presença forte de picos de lentidão/outliers.")
    except (NameError, NotImplementedError, TypeError):
        st.info("💡 Teste de Shapiro-Wilk não implementado ainda.")

with col_b:
    st.subheader("Planejamento de Capacidade (Capacity Planning)")
    try:
        indices = list(range(len(valores_latencia)))
        valores_ram = df_apm["uso_ram_percent"].tolist()
        a, b = ajuste_regressao_linear(indices, valores_ram)
        
        futuro = 48
        predito = a * (len(valores_latencia) + futuro) + b
        
        st.markdown(f"**Equação de Tendência (RAM)**: $RAM = {a:.4f} \\times Hora + {b:.2f}$")
        if predito >= 90.0:
            st.error(f"🚨 **ALERTA CRÍTICO**: A RAM estimada para as próximas {futuro}h é de **{predito:.2f}%**. Risco de Out-Of-Memory (Memory Leak detectado)!")
        else:
            st.success(f"🟢 Seguro: Uso de RAM estimado em {futuro}h está sob controle ({predito:.2f}%).")
    except (NameError, NotImplementedError, TypeError):
        st.info("💡 Ajuste de regressão linear para capacity planning pendente de implementação.")

st.markdown("---")
st.header("💻 Inspeção de Código Ativo (Algoritmos Estatísticos)")
st.markdown("Veja abaixo as implementações reais das funções matemáticas utilizadas nas métricas deste dashboard:")

col_code1, col_code2 = st.columns(2)
with col_code1:
    exibir_codigo_funcao(calcular_media, "calcular_media")
    exibir_codigo_funcao(calcular_mediana, "calcular_mediana")
    exibir_codigo_funcao(calcular_desvio_padrao, "calcular_desvio_padrao")

with col_code2:
    exibir_codigo_funcao(teste_shapiro_wilk, "teste_shapiro_wilk")
    exibir_codigo_funcao(ajuste_regressao_linear, "ajuste_regressao_linear")
