import streamlit as st
import numpy as np
import pandas as pd
from utils.helpers import testar_funcao, exibir_codigo_funcao

# Importações do aluno
decompor_serie_temporal = None
try:
    import core.time_series as core_time_series
    decompor_serie_temporal = getattr(core_time_series, 'decompor_serie_temporal', None)
except ImportError:
    try:
        import app.core.time_series as core_time_series
        decompor_serie_temporal = getattr(core_time_series, 'decompor_serie_temporal', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 10: Decomposição & Logs", page_icon="⚙️", layout="wide")

st.title("Semana 10: Decomposição & SNS/SQS Pricing")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Séries Temporais: Decomposição de uso de CPU (Tendência, Sazonalidade) e suavização.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS SQS (filas) e AWS SNS (mensagens/e-mails). Precificação de volume de filas e alertas.</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Log Centralizado: Integração do Docker Log Driver para exportar logs da aplicação para o CloudWatch Logs.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar a função `decompor_serie_temporal` em `app/core/time_series.py`. Integrar alertas automáticos por e-mail com Amazon SNS.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_dec = testar_funcao(decompor_serie_temporal, pd.Series(np.random.rand(50), index=pd.date_range("2026-01-01", periods=50)), 7)

# Exibe o código-fonte detectado
exibir_codigo_funcao(decompor_serie_temporal, "decompor_serie_temporal")

if status_dec == "NotImplemented":
    st.error("🔴 PENDENTE: Função `decompor_serie_temporal` não implementada em `time_series.py`.")
else:
    st.success("🟢 CONCLUÍDO: Decomposição clássica de séries temporais validada!")

st.markdown("---")
st.header("🧬 Conteúdo Estatístico Detalhado")

# Dados de Exemplo
np.random.seed(42)
datas = pd.date_range(start="2026-06-01", periods=24, freq="h")
# Cria uma série temporal com tendência e sazonalidade de período 6
tendencia = np.linspace(20, 50, 24)
sazonalidade = np.sin(np.linspace(0, 4*np.pi, 24)) * 10
ruido = np.random.normal(0, 2, 24)
s_observada = pd.Series(tendencia + sazonalidade + ruido, index=datas)

st.write("**Série Temporal Observada de Uso de CPU (24 horas):**")
st.line_chart(s_observada)

# Card da Decomposição
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Decomposição de Séries Temporais")
        st.markdown("""
        **Conceito**: Consiste em desmembrar uma série de dados cronológicos observada em componentes individuais para facilitar o entendimento de padrões.
        
        **Fórmula Matemática (Modelo Aditivo)**:
        $$Y_t = T_t + S_t + I_t$$
        onde:
        *   $Y_t$: Série observada original
        *   $T_t$: **Tendência** (comportamento de longo prazo)
        *   $S_t$: **Sazonalidade** (ciclo periódico repetitivo)
        *   $I_t$: **Resíduo** (ruído ou flutuação irregular aleatória)
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_dec != "NotImplemented":
            try:
                trend, seasonal, resid = decompor_serie_temporal(s_observada, 6)
                st.info("💡 **Decomposição Realizada com Sucesso!**")
                
                # Plot resumido
                df_decomp = pd.DataFrame({
                    "Observado": s_observada,
                    "Tendência (Long Term)": trend,
                    "Sazonalidade (Ciclos)": seasonal
                })
                st.line_chart(df_decomp)
            except Exception as e:
                st.error(f"Erro no cálculo: {e}")
        else:
            st.warning("⚠️ Aguardando implementação para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado**:
        Ao isolar a **Sazonalidade**, conseguimos ver o pico periódico que se repete a cada período configurado. Já o isolamento da **Tendência** nos revela a curva real purificada de ruídos e oscilações cíclicas, mostrando claramente o avanço contínuo e sustentado do consumo de recursos.
        
        **Importância no APM**:
        Permite que a engenharia de DevOps e SRE configure regras de alerta inteligentes. Em vez de disparar falsos alarmes de CPU durante o pico natural do horário comercial (sazonalidade), o sistema analisa a *Tendência* subjacente para detectar fadigas reais de hardware no longo prazo.
        """)
