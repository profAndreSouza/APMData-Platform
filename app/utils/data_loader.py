import pandas as pd
import numpy as np
import os

def gerar_dados_apm(num_registros: int = 100) -> pd.DataFrame:
    """
    Gera dados simulados de métricas de APM (tempo de resposta, CPU, RAM, etc.)
    para uso no dashboard e nas aulas.
    """
    np.random.seed(42)
    datas = pd.date_range(start="2026-06-01", periods=num_registros, freq="h")
    
    # Latência base em ms com ruído e spikes (anomalias de lentidão)
    latencia_base = 120.0
    tendencia_latencia = np.linspace(0, 50, num_registros) # Leve piora com o tempo
    ruido_latencia = np.random.normal(0, 15, num_registros)
    latencias = latencia_base + tendencia_latencia + ruido_latencia
    
    # Injeta alguns spikes críticos (ex: gargalo de banco de dados ou GC)
    latencias[15] = 1200.0
    latencias[55] = 3500.0
    latencias[85] = 1850.0
    
    # Uso de CPU (%) correlacionado com tráfego e latência
    uso_cpu = 15.0 + (latencias / 50.0) + np.random.normal(0, 5, num_registros)
    uso_cpu = np.clip(uso_cpu, 0.0, 100.0)
    
    # Uso de RAM (%) simulando um vazamento de memória (Memory Leak) gradual
    uso_ram = 30.0 + np.linspace(0, 45, num_registros) + np.random.normal(0, 1, num_registros)
    uso_ram = np.clip(uso_ram, 0.0, 100.0)
    
    # Endpoints e Status HTTP
    endpoints = ["/api/v1/checkout", "/api/v1/search", "/api/v1/login", "/api/v1/products"]
    status_opcoes = [200, 400, 404, 500]
    
    # Distribuição probabilística para endpoints e status
    eps = np.random.choice(endpoints, size=num_registros, p=[0.20, 0.40, 0.15, 0.25])
    
    status_codes = []
    for ep in eps:
        if ep == "/api/v1/checkout":
            # Checkout tem maior taxa de erro 500 simulada
            status = np.random.choice(status_opcoes, p=[0.75, 0.10, 0.05, 0.10])
        elif ep == "/api/v1/login":
            # Login tem mais 400 (Bad Request / Senha errada)
            status = np.random.choice(status_opcoes, p=[0.70, 0.20, 0.08, 0.02])
        else:
            status = np.random.choice(status_opcoes, p=[0.92, 0.04, 0.03, 0.01])
        status_codes.append(int(status))
        
    df = pd.DataFrame({
        "data_hora": datas,
        "tempo_resposta_ms": latencias,
        "uso_cpu_percent": uso_cpu,
        "uso_ram_percent": uso_ram,
        "endpoint": eps,
        "status_http": status_codes
    })
    
    return df
