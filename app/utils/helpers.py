import os

def testar_funcao(func, *args, **kwargs):
    """
    Retorna True se a função executa sem NotImplementedError, 
    'NotImplemented' caso contrário, ou 'RuntimeError' para outros erros.
    """
    if func is None:
        return "NotImplemented"
    try:
        func(*args, **kwargs)
        return True
    except NotImplementedError:
        return "NotImplemented"
    except Exception:
        return "RuntimeError"

def obter_readme_markdown() -> str:
    """Carrega dinamicamente o arquivo README.md da raiz do projeto."""
    caminho_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_readme = os.path.join(caminho_dir, "../../README.md")
    
    if not os.path.exists(caminho_readme):
        caminho_readme = "README.md"
        
    if os.path.exists(caminho_readme):
        try:
            with open(caminho_readme, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Não foi possível ler o arquivo README.md: {e}"
    return ""

def obter_codigo_funcao(func) -> str:
    """Retorna o código-fonte de uma função em formato string."""
    import inspect
    if func is None:
        return "Função não importada ou indisponível."
    try:
        return inspect.getsource(func)
    except Exception as e:
        return f"Não foi possível ler o código-fonte: {e}"

def obter_semana_info(num: int) -> dict:
    """Retorna metadados teóricos e descrições detalhadas da semana solicitada."""
    semanas = {
        1: {
            "title": "Setup & Git",
            "icon": "🔧",
            "conteudo": {
                "cd": "Apresentação da telemetria APM/Sensores e escalas de medição. Classificamos variáveis em quatro níveis fundamentais: Nominal (rótulos qualitativos como ID do sensor ou status do motor), Ordinal (ordenamento sem distância métrica exata, ex: criticidade de alerta Leve/Médio/Grave), Intervalar (valores numéricos com zero arbitrário, ex: temperatura em °C) e Razão (valores métricos reais com zero absoluto, ex: latência em ms, vibração mecânica).",
                "cloud": "Introdução ao faturamento na AWS. Estudo da estrutura de cobrança Pay-as-you-go (pagamento pelo uso efetivo), políticas de Free Tier (níveis gratuitos) e a utilização do AWS Pricing Calculator para estimar custos iniciais de armazenamento de dados brutos de sensores.",
                "devops": "Cultura DevOps baseada nos pilares de colaboração, automação e monitoramento contínuo. Introdução ao Git como base para controle de versão, conceitos de commits atômicos e inicialização do repositório local de sensores."
            },
            "tarefa": "Realizar o fork do repositório, clonar localmente e configurar o ambiente virtual do Python (pip install -r requirements.txt).",
            "validacao": "Semana de Setup. Nenhuma função de código estatístico é validada nesta semana.",
            "exercicios": [
                "Classifique as seguintes variáveis de monitoramento mecânico nas quatro escalas de medição: 1) Status da bomba (Ligada/Desligada), 2) Índice de vibração (em Hz), 3) Criticidade da falha (Urgente, Alta, Média), 4) Temperatura interna do mancal (em Kelvin). Justifique cada escolha.",
                "Acesse o AWS Pricing Calculator e estime o custo mensal para armazenar 150GB de dados em um Bucket S3 na região de São Paulo, considerando operações básicas de escrita (PUT) e leitura (GET) realizadas por 1.000 requisições diárias."
            ]
        },
        2: {
            "title": "Tendência Central & IAM",
            "icon": "📏",
            "conteudo": {
                "cd": "Estatística Descritiva focada em Medidas de Tendência Central: Média Aritmética (ponto de equilíbrio matemático da distribuição), Mediana (P50 - o valor que divide os dados ordenados exatamente em 50% menores e 50% maiores, imune a outliers extremos de sensores) e a Moda (valores que mais se repetem, útil para classificar falhas de rotina em motores).",
                "cloud": "AWS Global Infrastructure: divisão em Regiões geográficas e Zonas de Disponibilidade (AZs) redundantes. Segurança baseada no Princípio do Menor Privilégio com AWS IAM (Identity and Access Management), configurando políticas de segurança em formato JSON, grupos de acesso e roles de execução para leitura/escrita do RDS.",
                "devops": "Colaboração e versionamento no Git utilizando branching strategies (Git Flow). Conceito de Pull Requests (PRs), code review sistemático para validação de algoritmos e práticas de escrita de commits semânticos (Conventional Commits)."
            },
            "tarefa": "Implementar as funções `calcular_media` e `calcular_mediana` no arquivo `app/core/stats.py` sem usar funções de agregação prontas (ex: `sum()` ou `statistics.median()`).",
            "validacao": "Validado executando a média e mediana amostral sobre dados simulados.",
            "exercicios": [
                "Imagine que a latência de coleta de um motor elétrico apresentou as seguintes medições: [12, 15, 14, 12, 18, 900, 11] ms. Calcule manualmente a Média e a Mediana deste conjunto. Explique qual das duas medidas descreve melhor a experiência típica de monitoramento da máquina e por que a outra foi severamente afetada.",
                "Escreva uma política IAM em formato JSON que permita que uma aplicação execute exclusivamente ações de leitura ('s3:GetObject') e listagem ('s3:ListBucket') no bucket chamado 'indudata-sensor-logs'."
            ]
        },
        3: {
            "title": "Variabilidade & EC2 Pricing",
            "icon": "📊",
            "conteudo": {
                "cd": "Medidas de Dispersão e Variabilidade: Amplitude (R - diferença entre máximo e mínimo), Variância Amostral (s² - média ponderada dos quadrados dos desvios, com denominador N-1 para compensar viés amostral) e Desvio Padrão (s - a raiz quadrada da variância, trazendo a dispersão de volta para a unidade original do dado). Medidas úteis para quantificar o Jitter (oscilação/instabilidade) de vibração de mancais.",
                "cloud": "Estudo de computação elástica com AWS EC2 (Elastic Compute Cloud). Comparativo financeiro entre modelos de contratação: On-Demand (sem compromisso, ideal para testes), Instâncias Reservadas (descontos de até 72% para contratos de 1 a 3 anos) e Spot Instances (uso de capacidade sobressalente da AWS com descontos de até 90%, mas sujeitas a interrupções).",
                "devops": "Virtualização por container com Docker. Filosofia de empacotamento isolado (isolamento de processos, rede e sistemas de arquivos). Escrita de um Dockerfile otimizado em múltiplas camadas (multi-stage builds) para reduzir a superfície de ataque e o tamanho da imagem da aplicação."
            },
            "tarefa": "Implementar as funções `calcular_variancia`, `calcular_desvio_padrao` e `calcular_amplitude` em `app/core/stats.py`. Dockerizar a aplicação Flask do APM.",
            "validacao": "Validado executando variância amostral com divisor N-1 e amplitude.",
            "exercicios": [
                "Dois motores elétricos idênticos foram monitorados quanto à vibração (Hz) ao longo de 5 minutos. O Motor A obteve média = 60Hz e desvio padrão = 1.2Hz. O Motor B obteve média = 60Hz e desvio padrão = 15.6Hz. Do ponto de vista de manutenção preditiva, qual motor apresenta indícios de desgaste mecânico iminente e por quê?",
                "Escreva um Dockerfile de referência para uma aplicação Flask simples em Python 3.11. Certifique-se de expor a porta correta, instalar as dependências de um arquivo 'requirements.txt' e definir um usuário não-root (não-administrador) por motivos de segurança."
            ]
        },
        4: {
            "title": "Amostragem & Custos de Rede",
            "icon": "🔀",
            "conteudo": {
                "cd": "Teoria e técnicas de amostragem estatística: Amostragem Aleatória Simples (seleção de registros equiprováveis), Amostragem Sistemática (seleção a cada intervalo constante 'k', ideal para fluxos de telemetria contínuos) e Amostragem Estratificada Proporcional (subdivisão da população em estratos homogêneos, como por ID do motor, garantindo representatividade proporcional de cada equipamento no conjunto de análise).",
                "cloud": "Conceitos de redes com AWS VPC (Virtual Private Cloud), subredes públicas e privadas, regras de Security Groups e custos de Data Transfer. Análise de custos ocultos de tráfego de dados na AWS (tráfego entre diferentes AZs, transferência para a internet e custos de IPs públicos).",
                "devops": "Orquestração de múltiplos containers locais usando o Docker Compose. Configuração de volumes persistentes para que os dados do banco de dados não sejam perdidos no reinício do container e mapeamento de redes internas isoladas."
            },
            "tarefa": "Implementar as funções de `amostragem_sistematica` e `amostragem_estratificada` em `app/core/sampling.py` para reduzir a base de análise do APM.",
            "validacao": "Validado executando amostragem sistemática de passo k=N/n.",
            "exercicios": [
                "Você possui um log com 1.000.000 de registros contendo dados de 4 motores diferentes em proporções muito desiguais: Motor 1 (80% dos logs), Motor 2 (15%), Motor 3 (4%) e Motor 4 (1%). Explique por que utilizar uma Amostragem Aleatória Simples para reduzir o conjunto de dados para 1.000 registros pode ocultar falhas no Motor 4. Qual o método de amostragem ideal para este cenário?",
                "Projete um arquivo docker-compose.yml que suba dois serviços interconectados: um banco PostgreSQL (com senha e banco configurados nas variáveis de ambiente e dados persistidos em um volume) e o backend Python exposto na porta 5000."
            ]
        },
        5: {
            "title": "Visualização & S3 Lifecycle Pricing",
            "icon": "🖥️",
            "conteudo": {
                "cd": "Comunicação visual e exploração de dados: Gráficos de Linha (ideais para tendências temporais), Gráficos de Dispersão (correlações entre variáveis), Histogramas (distribuição de frequência) e Boxplots (identificação visual rápida de mediana, quartis e outliers de sensores).",
                "cloud": "Armazenamento em nuvem com AWS S3 (Simple Storage Service). Comparativo de precificação entre classes: S3 Standard (dados quentes), S3 Infrequent Access (acesso eventual, menor custo de armazenamento, mas cobra taxa de leitura) e S3 Glacier (arquivamento de longa data, altíssima economia). Definição de regras de ciclo de vida (Lifecycle Rules) para transição de classes.",
                "devops": "Integração Contínua (CI) automatizada. Configuração de esteira no GitHub Actions por meio de arquivos YAML. Automação de linters e formatação automática de código (ex: Black e Flake8) para manter a qualidade de código do repositório."
            },
            "tarefa": "Concluir os gráficos de telemetria do Dashboard e ativar a esteira de CI com Linter (Black/Flake8) disparando no git push.",
            "validacao": "Dashboard estruturado! Certifique-se de que a automação do GitHub Actions (.github/workflows/ci.yml) está rodando sem erros no GitHub.",
            "exercicios": [
                "A vibração de uma máquina apresentou um pico anormal. Em qual tipo de visualização gráfica (Histograma ou Boxplot) esse pico será mais facilmente identificado como um ponto isolado além dos limites da distribuição (Outlier)? Justifique sua resposta.",
                "Uma fábrica gera 10GB de logs de telemetria por dia. Os operadores precisam de acesso instantâneo a esses dados apenas nos primeiros 30 dias. Depois, as auditorias fiscais exigem que os logs fiquem salvos por 5 anos, mas o acesso pode demorar algumas horas para ser recuperado. Projete a estratégia de classes do S3 e as Lifecycle Rules ideais para reduzir o custo ao mínimo."
            ]
        },
        6: {
            "title": "Normalidade & RDS vs EC2 Pricing",
            "icon": "📉",
            "conteudo": {
                "cd": "Princípios de Inferência Estatística e Testes de Hipótese. Teste de Shapiro-Wilk para testar a aderência à Distribuição Normal (Gaussiana). Definição de Hipótese Nula (H0 - a amostra provém de uma população normal) e nível de significância alpha = 0.05. Se p-valor < 0.05, rejeita-se H0, provando que a latência/oscilação do motor é instável e possui comportamento anômalo.",
                "cloud": "Bancos de dados relacionais gerenciados com Amazon RDS (Relational Database Service) PostgreSQL. Análise comparativa de custos de manutenção e administração: provisionar banco em máquina própria EC2 (IaaS - maior gerência e trabalho de backup/patches manual) vs utilizar o RDS (PaaS - backups automáticos, alta disponibilidade e menor sobrecarga operacional).",
                "devops": "Automação de testes de regressão. Integração de testes automatizados unitários (`pytest`) na esteira de CI, forçando a falha da build e impedindo deploy caso alguma alteração quebre os cálculos estatísticos fundamentais."
            },
            "tarefa": "Implementar `teste_shapiro_wilk` em `app/core/hypothesis.py`. Conectar a aplicação ao banco de dados Amazon RDS PostgreSQL provisionado.",
            "validacao": "Validado testando a hipótese de normalidade da latência usando o teste estatístico Shapiro-Wilk.",
            "exercicios": [
                "Você executou o teste de Shapiro-Wilk sobre os desvios de rotação de um motor e obteve W = 0.985 e p-valor = 0.0012. Explique detalhadamente a decisão estatística que você deve tomar em relação à hipótese nula (H0) e qual a interpretação operacional que o time de engenharia deve tirar sobre o funcionamento deste motor.",
                "Em qual situação de negócio uma corporação pode preferir alocar um banco de dados relacional em instâncias EC2 do que migrar para o RDS, mesmo tendo que gerenciar manualmente backups e atualizações?"
            ]
        },
        7: {
            "title": "Associação Categórica & SDK Boto3",
            "icon": "📈",
            "conteudo": {
                "cd": "Análise de variáveis categóricas qualitativas. Teste de Qui-Quadrado de Independência / Associação. Construção da Tabela de Contingência (Frequências Observadas vs Esperadas). O teste avalia se a relação entre duas variáveis nominais/ordinais (ex: Turno de trabalho A/B/C vs Estado do Motor Funcionando/Falho) ocorre por mero acaso ou se existe uma associação estatisticamente significativa.",
                "cloud": "Integração programática com recursos AWS usando o SDK oficial para Python (Boto3). Configuração de conexões com clientes e recursos S3, manipulação de arquivos (uploads e downloads de arquivos JSON de sensores) e tratamento de erros de credenciais.",
                "devops": "Gerenciamento de repositórios de imagens de container. Registro e publicação automática da imagem compilada da aplicação no Docker Hub via workflows do GitHub Actions utilizando GitHub Secrets para gerenciar tokens e credenciais seguras."
            },
            "tarefa": "Implementar `teste_qui_quadrado_associacao` em `app/core/hypothesis.py`. Adicionar código no pipeline para gerar a tag da imagem Docker e enviar ao Docker Hub.",
            "validacao": "Validado rodando o teste qui-quadrado de independência sobre tabelas de contingência de endpoints.",
            "exercicios": [
                "Considere a seguinte tabela de contingência contendo falhas registradas em motores mecânicos nos turnos diurno e noturno: Turno Diurno (10 falhas, 90 normais) | Turno Noturno (35 falhas, 65 normais). Calcule o valor do teste de Qui-Quadrado de associação ou explique teoricamente: com um p-valor menor que 0.001, o que podemos concluir sobre a relação entre o turno de trabalho e a taxa de falha dos motores?",
                "Escreva uma rotina simples em Python utilizando a biblioteca Boto3 para carregar localmente um arquivo JSON contendo telemetria industrial de um Bucket S3 da AWS, tratando possíveis exceções de autenticação."
            ]
        },
        8: {
            "title": "Correlação & Custos CloudWatch",
            "icon": "🔗",
            "conteudo": {
                "cd": "Análise de associação linear de variáveis quantitativas com o Coeficiente de Correlação de Pearson (r). O coeficiente quantifica a força e a direção da relação linear, variando entre -1 (relação inversa perfeita, ex: nível de óleo vs temperatura) e +1 (relação direta perfeita, ex: rotações RPM vs vibração do motor).",
                "cloud": "Observabilidade e monitoramento de performance com AWS CloudWatch. Definição de custos associados à ingestão de métricas e retenção de logs de telemetria por GB ingerido. Criação de alarmes baseados em limites de faturamento e custos para evitar surpresas na conta da nuvem.",
                "devops": "Entrega Contínua (CD) clássica para ambientes IaaS (EC2). Escrita de scripts de shell com conexões SSH automatizadas via GitHub Actions para realizar pull da imagem Docker atualizada no Docker Hub e reiniciar o container na produção."
            },
            "tarefa": "Implementar `calcular_correlacao_pearson` em `app/core/time_series.py`. Integrar o script de deploy automatizado por SSH na pipeline do GitHub Actions.",
            "validacao": "Validado rodando o cálculo de Pearson entre requisições de entrada e uso de CPU.",
            "exercicios": [
                "Você calculou a correlação de Pearson entre a temperatura de um motor e sua vibração física obtendo r = 0.88. Entre o nível de lubrificação e o calor gerado, obteve r = -0.72. O que essas correlações indicam do ponto de vista de desgaste e prevenção mecânica?",
                "Projete um fluxo básico de deploy contínuo (CD) em um script Bash que conecte via SSH em uma máquina virtual Linux remota, baixe a última imagem Docker gerada no Docker Hub e substitua o container atual pelo novo container minimizando o tempo de indisponibilidade."
            ]
        },
        9: {
            "title": "Sazonalidade & Custos Serverless",
            "icon": "⏳",
            "conteudo": {
                "cd": "Introdução à modelagem de Séries Temporais. Componentes de dados organizados no tempo: Tendência (comportamento de longo prazo), Sazonalidade (padrões periódicos repetitivos, ex: oscilação de temperatura em horários mais quentes do dia) e o Ruído/Irregularidade (flutuações aleatórias sem padrão estatístico).",
                "cloud": "Arquitetura computacional orientada a eventos e Serverless. Provisionamento e precificação baseada no consumo real com AWS Lambda (cobrança por milissegundo de execução e alocação de memória) e API Gateway. Estudo comparativo de custos entre manter servidores dedicados ligados 24/7 vs usar funções Lambda.",
                "devops": "Deploy Serverless automatizado. Escrita de workflows GitHub Actions voltados para o empacotamento, empacotamento em zip e upload automatizado do código Python para funções AWS Lambda utilizando ferramentas de linha de comando CLI."
            },
            "tarefa": "Desenvolver uma função simples em Python para rodar como Lambda na AWS. Estimar o custo de rodar essa função comparado a manter uma instância EC2 rodando direto.",
            "validacao": "Atividade validada por meio de entrega dos relatórios de custos e códigos Serverless no repositório.",
            "exercicios": [
                "Em manutenção de motores industriais, qual o significado operacional e prático do componente de 'Tendência' em uma série temporal de vibração contínua?",
                "Uma fábrica necessita de um endpoint HTTP para receber dados de vibração de 1.000 motores. Cada motor envia dados 1 vez por minuto. Calcule o número total de execuções mensais e compare o custo aproximado entre manter uma máquina EC2 t3.medium ($30/mês fixa) e uma arquitetura baseada em AWS Lambda ($0.20 por milhão de execuções)."
            ]
        },
        10: {
            "title": "Decomposição & SNS/SQS Pricing",
            "icon": "📡",
            "conteudo": {
                "cd": "Análise avançada de Séries Temporais: Decomposição Clássica Aditiva (Yt = Tt + St + It) para isolar a Tendência e Sazonalidade do Ruído. Técnicas de suavização para remoção de spikes e anomalias pontuais, facilitando a identificação visual de avaria física crônica no longo prazo.",
                "cloud": "Arquitetura desacoplada e assíncrona. AWS SQS (Simple Queue Service) para filas de mensagens resilientes (comparativo FIFO vs Standard) e AWS SNS (Simple Notification Service) para notificações multicanal (alertas de SMS, e-mails de incidentes e webhooks). Estrutura de preços baseada no volume de requisições e envios.",
                "devops": "Observabilidade e centralização de registros de container. Configuração dos drivers de log nativos do Docker (Docker Log Drivers) para encaminhar automaticamente a saída padrão de execução do container Flask para o CloudWatch Logs da AWS."
            },
            "tarefa": "Implementar a função `decompor_serie_temporal` em `app/core/time_series.py`. Integrar alertas automatizados por e-mail com Amazon SNS.",
            "validacao": "Validado rodando decomposição aditiva de uso de CPU com sazonalidade.",
            "exercicios": [
                "Após aplicar a decomposição aditiva na temperatura de um motor industrial, você observou que a 'Sazonalidade' apresenta comportamento diário estável, mas a 'Tendência' está subindo continuamente. O que isso indica operacionalmente e qual decisão de manutenção preditiva deve ser tomada?",
                "Explique como a utilização de filas assíncronas do AWS SQS pode proteger a aplicação InduData contra a perda de registros em tempo real em momentos de picos súbitos de leitura de sensores industriais."
            ]
        },
        11: {
            "title": "Capacity Planning & Fargate Pricing",
            "icon": "🔮",
            "conteudo": {
                "cd": "Capacity Planning estatístico utilizando Regressão Linear Simples. Método dos Mínimos Quadrados Ordinários (MQO) para encontrar os coeficientes angular (a - taxa de crescimento de uso de recursos por unidade de tempo) e linear (b - intercepto, estimativa de uso no tempo inicial zero) da reta matemática y = a*x + b.",
                "cloud": "Alta disponibilidade e escalabilidade. Provisionamento de balanceadores de carga AWS ELB (Elastic Load Balancing) e grupos de Auto Scaling (ASG). Precificação baseada no ECS Fargate, calculando o consumo sob demanda de CPU e RAM por hora por tarefa ativa.",
                "devops": "Deploy de containers em serviços serverless em nuvem. Configuração e automação do processo de implantação contínua para hospedar o container Flask no AWS App Runner ou AWS ECS Fargate, configurando regras de roteamento."
            },
            "tarefa": "Implementar `ajuste_regressao_linear` em `app/core/time_series.py`. Rodar o deploy automatizado da aplicação para um serviço gerenciado escalável (App Runner/ECS).",
            "validacao": "Validado computando inclinação (a) e intercepto (b) da reta de tendência de RAM.",
            "exercicios": [
                "O modelo de regressão linear para prever a temperatura de um motor obteve a equação: Temp = 0.45 * Hora + 35.0. Se o motor não pode exceder a temperatura crítica de 75°C sob risco de fundir, estime em quantas horas de operação contínua ele atingirá essa temperatura.",
                "Explique qual a vantagem operacional e econômica de configurar o Auto Scaling baseado no consumo de CPU ao invés de manter instâncias EC2 superdimensionadas ligadas de forma estática na nuvem."
            ]
        },
        12: {
            "title": "Métricas & Secrets Manager Pricing",
            "icon": "🔐",
            "conteudo": {
                "cd": "Validação e avaliação de precisão de modelos estatísticos e matemáticos de predição. Métricas de erro fundamentais: Erro Médio Absoluto (MAE - média dos desvios absolutos), Erro Quadrático Médio (MSE - que penaliza erros grandes de forma quadrática) e a Raiz do Erro Quadrático Médio (RMSE - trazendo o erro de volta para a escala do dado original).",
                "cloud": "Segurança de dados sensíveis e criptografia. Utilização do AWS Secrets Manager para gerenciar credenciais (como senhas do banco RDS e chaves de APIs) de forma rotativa e segura. AWS KMS (Key Management Service) para controle de chaves de criptografia e precificação baseada em chamadas de API e segredos ativos.",
                "devops": "Configuração de conexões seguras sem chaves estáticas. Autenticação baseada em OIDC (OpenID Connect) para que o GitHub Actions se comunique com a AWS gerando tokens temporários seguros, eliminando credenciais de longo prazo."
            },
            "tarefa": "Configurar o AWS Secrets Manager para gerenciar a senha do RDS. Integrar a leitura do segredo na aplicação utilizando o Boto3.",
            "validacao": "Segurança e segredos integrados! Valide o fluxo de credenciais seguras no pipeline de deploy.",
            "exercicios": [
                "Você treinou dois algoritmos diferentes para prever a vibração de um motor. O Algoritmo 1 obteve RMSE = 2.3Hz. O Algoritmo 2 obteve RMSE = 8.9Hz. Do ponto de vista de confiabilidade industrial, qual modelo você deve implantar em produção e como você interpreta a diferença métrica do erro?",
                "Explique os riscos de segurança de manter credenciais de banco de dados (host, usuário e senha) salvas em texto puro dentro do código do repositório Git, e de que forma o Secrets Manager resolve essa falha."
            ]
        },
        13: {
            "title": "Dashboard Final & Precificação de IaC",
            "icon": "🏗️",
            "conteudo": {
                "cd": "Consolidação e visualização de resultados de Ciência de Dados. Estruturação final do painel de monitoramento preditivo para visualização integrada de tendência central, dispersão, normalidade, regressão e gráficos em tempo real.",
                "cloud": "Introdução à Infraestrutura como Código (IaC). Princípios de automação, versionamento e idoneidade do provisionamento de recursos de nuvem, permitindo recriar a arquitetura inteira de forma automatizada por comandos.",
                "devops": "Escrita e provisionamento de infraestrutura usando Terraform. Configuração de arquivos declarativos HCL (`main.tf`, `variables.tf`) para provisionar de forma reprodutível instâncias EC2, buckets S3 e redes VPC no pipeline."
            },
            "tarefa": "Escrever um script simplificado de Terraform (`main.tf`) para provisionar o bucket S3 do projeto e validar a execução sintática no workflow.",
            "validacao": "Atividade prática avaliada qualitativamente pelo professor via análise do código Terraform submetido.",
            "exercicios": [
                "Escreva um código Terraform declarativo e enxuto que crie um Bucket S3 chamado 'indudata-backup-bucket' e que configure a criptografia em repouso dos arquivos usando a chave gerenciada do S3 (SSE-S3).",
                "O que é 'State File' (terraform.tfstate) no Terraform, por que ele é crítico e por que nunca devemos modificar ou deletar esse arquivo manualmente?"
            ]
        },
        14: {
            "title": "Observabilidade & Otimização de Custos (FinOps)",
            "icon": "📡",
            "conteudo": {
                "cd": "Análise crítica de relatórios e tomada de decisão preditiva baseada em evidências estatísticas compiladas ao longo das semanas de coleta contínua.",
                "cloud": "Estudo do pilar de Otimização de Custos do AWS Well-Architected Framework. Práticas de FinOps (gestão financeira em nuvem): acompanhamento de custos diários, identificação de instâncias ociosas (idle), redimensionamento de recursos (rightsizing) e uso de orçamentos de alerta (AWS Budgets).",
                "devops": "Introdução às arquiteturas modernas de observabilidade de microsserviços. Conceitos básicos de exportação e coleta de telemetria baseada em métricas e logs consolidados em painéis unificados usando Prometheus (coleta e alertas) e Grafana (visualização)."
            },
            "tarefa": "Revisar a arquitetura da aplicação para identificar desperdícios de custos em instâncias sobredimensionadas. Preparar o relatório final de FinOps com estimativas de custos.",
            "validacao": "Dashboard consolidado! O repositório está pronto para a entrega final de produção.",
            "exercicios": [
                "Diferencie as duas abordagens de observabilidade no monitoramento de servidores: 'Push' (envio de telemetria pela aplicação para um servidor) vs 'Pull' (o servidor faz requisições periódicas consultando as métricas da aplicação). Qual a mais comum no ecossistema do Prometheus?",
                "Você identificou em seu relatório FinOps que a instância EC2 alocada para processamento de logs opera com apenas 4% de CPU ao longo de todo o mês. Indique qual atitude prática de redução de custos (Rightsizing) você recomendaria e qual seria a economia mensal aproximada."
            ]
        },
        15: {
            "title": "Defesa Final de Produção & FinOps",
            "icon": "🎉",
            "conteudo": {
                "cd": "Defesa acadêmica final do projeto integrador. Apresentação do modelo matemático preditivo, avaliação de erros estatísticos e justificativa científica do comportamento de falha do maquinário monitorado.",
                "cloud": "Defesa de custos e relatório de FinOps consolidado. Justificativa de dimensionamento e custos de rede, banco, serverless e armazenamento para manter o sistema online.",
                "devops": "Validação de ponta a ponta: fluxo completo de deploy contínuo (Git Commit -> GitHub Actions Linter -> Tests -> Build Docker Image -> Docker Hub Push -> SSH Server Deployment) funcionando de forma integrada."
            },
            "tarefa": "Apresentar a arquitetura completa ao professor e à banca. Demonstrar a esteira rodando em tempo real com commit provocando o auto-deploy.",
            "validacao": "Parabéns! O semestre foi concluído com sucesso e o deploy está online e seguro na AWS!",
            "exercicios": [
                "Faça uma descrição detalhada de como os algoritmos de Ciência de Dados (Semanas 2, 3, 6, 8 e 11) se integraram à infraestrutura da AWS e à automação de DevOps no projeto InduData para formar um ecossistema completo de detecção de anomalias industriais.",
                "Se a sua aplicação InduData passar a receber dados de 100.000 sensores de forma concorrente, qual parte da infraestrutura AWS descrita no seu projeto seria o principal gargalo de custos e como você escalaria a arquitetura para suportar esse novo volume sem estourar o orçamento?"
            ]
        }
    }
    return semanas.get(num, {})
