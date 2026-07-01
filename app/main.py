from flask import Flask, render_template, jsonify, abort
import numpy as np
import pandas as pd
import io
import base64
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Importa loaders e helpers
from utils.data_loader import gerar_dados_apm
from utils.helpers import obter_readme_markdown, testar_funcao, obter_codigo_funcao, obter_semana_info

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
calcular_variancia = getattr(core_stats, 'calcular_variancia', None)
calcular_amplitude = getattr(core_stats, 'calcular_amplitude', None)

core_hypothesis = None
try:
    import core.hypothesis as core_hypothesis
except ImportError:
    try:
        import app.core.hypothesis as core_hypothesis
    except ImportError:
        pass

teste_shapiro_wilk = getattr(core_hypothesis, 'teste_shapiro_wilk', None)
teste_kolmogorov_smirnov = getattr(core_hypothesis, 'teste_kolmogorov_smirnov', None)
teste_qui_quadrado_associacao = getattr(core_hypothesis, 'teste_qui_quadrado_associacao', None)

core_time_series = None
try:
    import core.time_series as core_time_series
except ImportError:
    try:
        import app.core.time_series as core_time_series
    except ImportError:
        pass

ajuste_regressao_linear = getattr(core_time_series, 'ajuste_regressao_linear', None)
decompor_serie_temporal = getattr(core_time_series, 'decompor_serie_temporal', None)
calcular_correlacao_pearson = getattr(core_time_series, 'calcular_correlacao_pearson', None)

core_sampling = None
try:
    import core.sampling as core_sampling
except ImportError:
    try:
        import app.core.sampling as core_sampling
    except ImportError:
        pass

amostragem_sistematica = getattr(core_sampling, 'amostragem_sistematica', None)

app = Flask(__name__)

def calcular_status_semanas():
    # Semana 2: `calcular_media` e `calcular_mediana`
    s2_media = testar_funcao(calcular_media, [10.0, 20.0, 30.0])
    s2_mediana = testar_funcao(calcular_mediana, [10.0, 20.0, 30.0])
    status_sem2 = "Concluído" if (s2_media is True and s2_mediana is True) else "Pendente"

    # Semana 3: `calcular_variancia`, `calcular_desvio_padrao`, `calcular_amplitude`
    s3_var = testar_funcao(calcular_variancia, [10.0, 20.0, 30.0])
    s3_std = testar_funcao(calcular_desvio_padrao, [10.0, 20.0, 30.0])
    s3_amp = testar_funcao(calcular_amplitude, [10.0, 20.0, 30.0])
    status_sem3 = "Concluído" if (s3_var is True and s3_std is True and s3_amp is True) else "Pendente"

    # Semana 4: `amostragem_sistematica`
    s4_sis = testar_funcao(amostragem_sistematica, [1, 2, 3, 4, 5, 6], 2)
    status_sem4 = "Concluído" if s4_sis is True else "Pendente"

    # Semana 6: `teste_shapiro_wilk`
    s6_shap = testar_funcao(teste_shapiro_wilk, [1.0, 2.0, 3.0, 4.0, 5.0])
    status_sem6 = "Concluído" if s6_shap is True else "Pendente"

    # Semana 7: `teste_qui_quadrado_associacao`
    s7_qui = testar_funcao(teste_qui_quadrado_associacao, [[10, 10], [10, 10]])
    status_sem7 = "Concluído" if s7_qui is True else "Pendente"

    # Semana 8: `calcular_correlacao_pearson`
    s8_pe = testar_funcao(calcular_correlacao_pearson, [1, 2, 3], [2, 4, 6])
    status_sem8 = "Concluído" if s8_pe is True else "Pendente"

    # Semana 10: `decompor_serie_temporal`
    s10_dec = testar_funcao(decompor_serie_temporal, pd.Series(np.random.rand(50), index=pd.date_range("2026-01-01", periods=50)), 7)
    status_sem10 = "Concluído" if s10_dec is True else "Pendente"

    # Semana 11: `ajuste_regressao_linear`
    s11_reg = testar_funcao(ajuste_regressao_linear, [1, 2, 3], [2, 4, 5])
    status_sem11 = "Concluído" if s11_reg is True else "Pendente"

    return {
        1: "Concluído",
        2: status_sem2,
        3: status_sem3,
        4: status_sem4,
        5: "Concluído",
        6: status_sem6,
        7: status_sem7,
        8: status_sem8,
        9: "Concluído",
        10: status_sem10,
        11: status_sem11,
        12: "Concluído",
        13: "Concluído",
        14: "Concluído",
        15: "Concluído"
    }

@app.route("/")
def index():
    # Obtém o status de todas as semanas
    status_semanas = calcular_status_semanas()
    
    # Prepara lista de semanas estruturada para o grid
    semanas_info = []
    for num in range(1, 16):
        meta = obter_semana_info(num)
        semanas_info.append({
            "n": num,
            "title": meta.get("title", f"Semana {num}"),
            "icon": meta.get("icon", "📓"),
            "desc": meta.get("conteudo", {}).get("cd", ""),
            "status": status_semanas[num],
            "progress": "100%" if status_semanas[num] == "Concluído" else "0%"
        })

    # Carrega e calcula telemetria em tempo real
    df_apm = gerar_dados_apm(150)
    valores_latencia = df_apm["tempo_resposta_ms"].tolist()

    # Estatísticas básicas com fallback
    media_val = None
    if calcular_media and testar_funcao(calcular_media, [1, 2]) is True:
        media_val = f"{calcular_media(valores_latencia):.2f} ms"
    
    mediana_val = None
    if calcular_mediana and testar_funcao(calcular_mediana, [1, 2]) is True:
        mediana_val = f"{calcular_mediana(valores_latencia):.2f} ms"
        
    std_val = None
    if calcular_desvio_padrao and testar_funcao(calcular_desvio_padrao, [1, 2]) is True:
        std_val = f"{calcular_desvio_padrao(valores_latencia):.2f} ms"

    # Gráfico 1: Histórico de Latência
    fig, ax = plt.subplots(figsize=(10, 4.3))
    ax.plot(df_apm["data_hora"], df_apm["tempo_resposta_ms"], label="Latência (ms)", color="#10b981", linewidth=2)
    ax.axhline(500.0, color="#ef4444", linestyle="--", label="Limite SLA Alerta (500ms)")
    ax.set_ylabel("Tempo de Resposta (ms)", color="#475569")
    ax.set_xlabel("Hora do Registro", color="#475569")
    ax.tick_params(colors="#475569")
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.legend(facecolor="#ffffff", edgecolor="#e2e8f0")
    fig.patch.set_facecolor("#f8fafc")
    ax.set_facecolor("#ffffff")
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color("#cbd5e1")
    ax.spines["left"].set_color("#cbd5e1")
    
    buf1 = io.BytesIO()
    plt.savefig(buf1, format="png", bbox_inches="tight")
    buf1.seek(0)
    chart_latencia = base64.b64encode(buf1.read()).decode("utf-8")
    plt.close(fig)

    # Gráfico 2: Distribuição Boxplot
    fig2, ax2 = plt.subplots(figsize=(5, 4.8))
    sns.boxplot(data=df_apm[["uso_cpu_percent", "uso_ram_percent"]], ax=ax2, palette=["#10b981", "#38bdf8"])
    ax2.set_ylabel("Uso (%)", color="#475569")
    ax2.set_xticklabels(["CPU", "RAM (Memória)"])
    ax2.tick_params(colors="#475569")
    fig2.patch.set_facecolor("#f8fafc")
    ax2.set_facecolor("#ffffff")
    for spine in ["top", "right"]:
        ax2.spines[spine].set_visible(False)
    ax2.spines["bottom"].set_color("#cbd5e1")
    ax2.spines["left"].set_color("#cbd5e1")
    
    buf2 = io.BytesIO()
    plt.savefig(buf2, format="png", bbox_inches="tight")
    buf2.seek(0)
    chart_recursos = base64.b64encode(buf2.read()).decode("utf-8")
    plt.close(fig2)

    # Teste de Shapiro-Wilk
    shapiro_resultado = None
    if teste_shapiro_wilk and testar_funcao(teste_shapiro_wilk, [1.0, 2.0, 3.0, 4.0, 5.0]) is True:
        est, p_val, e_normal = teste_shapiro_wilk(valores_latencia)
        shapiro_resultado = {
            "est": f"{est:.4f}",
            "p_val": f"{p_val:.4e}",
            "normal": e_normal
        }

    # Capacity planning (Regressão)
    capacity_resultado = None
    if ajuste_regressao_linear and testar_funcao(ajuste_regressao_linear, [1, 2], [2, 4]) is True:
        indices = list(range(len(valores_latencia)))
        valores_ram = df_apm["uso_ram_percent"].tolist()
        a, b = ajuste_regressao_linear(indices, valores_ram)
        futuro = 48
        predito = a * (len(valores_latencia) + futuro) + b
        capacity_resultado = {
            "a": f"{a:.4f}",
            "b": f"{b:.2f}",
            "predito": f"{predito:.2f}",
            "critico": predito >= 90.0
        }

    readme_content = obter_readme_markdown()

    return render_template(
        "index.html",
        semanas=semanas_info,
        media=media_val,
        mediana=mediana_val,
        jitter=std_val,
        chart_latencia=chart_latencia,
        chart_recursos=chart_recursos,
        shapiro=shapiro_resultado,
        capacity=capacity_resultado,
        readme=readme_content
    )

@app.route("/semana/<int:num>")
def semana(num):
    if num < 1 or num > 15:
        abort(404)
        
    meta = obter_semana_info(num)
    if not meta:
        abort(404)

    # Verifica status desta semana específica
    status_semanas = calcular_status_semanas()
    status_atual = status_semanas[num]

    live_calculation = None
    codigos_fonte = {}

    # Executa validação de entregas e gera dados de simulação por semana
    if num == 2:
        # Semana 2: Tendência Central
        s2_media = testar_funcao(calcular_media, [10.0, 20.0, 30.0])
        s2_mediana = testar_funcao(calcular_mediana, [10.0, 20.0, 30.0])
        valida_entrega = s2_media is True and s2_mediana is True
        
        dados_exemplo = [100.0, 150.0, 120.0, 900.0, 130.0]
        calculo_media = None
        calculo_mediana = None
        if valida_entrega:
            calculo_media = f"{calcular_media(dados_exemplo):.2f} ms"
            calculo_mediana = f"{calcular_mediana(dados_exemplo):.2f} ms"

        live_calculation = {
            "dados": str(dados_exemplo),
            "resultados": [
                {"label": "Média Aritmética (Live)", "value": calculo_media or "Pendente"},
                {"label": "Mediana / P50 (Live)", "value": calculo_mediana or "Pendente"}
            ]
        }
        codigos_fonte = {
            "calcular_media": obter_codigo_funcao(calcular_media),
            "calcular_mediana": obter_codigo_funcao(calcular_mediana)
        }
    elif num == 3:
        # Semana 3: Variabilidade
        s3_var = testar_funcao(calcular_variancia, [10.0, 20.0, 30.0])
        s3_std = testar_funcao(calcular_desvio_padrao, [10.0, 20.0, 30.0])
        s3_amp = testar_funcao(calcular_amplitude, [10.0, 20.0, 30.0])
        valida_entrega = s3_var is True and s3_std is True and s3_amp is True

        dados_exemplo = [50.0, 450.0, 20.0, 600.0, 80.0]
        calc_var = None
        calc_std = None
        calc_amp = None
        if valida_entrega:
            calc_var = f"{calcular_variancia(dados_exemplo, amostral=True):.2f} ms²"
            calc_std = f"{calcular_desvio_padrao(dados_exemplo, amostral=True):.2f} ms"
            calc_amp = f"{calcular_amplitude(dados_exemplo):.2f} ms"

        live_calculation = {
            "dados": str(dados_exemplo),
            "resultados": [
                {"label": "Amplitude (R)", "value": calc_amp or "Pendente"},
                {"label": "Variância Amostral (s²)", "value": calc_var or "Pendente"},
                {"label": "Desvio Padrão (s)", "value": calc_std or "Pendente"}
            ]
        }
        codigos_fonte = {
            "calcular_variancia": obter_codigo_funcao(calcular_variancia),
            "calcular_desvio_padrao": obter_codigo_funcao(calcular_desvio_padrao),
            "calcular_amplitude": obter_codigo_funcao(calcular_amplitude)
        }
    elif num == 4:
        # Semana 4: Amostragem
        s4_sis = testar_funcao(amostragem_sistematica, [1, 2, 3, 4, 5, 6], 2)
        valida_entrega = s4_sis is True

        dados_exemplo = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
        amostra_res = None
        if valida_entrega:
            amostra_res = str(amostragem_sistematica(dados_exemplo, 4, ponto_partida=0))

        live_calculation = {
            "dados": f"População (12 itens): {dados_exemplo}",
            "resultados": [
                {"label": "Amostra Sistemática (n=4, i=0)", "value": amostra_res or "Pendente"}
            ]
        }
        codigos_fonte = {
            "amostragem_sistematica": obter_codigo_funcao(amostragem_sistematica)
        }
    elif num == 6:
        # Semana 6: Normalidade
        s6_shap = testar_funcao(teste_shapiro_wilk, [1.0, 2.0, 3.0, 4.0, 5.0])
        valida_entrega = s6_shap is True

        dados_exemplo = [120.0, 122.0, 118.0, 121.0, 119.0, 120.0, 123.0, 117.0, 121.0, 119.0]
        decisao = None
        if valida_entrega:
            stat, p_val, eh_normal = teste_shapiro_wilk(dados_exemplo)
            decisao = f"Normal (p={p_val:.4f})" if eh_normal else f"Não-Normal (p={p_val:.4f})"

        live_calculation = {
            "dados": str(dados_exemplo),
            "resultados": [
                {"label": "Resultado Shapiro-Wilk", "value": decisao or "Pendente"}
            ]
        }
        codigos_fonte = {
            "teste_shapiro_wilk": obter_codigo_funcao(teste_shapiro_wilk)
        }
    elif num == 7:
        # Semana 7: Qui-Quadrado
        s7_qui = testar_funcao(teste_qui_quadrado_associacao, [[10, 10], [10, 10]])
        valida_entrega = s7_qui is True

        tabela_exemplo = [[45, 5], [15, 35]]
        decisao = None
        if valida_entrega:
            chi2_stat, p_val, associado = teste_qui_quadrado_associacao(tabela_exemplo)
            decisao = f"Há Associação (p={p_val:.6f})" if associado else f"Variáveis Independentes (p={p_val:.6f})"

        live_calculation = {
            "dados": "Tabela Contingência: products [45, 5] vs checkout [15, 35]",
            "resultados": [
                {"label": "Decisão Qui-Quadrado", "value": decisao or "Pendente"}
            ]
        }
        codigos_fonte = {
            "teste_qui_quadrado_associacao": obter_codigo_funcao(teste_qui_quadrado_associacao)
        }
    elif num == 8:
        # Semana 8: Correlação
        s8_pe = testar_funcao(calcular_correlacao_pearson, [1, 2, 3], [2, 4, 6])
        valida_entrega = s8_pe is True

        x_ex = [10.0, 20.0, 30.0, 40.0, 50.0]
        y_ex = [12.0, 22.0, 44.0, 61.0, 85.0]
        coef = None
        if valida_entrega:
            coef = f"{calcular_correlacao_pearson(x_ex, y_ex):.4f}"

        live_calculation = {
            "dados": f"Reqs: {x_ex} | CPU: {y_ex}",
            "resultados": [
                {"label": "Pearson (r)", "value": coef or "Pendente"}
            ]
        }
        codigos_fonte = {
            "calcular_correlacao_pearson": obter_codigo_funcao(calcular_correlacao_pearson)
        }
    elif num == 10:
        # Semana 10: Decomposição
        s10_dec = testar_funcao(decompor_serie_temporal, pd.Series(np.random.rand(50), index=pd.date_range("2026-01-01", periods=50)), 7)
        valida_entrega = s10_dec is True

        chart_base64 = None
        if valida_entrega:
            np.random.seed(42)
            datas = pd.date_range(start="2026-06-01", periods=24, freq="h")
            tendencia = np.linspace(20, 50, 24)
            sazonalidade = np.sin(np.linspace(0, 4*np.pi, 24)) * 10
            ruido = np.random.normal(0, 2, 24)
            s_observada = pd.Series(tendencia + sazonalidade + ruido, index=datas)

            trend, seasonal, resid = decompor_serie_temporal(s_observada, 6)
            
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(s_observada.index, s_observada.values, label="Observado", color="#64748b")
            ax.plot(trend.index, trend.values, label="Tendência", color="#10b981", linewidth=2)
            ax.plot(seasonal.index, seasonal.values, label="Sazonalidade", color="#38bdf8")
            ax.set_ylabel("Uso de CPU (%)")
            ax.legend()
            fig.patch.set_facecolor("#f8fafc")
            ax.set_facecolor("#ffffff")
            for spine in ["top", "right"]:
                ax.spines[spine].set_visible(False)
            
            buf = io.BytesIO()
            plt.savefig(buf, format="png", bbox_inches="tight")
            buf.seek(0)
            chart_base64 = base64.b64encode(buf.read()).decode("utf-8")
            plt.close(fig)

        live_calculation = {
            "dados": "Série temporal de CPU simulada (24 horas, período=6)",
            "resultados": [
                {"label": "Gráfico de Decomposição", "value": "Disponível" if chart_base64 else "Pendente"}
            ],
            "chart": chart_base64
        }
        codigos_fonte = {
            "decompor_serie_temporal": obter_codigo_funcao(decompor_serie_temporal)
        }
    elif num == 11:
        # Semana 11: Regressão
        s11_reg = testar_funcao(ajuste_regressao_linear, [1, 2, 3], [2, 4, 5])
        valida_entrega = s11_reg is True

        horas = [1.0, 2.0, 3.0, 4.0, 5.0]
        ram = [30.0, 35.0, 41.0, 47.0, 52.0]
        eq_reta = None
        pred_12 = None
        if valida_entrega:
            a_coef, b_coef = ajuste_regressao_linear(horas, ram)
            eq_reta = f"RAM = {a_coef:.2f} * t + {b_coef:.2f}"
            pred_12 = f"{(a_coef * 12 + b_coef):.2f}%"

        live_calculation = {
            "dados": f"Horas: {horas} | RAM: {ram}",
            "resultados": [
                {"label": "Equação Ajustada", "value": eq_reta or "Pendente"},
                {"label": "Uso estimado em t=12h", "value": pred_12 or "Pendente"}
            ]
        }
        codigos_fonte = {
            "ajuste_regressao_linear": obter_codigo_funcao(ajuste_regressao_linear)
        }
    else:
        valida_entrega = True

    return render_template(
        "semana.html",
        num=num,
        title=meta.get("title", ""),
        icon=meta.get("icon", ""),
        conteudo=meta.get("conteudo", {}),
        tarefa=meta.get("tarefa", ""),
        validacao=meta.get("validacao", ""),
        status=status_atual,
        live=live_calculation,
        codigos=codigos_fonte,
        valida_entrega=valida_entrega,
        exercicios=meta.get("exercicios", [])
    )

@app.route("/semana/15/celebrar", methods=["POST"])
def celebrar():
    return jsonify({"status": "success", "message": "Parabéns pela conclusão do semestre!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
