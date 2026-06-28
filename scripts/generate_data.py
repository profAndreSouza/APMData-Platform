"""
Script utilitário para geração de dados de logs e métricas de APM simulados.
Gera um arquivo CSV de telemetria de performance ou insere dados diretamente no banco de dados.
"""
import argparse
import pandas as pd
import numpy as np
import psycopg2

def gerar_dados(num_leituras: int = 500):
    print(f"Gerando {num_leituras} registros de APM simulados...")
    np.random.seed(42)
    datas = pd.date_range(start="2026-06-01", periods=num_leituras, freq="h")
    
    # Latência base em ms com ruído e spikes (anomalias de lentidão)
    latencia_base = 120.0
    tendencia_latencia = np.linspace(0, 80, num_leituras)
    ruido_latencia = np.random.normal(0, 20, num_leituras)
    latencias = latencia_base + tendencia_latencia + ruido_latencia
    
    # Injeta alguns spikes críticos (ex: gargalo de banco de dados ou GC)
    indices_spikes = [int(num_leituras * 0.15), int(num_leituras * 0.55), int(num_leituras * 0.85)]
    for idx in indices_spikes:
        latencias[idx] += 1500.0 + np.random.uniform(500, 2000)
    latencias = np.clip(latencias, 10.0, 5000.0)
    
    # Uso de CPU (%) correlacionado com tráfego e latência
    uso_cpu = 10.0 + (latencias / 40.0) + np.random.normal(0, 4, num_leituras)
    uso_cpu = np.clip(uso_cpu, 0.0, 100.0)
    
    # Uso de RAM (%) simulando um vazamento de memória (Memory Leak) gradual
    uso_ram = 25.0 + np.linspace(0, 55, num_leituras) + np.random.normal(0, 1.2, num_leituras)
    uso_ram = np.clip(uso_ram, 0.0, 100.0)
    
    # Endpoints e Status HTTP
    endpoints = ["/api/v1/checkout", "/api/v1/search", "/api/v1/login", "/api/v1/products"]
    status_opcoes = [200, 400, 404, 500]
    
    eps = np.random.choice(endpoints, size=num_leituras, p=[0.20, 0.40, 0.15, 0.25])
    
    status_codes = []
    for ep in eps:
        if ep == "/api/v1/checkout":
            status = np.random.choice(status_opcoes, p=[0.75, 0.10, 0.05, 0.10])
        elif ep == "/api/v1/login":
            status = np.random.choice(status_opcoes, p=[0.70, 0.20, 0.08, 0.02])
        else:
            status = np.random.choice(status_opcoes, p=[0.92, 0.04, 0.03, 0.01])
        status_codes.append(int(status))

    df = pd.DataFrame({
        "data_hora": datas.strftime("%Y-%m-%d %H:%M:%S"),
        "tempo_resposta_ms": latencias,
        "uso_cpu_percent": uso_cpu,
        "uso_ram_percent": uso_ram,
        "endpoint": eps,
        "status_http": status_codes
    })
    
    return df

def salvar_csv(df: pd.DataFrame, caminho: str):
    df.to_csv(caminho, index=False)
    print(f"Dados salvos com sucesso em: {caminho}")

def popular_banco(df: pd.DataFrame, host: str, porta: int, db: str, user: str, psw: str):
    print(f"Conectando ao banco de dados PostgreSQL em {host}:{porta}...")
    try:
        conn = psycopg2.connect(
            host=host,
            port=porta,
            database=db,
            user=user,
            password=psw
        )
        cur = conn.cursor()
        
        # Cria a tabela caso não exista
        cur.execute("""
            CREATE TABLE IF NOT EXISTS logs_apm (
                id SERIAL PRIMARY KEY,
                data_hora TIMESTAMP UNIQUE NOT NULL,
                tempo_resposta_ms REAL NOT NULL,
                uso_cpu_percent REAL NOT NULL,
                uso_ram_percent REAL NOT NULL,
                endpoint VARCHAR(100) NOT NULL,
                status_http INTEGER NOT NULL
            );
        """)
        conn.commit()
        
        print("Inserindo registros...")
        for _, row in df.iterrows():
            try:
                cur.execute("""
                    INSERT INTO logs_apm (data_hora, tempo_resposta_ms, uso_cpu_percent, uso_ram_percent, endpoint, status_http)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (data_hora) DO NOTHING;
                """, (row['data_hora'], row['tempo_resposta_ms'], row['uso_cpu_percent'], row['uso_ram_percent'], row['endpoint'], row['status_http']))
            except Exception as insert_err:
                print(f"Aviso ao inserir linha: {insert_err}")
                
        conn.commit()
        cur.close()
        conn.close()
        print("Carga de dados de APM concluída!")
    except Exception as e:
        print(f"Erro ao conectar ou operar no banco de dados: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulador de Métricas APM InduData")
    parser.add_argument("--csv", type=str, default="dados_apm.csv", help="Caminho do arquivo CSV de saída")
    parser.add_argument("--n", type=int, default=500, help="Quantidade de registros a gerar")
    parser.add_argument("--db-populate", action="store_true", help="Se ativado, envia os dados gerados para o banco de dados")
    parser.add_argument("--db-host", type=str, default="localhost", help="Host do banco de dados")
    parser.add_argument("--db-port", type=int, default=5432, help="Porta do banco de dados")
    parser.add_argument("--db-name", type=str, default="indudata", help="Nome do banco de dados")
    parser.add_argument("--db-user", type=str, default="postgres", help="Usuário do banco de dados")
    parser.add_argument("--db-pass", type=str, default="postgres_indudata", help="Senha do banco de dados")
    
    args = parser.parse_args()
    
    df = gerar_dados(args.n)
    salvar_csv(df, args.csv)
    
    if args.db_populate:
        popular_banco(df, args.db_host, args.db_port, args.db_name, args.db_user, args.db_pass)
