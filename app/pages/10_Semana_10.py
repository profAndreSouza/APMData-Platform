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
st.subheader("💡 Guia de Teoria e Interpretação (APM)")

st.markdown("""
#### 📐 Decomposição de Séries Temporais
*   **Teoria**: Separação de uma série temporal observada em três componentes estruturais distintos:
    1.  **Tendência**: Direção de longo prazo (crescimento ou decrescimento sustentado).
    2.  **Sazonalidade**: Variações periódicas regulares que se repetem em intervalos fixos (ex: picos diários ou semanais).
    3.  **Resíduo (Ruído)**: Flutuações aleatórias não explicadas pelos outros dois fatores.
*   **Na Aplicação (APM - Uso de CPU/RAM)**: Ajuda a ignorar variações rotineiras de acessos diários (sazonalidade de pico comercial) para enxergar o comportamento subjacente do sistema. Ao analisar a curva de **Tendência**, o time de SRE consegue identificar degradações silenciosas e sustentadas na performance ou vazamentos lentos de recursos que exigiriam redimensionamento físico da infraestrutura a médio prazo.
""")
