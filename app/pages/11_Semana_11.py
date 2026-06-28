import streamlit as st
from utils.helpers import testar_funcao, exibir_codigo_funcao

# Importações do aluno
ajuste_regressao_linear = None
try:
    import core.time_series as core_time_series
    ajuste_regressao_linear = getattr(core_time_series, 'ajuste_regressao_linear', None)
except ImportError:
    try:
        import app.core.time_series as core_time_series
        ajuste_regressao_linear = getattr(core_time_series, 'ajuste_regressao_linear', None)
    except ImportError:
        pass

st.set_page_config(page_title="Semana 11: Regressão & Auto-Scaling", page_icon="📈", layout="wide")

st.title("Semana 11: Capacity Planning & Fargate Pricing")
st.markdown("---")

st.markdown("""
<div style="background-color: #f8f9fa; border-left: 5px solid #ff5722; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>📚 Conteúdo Teórico e Prático</h3>
    <p><span style="font-weight: bold; background-color: #d1ecf1; color: #0c5460; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Ciência de Dados</span> Regressão Linear Simples por Mínimos Quadrados para estimar quando a RAM/disco estourará.</p>
    <p><span style="font-weight: bold; background-color: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">Computação em Nuvem</span> AWS ELB (Load Balancers) e ASG (Auto Scaling). Fator de precificação do ECS (Fargate) por CPU/RAM hora.</p>
    <p><span style="font-weight: bold; background-color: #e2e3e5; color: #383d41; padding: 4px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">DevOps</span> Deploy de Containers em larga escala: Configuração da esteira para deploy no AWS App Runner ou ECS Fargate.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("📝 Tarefa da Semana")
st.info("Implementar `ajuste_regressao_linear` em `app/core/time_series.py`. Rodar o deploy automatizado da aplicação para um serviço gerenciado escalável (App Runner/ECS).")

st.subheader("🔍 Validação da Entrega (Indicador de Progresso)")

status_reg = testar_funcao(ajuste_regressao_linear, [1, 2, 3], [2, 4, 5])

# Exibe o código-fonte detectado
exibir_codigo_funcao(ajuste_regressao_linear, "ajuste_regressao_linear")

if status_reg == "NotImplemented":
    st.error("🔴 PENDENTE: Função `ajuste_regressao_linear` pendente em `time_series.py`.")
else:
    try:
        a, b = ajuste_regressao_linear([1, 2, 3], [2, 4, 5])
        if abs(a - 1.5) < 0.01:
            st.success("🟢 CONCLUÍDO: Função de regressão linear preditiva validada com sucesso!")
        else:
            st.warning("⚠️ AJUSTES NECESSÁRIOS: Os coeficientes calculados não batem com o gabarito matemático.")
    except Exception as e:
        st.error(f"Erro ao validar implementação: {e}")

st.markdown("---")
st.header("🧬 Conteúdo Estatístico Detalhado")

# Dados de Exemplo
horas = [1.0, 2.0, 3.0, 4.0, 5.0]
ram = [30.0, 35.0, 41.0, 47.0, 52.0]

col_reg1, col_reg2 = st.columns(2)
with col_reg1:
    st.write(f"**Variável Independente X (Tempo decorrido em horas):** `{horas}`")
with col_reg2:
    st.write(f"**Variável Dependente Y (% Uso de RAM):** `{ram}`")

# Card da Regressão Linear
with st.container(border=True):
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📊 Regressão Linear Simples por MQO")
        st.markdown("""
        **Conceito**: Modela o relacionamento linear entre duas variáveis contínuas ajustando a reta ideal. A inclinação ($a$) representa a taxa de variação de $Y$ por unidade de $X$, e o intercepto ($b$) representa o valor de $Y$ quando $X = 0$.
        
        **Fórmula Matemática**:
        $$y = a \\cdot x + b$$
        $$a = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sum (x_i - \\bar{x})^2} \\quad , \\quad b = \\bar{y} - a \\cdot \\bar{x}$$
        """)
    with col_r:
        st.markdown("**Resultado do Cálculo (Live Exec):**")
        if status_reg != "NotImplemented":
            try:
                a_coef, b_coef = ajuste_regressao_linear(horas, ram)
                st.info(f"💡 **Equação Ajustada**: $RAM = {a_coef:.2f} \\cdot Hora + {b_coef:.2f}$")
                
                # Previsão para hora = 12
                prev_12 = a_coef * 12 + b_coef
                st.write(f"**Previsão de uso de RAM para o instante t = 12h:** `{prev_12:.2f}%`")
            except Exception as e:
                st.error(f"Erro no cálculo: {e}")
        else:
            st.warning("⚠️ Aguardando implementação para exibir o cálculo.")
            
        st.markdown("""
        **Explicação do Resultado**:
        O coeficiente angular ($a = 5.60$) nos diz que o consumo de memória RAM cresce linearmente em **5,60%** a cada hora. Com o intercepto em $24.20$, prevemos que na hora $12$ o consumo de RAM estourará os limites e atingirá **91.4%**, representando um risco severo de travamento.
        
        **Importância no APM (Capacity Planning)**:
        Esta análise capacita o time de infraestrutura a identificar vazamentos de recursos (Memory Leaks). Ao projetar linearmente o consumo de RAM, os engenheiros evitam interrupções inesperadas (Out-Of-Memory / OOM), programando alarmes ou escalando preventivamente antes da quebra de serviço.
        """)
