# 🏭 InduData Platform - Guia Integrado de Projetos

Este repositório contém a infraestrutura e a base do projeto prático integrador para as disciplinas de **Ciência de Dados**, **Computação em Nuvem** e **DevOps**.

---

## 🎯 Objetivo Pedagógico

O objetivo é que os alunos desenvolvam uma plataforma real de **Manutenção Preditiva** para monitoramento de motores elétricos industriais. 
Ao longo das **15 semanas**, os alunos irão:
1. **Ciência de Dados**: Codificar funções estatísticas básicas em Python, criar testes de hipóteses, realizar análises de séries temporais e modelos preditivos lineares.
2. **Computação em Nuvem**: Provisionar recursos na **AWS** (S3, EC2, RDS, VPC, Lambda) alinhados com o currículo de **AWS Academy Cloud Developing**.
3. **DevOps**: Montar o repositório, dockerizar a aplicação, rodar testes no GitHub Actions e automatizar o deploy contínuo (CD) na AWS.

---

## ☁️ Integração de Labs - AWS Academy Cloud Developing

Para consolidar os conhecimentos de **Computação em Nuvem**, os alunos devem concluir o curso oficial **AWS Academy Cloud Developing**. Os laboratórios práticos do curso estão integrados ao cronograma do projeto da seguinte forma:

| Semana | Laboratório AWS Academy | Foco do Laboratório | Aplicação no Projeto Integrador |
| :--- | :--- | :--- | :--- |
| **Semana 2** | *Lab 1: Working with IAM* | Permissões, Policies e Roles | Configurar o acesso seguro para a equipe de DevOps e leitura de dados. |
| **Semana 6** | *Lab 3: RDS Application Databases* | Provisionamento de Banco Relacional | Criação da base de dados PostgreSQL para persistir os registros de falhas. |
| **Semana 7** | *Lab 2: AWS SDK (Boto3) & Lab 4: DynamoDB* | Programação com SDK em Python | Desenvolver scripts em Python (`s3_service.py`) para ler e salvar CSVs no S3. |
| **Semana 9** | *Lab 6: AWS Lambda & API Gateway* | Serverless e Microsserviços | Publicar um endpoint serverless para receber triggers rápidos de novos logs. |
| **Semana 10** | *Lab 5: EventBridge & SNS + Lab 7: SQS* | Mensageria e Eventos | Enviar alertas assíncronos para o e-mail do time técnico em caso de anomalia. |
| **Semana 11** | *Lab 9: Beanstalk, ECS or AWS SAM* | Orquestração e Deploy Automatizado | Implantar a aplicação conteinerizada Streamlit em infraestrutura escalável. |
| **Semana 12** | *Lab 8: AWS KMS & Secrets Manager* | Criptografia e Proteção de Credenciais | Armazenar de forma segura a senha de conexão do RDS e chaves de APIs. |

---

## 🏗️ Estrutura do Projeto

```text
indudata-platform/
│
├── .github/workflows/          # [DevOps] CI/CD Pipelines (semana 5, 8 e 12)
│   └── ci.yml                  # Validação de testes no Git push/PR
│
├── app/                        # [Ciência de Dados & Nuvem] Código do Dashboard
│   ├── core/                   # Algoritmos estatísticos (desafios dos alunos)
│   │   ├── stats.py            # Semanas 2 e 3: Estatística Descritiva
│   │   ├── sampling.py         # Semana 4: Amostragem de Dados
│   │   ├── hypothesis.py       # Semanas 6 e 7: Testes de Hipóteses
│   │   └── time_series.py      # Semanas 8, 9, 10 e 11: Regressão e Séries Temporais
│   │
│   ├── services/               # [Nuvem] Integração AWS (Semanas 6, 7 e 10)
│   │   ├── s3_service.py       # Integração com S3 (Boto3)
│   │   └── db_service.py       # Conexão com AWS RDS PostgreSQL
│   │
│   └── main.py                 # Interface Streamlit do Painel Industrial
│
├── tests/                      # [DevOps] Testes de Correção Automática
│   ├── test_stats.py
│   ├── test_sampling.py
│   ├── test_hypothesis.py
│   └── test_time_series.py
│
├── scripts/                    # Scripts utilitários
│   └── generate_data.py        # Gerador de dados de simulação
│
├── Dockerfile                  # [DevOps] Dockerização da App (Semana 3)
├── docker-compose.yml          # [DevOps] Orquestrador local (Semana 4)
└── requirements.txt            # Dependências Python
```

---

## 🚀 Como Executar Localmente

### 1. Ambiente Virtual Python (Local)
Para rodar a aplicação localmente instalando as dependências na sua máquina:

```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente (Windows)
.\venv\Scripts\activate

# Instala as dependências
pip install -r requirements.txt

# Executa o painel
streamlit run app/main.py
```

### 2. Rodando com Docker Compose (Semana 4+)
Se já tiver o Docker instalado, você pode levantar a aplicação Streamlit conectada a um banco de dados PostgreSQL com um único comando:

```bash
docker-compose up --build
```
Acesse o painel em `http://localhost:8501`.

---

## 📖 Atividades Semana a Semana & Guia do Professor

### 🔹 Semana 1: Setup do Ambiente e Git (CD + CN + DevOps)
*   **Ciência de Dados**: Apresentação dos dados e discussões sobre escalas de medição (latência em ms, CPU/RAM em %).
*   **Computação em Nuvem**: Conceitos de Cloud e introdução ao AWS Pricing Calculator.
*   **DevOps**: Os alunos criam um Fork deste repositório e clonam localmente. Configuram o Git.

### 🔹 Semana 2: Tendência Central (CD + CN)
*   **Desafio Python**: Implementar `calcular_media` e `calcular_mediana` em `app/core/stats.py`.
*   **Gabarito Esperado**:
    ```python
    def calcular_media(valores: list[float]) -> float:
        return sum(valores) / len(valores) if valores else 0.0

    def calcular_mediana(valores: list[float]) -> float:
        if not valores: return 0.0
        s = sorted(valores)
        n = len(s)
        if n % 2 == 1:
            return float(s[n // 2])
        return (s[(n // 2) - 1] + s[n // 2]) / 2.0
    ```
*   **Discussão Estatística**: A latência média foi de $210$ ms, mas a mediana foi de $125$ ms. Por quê? (Devido aos spikes ocasionais de resposta do banco que distorcem a média, mostrando a importância do P50/P99 em APM).

### 🔹 Semana 3: Dispersão e Containerização (CD + DevOps)
*   **Desafio Python**: Implementar `calcular_variancia`, `calcular_desvio_padrao` e `calcular_amplitude` em `app/core/stats.py`.
*   **DevOps**: Explicar e construir o `Dockerfile`. Os alunos empacotam o Streamlit em um container e o rodam localmente.

### 🔹 Semana 4: Amostragem e Redes (CD + CN + DevOps)
*   **Desafio Python**: Implementar `amostragem_sistematica` em `app/core/sampling.py`.
*   **Nuvem/Redes**: Criação da VPC na AWS. Discussão de custos de **Data Transfer** na AWS.

### 🔹 Semana 5: Dashboard e CI (CD + DevOps)
*   **Desafio**: Conectar o Dashboard Streamlit às funções criadas.
*   **DevOps**: Ligar o pipeline de CI do GitHub Actions (`.github/workflows/ci.yml`) rodando o Linter.

### 🔹 Semana 6: Testes de Hipótese e Banco de Dados (CD + CN)
*   **Desafio Python**: Usar `scipy.stats.shapiro` para o teste de Shapiro-Wilk em `app/core/hypothesis.py` para descobrir se o tempo de resposta segue distribuição normal.
*   **Gabarito**:
    ```python
    def teste_shapiro_wilk(valores: list[float]) -> tuple[float, float, bool]:
        stat, p_val = stats.shapiro(valores)
        return stat, p_val, bool(p_val >= 0.05)
    ```
*   **Nuvem**: Criar uma instância RDS PostgreSQL na AWS. Comparativo de custos: IaaS vs PaaS para banco.

### 🔹 Semana 7: Associação Categórica (CD + DevOps)
*   **Desafio Python**: Implementar teste de Qui-Quadrado (`scipy.stats.chi2_contingency`) para provar se a taxa de erros HTTP 500 está associada a endpoints específicos.
*   **DevOps**: Enviar a imagem Docker da aplicação automaticamente para o **Docker Hub** via GitHub Actions.

### 🔹 Semana 8: Correlação e CD para o EC2 (CD + DevOps)
*   **Desafio Python**: Implementar a fórmula clássica de Pearson em `app/core/time_series.py` para identificar a correlação entre consumo de CPU e tráfego de requisições.
*   **Gabarito**:
    ```python
    def calcular_correlacao_pearson(x: list[float], y: list[float]) -> float:
        n = len(x)
        media_x = sum(x) / n
        media_y = sum(y) / n
        num = sum((xi - media_x) * (yi - media_y) for xi, yi in zip(x, y))
        den_x = sum((xi - media_x)**2 for xi in x)
        den_y = sum((yi - media_y)**2 for yi in y)
        return num / math.sqrt(den_x * den_y) if den_x and den_y else 0.0
    ```
*   **DevOps**: Configurar deploy automático do container Docker na instância EC2 via GitHub Actions.

### 🔹 Semanas 9 e 10: Séries Temporais e Monitoramento na AWS (CD + CN)
*   **Desafio Python**: Implementar médias móveis e decomposição de séries temporais em `app/core/time_series.py`.
*   **Nuvem**: Configurar alertas automáticos de CPU/Tráfego via Amazon SNS/SQS.

### 🔹 Semana 11: Predição e Alta Disponibilidade (CD + CN)
*   **Desafio Python**: Ajustar regressão linear simples (Mínimos Quadrados) no histórico de RAM para prever gargalos de vazamento de memória (Capacity Planning).
*   **Nuvem**: Configuração de Load Balancer (ELB) e Auto Scaling (ASG). Análise de custos de escalabilidade.

### 🔹 Semana 12: Métricas de Predição e Segurança (CD + CN + DevOps)
*   **Desafio**: Validar predições com métricas de erro MSE/RMSE.
*   **Nuvem/DevOps**: Usar AWS Secrets Manager para obter senhas de banco de forma segura.

### 🔹 Semana 13: IaC com Terraform (CN + DevOps)
*   **Desafio**: Criar script simples de Terraform para gerenciar a infraestrutura.

### 🔹 Semana 14: Observabilidade e Otimização de Custos (CN + DevOps)
*   **Desafio**: Revisar a arquitetura baseada no AWS Well-Architected Pillar de Cost Optimization.

### 🔹 Semana 15: Entrega Final do Projeto Integrado
*   Os alunos realizam o "Code Freeze" e defendem o sistema completo rodando na AWS acompanhado do relatório financeiro estimando custos de faturamento da infraestrutura.

