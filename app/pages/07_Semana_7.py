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
st.header("🧬 Conteúdo Estatístico Detalhado")

# Tabela de contingência de exemplo
tabela_exemplo = [[45, 5], [15, 35]]
st.markdown("**Tabela de Contingência Observada (Frequências de Logs):**")

col_t1, col_t2 = st.columns([1, 2])
with col_t1:
    import pandas as pd
    df_tabela = pd.DataFrame(tabela_exemplo, 
                             index=["Rota /products", "Rota /checkout"], 
                             columns=["Sucesso (200 OK)", "Erro (500 Internal Error)"])
    st.table(df_tabela)

# Card do Qui-Quadrado
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Teste Qui-Quadrado de Independência")
        st.markdown("""
        **Conceito**: É utilizado para verificar se há associação estatisticamente significativa entre duas variáveis categóricas qualitativas (neste caso, "Rota Acessada" e "Resultado da Transação").
        
        *   **Hipótese Nula ($H_0$)**: As variáveis são independentes (a ocorrência de erro não está relacionada com a rota acessada).
        *   **Hipótese Alternativa ($H_1$)**: As variáveis são associadas (existe uma rota com mais falhas sistemáticas).
        
        **Fórmula Matemática**:
        $$\\chi^2 = \\sum \\frac{(O_i - E_i)^2}{E_i}$$
        onde $O_i$ é o valor observador real e $E_i$ é o valor esperado sob a hipótese nula.
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_qui != "NotImplemented":
            try:
                chi2_stat, p_val, associado = teste_qui_quadrado_associacao(tabela_exemplo)
                st.info(f"💡 **Estatística $\\chi^2$**: `{chi2_stat:.4f}` | **p-valor**: `{p_val:.8f}`")
                if associado:
                    st.success("🟢 Decisão Estatística: Rejeita H0 (Existe associação entre a rota e a taxa de erro!)")
                else:
                    st.warning("⚠️ Decisão Estatística: Falha em rejeitar H0 (Erros estão distribuídos uniformemente.)")
            except Exception as e:
                st.error(f"Erro no cálculo: {e}")
        else:
            st.warning("⚠️ Aguardando implementação para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado**:
        Com um p-valor extremamente próximo de zero (**< 0.0001**), rejeitamos fortemente a hipótese de independência. Isso prova que a rota `/checkout` tem estatisticamente mais erros do que o esperado por puro acaso.
        
        **Ação Operacional (Troubleshooting)**:
        Esta análise comprova que o problema não é uma falha de rede aleatória ou fadiga física do servidor, mas sim um bug de software específico no código do checkout, direcionando o time de DevOps a investigar especificamente as classes e integrações do carrinho de compras.
        """)
