import streamlit as st
from utils.helpers import testar_funcao, exibir_codigo_funcao

# Importações do aluno
teste_qui_quadrado_associacao = None
try:
    import core.hypothesis as core_hypothesis
    teste_qui_quadrado_associacao = getattr(core_hypothesis, 'teste_qui_quadrado_associacao', None)
except ImportError:
    try:
        import app.core.hypothesis as core_hypothesis
        teste_qui_quadrado_associacao = getattr(core_hypothesis, 'teste_qui_quadrado_associacao', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 7: Associação Categórica", page_icon="📊", layout="wide")

st.title("Semana 7: Associação Categórica & SDK Boto3")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Qui-Quadrado para verificar associação categórica (Endpoint da API vs Taxa de Erro HTTP 500).</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS SDK em Python (Boto3). Gravação e persistência automática de arquivos de log no S3.</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Docker Hub: Publicação automática da imagem Docker compilada via GitHub Actions.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar `teste_qui_quadrado_associacao` em `app/core/hypothesis.py`. Adicionar código no pipeline para gerar a tag da imagem Docker e enviar ao Docker Hub.")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_qui = testar_funcao(teste_qui_quadrado_associacao, [[10, 10], [10, 10]])

# Exibe o código-fonte detectado
exibir_codigo_funcao(teste_qui_quadrado_associacao, "teste_qui_quadrado_associacao")

if status_qui == "NotImplemented":
    st.error("🔴 PENDENTE: Teste Qui-Quadrado de associação categórica pendente em `hypothesis.py`.")
else:
    st.success("🟢 CONCLUÍDO: Módulo de associação estatística e teste do Qui-Quadrado validado!")

st.markdown("---")
st.subheader("💡 Guia de Teoria e Interpretação (APM)")

st.markdown("""
#### 📐 Teste do Qui-Quadrado de Associação (Independência)
*   **Teoria**: Compara frequências observadas de duas variáveis categóricas com as frequências esperadas sob a hipótese de que as variáveis são independentes ($H_0$). Se o p-valor < 0.05, rejeitamos $H_0$, indicando que as variáveis têm associação significativa.
*   **Na Aplicação (APM - Correlação de Erros)**: Crucial para **diagnóstico de incidentes (Troubleshooting)**. Permite provar se a ocorrência de erros HTTP 500 está associada de forma sistemática a um endpoint específico da API (ex: `/api/v1/checkout`) ou se os erros estão ocorrendo de maneira aleatória distribuída igualmente entre todas as rotas.
""")
