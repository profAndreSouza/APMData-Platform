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
            "icon": "fa-solid fa-screwdriver-wrench",
            "conteudo": {
                "cd": "Apresentação da telemetria de sensores industriais e classificação de dados. Estudamos os níveis de mensuração: **Nominal** (rótulos categóricos como ID do motor $M_i$), **Ordinal** (criticidade de alertas: Leve, Médio, Grave), **Intervalar** (temperatura em °C com ponto zero arbitrário) e **Razão** (dados de tempo com zero absoluto, como latência em milissegundos $t \\ge 0$ e vibração mecânica em Hertz).",
                "cloud": "Fundamentos da nuvem AWS. Estudo de modelos de serviço (IaaS, PaaS, SaaS) e economia de escala. Introdução ao faturamento na AWS por meio do princípio 'Pay-as-you-go' (pagamento pelo uso efetivo), Free Tier e utilização prática da calculadora AWS Pricing Calculator para simulação de projetos.",
                "devops": "Cultura DevOps baseada nos pilares de colaboração, automação e monitoramento contínuo. Introdução ao Git como base para controle de versão, conceitos de commits atômicos e inicialização do repositório local de sensores."
            },
            "tarefa": "Realizar o fork do repositório, clonar localmente e configurar o ambiente virtual do Python (pip install -r requirements.txt).",
            "validacao": "Semana de Setup. Nenhuma função de código estatístico é validada nesta semana.",
            "exercicios": [
                "Classifique as seguintes variáveis coletadas de um motor nas quatro escalas de medição (Nominal, Ordinal, Intervalar e Razão):\n\na) Status de Operação: [Ligado, Desligado, Em Manutenção]\nb) Índice de Vibração de Mancal: [45.2 Hz, 47.1 Hz, 120.4 Hz]\nc) Criticidade de Falha do Sistema: [Urgente, Alta, Média, Baixa]\nd) Temperatura do Rolamento: [310 K, 315 K, 320 K]\n\nJustifique detalhadamente a classificação de cada uma.",
                "Acesse o AWS Pricing Calculator e estime o custo mensal para armazenar e transferir os seguintes volumes de logs de motores:\n\n- Armazenamento S3 Standard: 150 GB de dados brutos\n- Transferência de Dados (Saída): 50 GB trafegados para a internet pública\n- Operações de Gravação: 1.000 requisições PUT diárias\n- Operações de Leitura: 5.000 requisições GET diárias"
            ]
        },
        2: {
            "title": "Tendência Central & Segurança (IAM)",
            "icon": "fa-solid fa-ruler-horizontal",
            "conteudo": {
                "cd": "Estatística Descritiva focada em Medidas de Tendência Central. Estudo da **Média Aritmética**:\n$$\\bar{x} = \\frac{1}{n} \\sum_{i=1}^{n} x_i$$\nEstudo da **Mediana** ($P_{50}$), que divide o conjunto de dados ordenados ao meio:\n$$\\text{Mediana} = \\begin{cases} x_{(n+1)/2} & \\text{se } n \\text{ for ímpar} \\\\ \\frac{x_{(n/2)} + x_{(n/2 + 1)}}{2} & \\text{se } n \\text{ for par} \\end{cases}$$\nE a **Moda** (valores com maior frequência absoluta, indicando falhas cíclicas comuns em motores).",
                "cloud": "Infraestrutura global da AWS dividida em Regiões geográficas e Zonas de Disponibilidade (AZs) redundantes e isoladas. Segurança de dados na nuvem através do AWS IAM (Identity and Access Management), configurando políticas em formato JSON baseadas no Princípio do Menor Privilégio, grupos de acesso e papéis de execução (Roles).",
                "devops": "Colaboração e versionamento no Git utilizando branching strategies (Git Flow). Conceito de Pull Requests (PRs), code review sistemático para validação de algoritmos e práticas de escrita de commits semânticos (Conventional Commits)."
            },
            "tarefa": "Implementar as funções `calcular_media` e `calcular_mediana` no arquivo `app/core/stats.py` sem usar funções de agregação prontas (ex: `sum()` ou `statistics.median()`).",
            "validacao": "Validado executando a média e mediana amostral sobre dados simulados.",
            "exercicios": [
                "Considere as seguintes medições de latência de leitura (em ms) de um sensor industrial:\n\nLatências = [12, 15, 14, 12, 18, 900, 11]\n\na) Calcule manualmente a Média Aritmética e a Mediana deste conjunto.\nb) Se o sensor apresentar um pico anômalo de 900ms devido a um ruído temporário na rede, explique qual das duas medidas descreve melhor a latência típica de operação do sistema e por quê.",
                "Crie uma política IAM de segurança em formato JSON que atenda ao Princípio do Menor Privilégio para a aplicação InduData, com as seguintes permissões:\n\n- Permitir listagem de arquivos e leitura de objetos apenas no bucket 'indudata-sensor-logs'\n- Bloquear explicitamente qualquer ação de exclusão (DeleteObject) neste bucket"
            ]
        },
        3: {
            "title": "Variabilidade & Computação Elástica (EC2)",
            "icon": "fa-solid fa-chart-simple",
            "conteudo": {
                "cd": "Quantificação do Jitter (oscilação e ruído físico de vibração nos mancais) via medidas de variabilidade. Estudo da **Amplitude (R)**:\n$$R = x_{\\text{max}} - x_{\\text{min}}$$\nDa **Variância Amostral ($s^2$)** com divisor $n-1$ para corrigir o viés amostral:\n$$s^2 = \\frac{1}{n-1} \\sum_{i=1}^{n} (x_i - \\bar{x})^2$$\nE do **Desvio Padrão ($s$)** como desvio médio quadrático na escala original da grandeza:\n$$s = \\sqrt{s^2}$$",
                "cloud": "Computação elástica na nuvem por meio do Amazon EC2 (Elastic Compute Cloud). Conceitos de virtualização e dimensionamento de hardware virtual. Diferenciação operacional e de custos entre os modelos de contratação de instâncias: sob demanda (On-Demand), instâncias reservadas de longo prazo (Reserved Instances) e instâncias com desconto de capacidade sobressalente (Spot Instances).",
                "devops": "Virtualização por container com Docker. Filosofia de empacotamento isolado (isolamento de processos, rede e sistemas de arquivos). Escrita de um Dockerfile otimizado em múltiplas camadas (multi-stage builds) para reduzir a superfície de ataque e o tamanho da imagem da aplicação."
            },
            "tarefa": "Implementar as funções `calcular_variancia`, `calcular_desvio_padrao` e `calcular_amplitude` em `app/core/stats.py`. Dockerizar a aplicação Flask do APM.",
            "validacao": "Validado executando variância amostral com divisor N-1 e amplitude.",
            "exercicios": [
                "Você coletou duas amostras de vibração mecânica (em Hz) de dois motores idênticos operando na fábrica:\n\nMotor A = [58, 60, 61, 59, 62]\nMotor B = [40, 75, 45, 80, 60]\n\na) Calcule a Amplitude (R), a Variância Amostral (s²) e o Desvio Padrão (s) de cada motor.\nb) Sabendo que oscilações extremas reduzem drasticamente a vida útil dos mancais de rolamento, qual motor apresenta indícios visíveis de instabilidade mecânica?",
                "Projete um Dockerfile otimizado de produção para rodar a aplicação Python Flask exposta na porta 5000, atendendo aos seguintes critérios de segurança:\n\n- Utilizar uma imagem base leve (alpine ou slim)\n- Configurar um usuário 'guest' com permissões não-root\n- Garantir que o container não grave bytecodes do Python (PYTHONDONTWRITEBYTECODE)"
            ]
        },
        4: {
            "title": "Amostragem & Topologia de Redes (VPC)",
            "icon": "fa-solid fa-shuffle",
            "conteudo": {
                "cd": "Métodos de amostragem probabilística para reduzir o custo computacional de processamento de logs industriais. **Amostragem Aleatória Simples** (seleção equiprovável), **Amostragem Sistemática** (seleção sistemática a cada passo constante $k = N/n$) e **Amostragem Estratificada** (divisão proporcional da população de telemetria baseada em estratos homogêneos, como por ID de motor $M_i$).",
                "cloud": "Criação de redes isoladas e virtuais na nuvem através do Amazon VPC (Virtual Private Cloud). Arquitetura de subredes públicas (para servidores web) e subredes privadas (para bancos de dados), tabelas de rotas, controle de acessos com Security Groups e custos agregados a Data Transfer de dados entre zonas e internet pública.",
                "devops": "Orquestração de múltiplos containers locais usando o Docker Compose. Configuração de volumes persistentes para que os dados do banco de dados não sejam perdidos no reinício do container e mapeamento de redes internas isoladas."
            },
            "tarefa": "Implementar as funções de `amostragem_sistematica` e `amostragem_estratificada` em `app/core/sampling.py` para reduzir a base de análise do APM.",
            "validacao": "Validado executando amostragem sistemática de passo k=N/n.",
            "exercicios": [
                "Considere uma população de logs de latência com N=12 itens registrados sequencialmente:\n\nLogs = [15, 22, 18, 30, 25, 40, 35, 50, 42, 60, 55, 70]\n\na) Utilize a amostragem sistemática com passo k=3 e ponto de partida i=1 (segundo item, índice 1) para extrair uma amostra de tamanho n=4.\nb) Demonstre passo a passo quais valores foram selecionados para compor o conjunto final.",
                "Imagine que você configurou uma arquitetura na AWS onde um servidor EC2 envia 5 TB de dados mensais para a internet pública e recebe 1 TB de dados de sensores. Sabendo que a AWS cobra $0.09 por GB para transferência de saída (Data Transfer Out) e $0.00 para entrada (Data Transfer In), calcule o custo total de rede dessa arquitetura."
            ]
        },
        5: {
            "title": "Visualização & Armazenamento de Objetos (S3)",
            "icon": "fa-solid fa-chart-pie",
            "conteudo": {
                "cd": "Comunicação visual e exploração de dados. Plotagem de gráficos temporais para acompanhamento de tendências, diagramas de dispersão para correlação, histogramas e **Boxplots** baseados na regra do intervalo interquartílico:\n$$\\text{IQR} = Q_3 - Q_1$$\nOnde valores fora de $[Q_1 - 1.5\\text{IQR}, Q_3 + 1.5\\text{IQR}]$ são classificados como outliers (picos térmicos anômalos).",
                "cloud": "Armazenamento de logs e telemetria industrial em larga escala com o Amazon S3 (Simple Storage Service). Mapeamento de classes de armazenamento (S3 Standard para análise imediata, S3 Infrequent Access para buscas eventuais e S3 Glacier para conformidade histórica barata) e definição automatizada de regras de ciclo de vida (S3 Lifecycle Policies).",
                "devops": "Integração Contínua (CI) automatizada. Configuração de esteira no GitHub Actions por meio de arquivos YAML. Automação de linters e formatação automática de código (ex: Black e Flake8) para manter a qualidade de código do repositório."
            },
            "tarefa": "Concluir os gráficos de telemetria do Dashboard e ativar a esteira de CI com Linter (Black/Flake8) disparando no git push.",
            "validacao": "Dashboard estruturado! Certifique-se de que a automação do GitHub Actions (.github/workflows/ci.yml) está rodando sem erros no GitHub.",
            "exercicios": [
                "Considere o seguinte conjunto de leituras de temperatura de um motor:\n\nTemperatura = [45, 48, 50, 52, 95, 47, 49, 51] °C\n\na) Desenhe conceitualmente um Boxplot deste conjunto identificando a Mediana (Q2) e a presença de outliers.\nb) Explique qual o limite superior do boxplot utilizando a regra do Intervalo Interquartílico (IQR) multiplicada por 1.5.",
                "Uma mineradora gera 100 GB diários de logs brutos que são analisados em tempo real nos primeiros 30 dias. Por razões de conformidade, esses arquivos devem permanecer salvos por mais 365 dias (sendo consultados no máximo uma vez ao ano) e depois excluídos de forma permanente. Projete a regra de ciclo de vida do S3 ideal para economizar o máximo de orçamento na AWS."
            ]
        },
        6: {
            "title": "Normalidade & Bancos Gerenciados (RDS)",
            "icon": "fa-solid fa-chart-line",
            "conteudo": {
                "cd": "Inferência estatística e testes de hipóteses no APM. Teste de **Shapiro-Wilk** para avaliar a aderência dos dados de sensores à Distribuição Normal (Gaussiana):\n$$W = \\frac{\\left(\\sum_{i=1}^{n} a_i x_{(i)}\\right)^2}{\\sum_{i=1}^{n} (x_i - \\bar{x})^2}$$\nEstabelecemos Hipótese Nula ($H_0$: dados são normais) com significância $\\alpha = 0.05$. Se o $p\\text{-valor} < 0.05$, rejeita-se a normalidade, indicando anormalidades ou fadiga mecânica persistente.",
                "cloud": "Hospedagem de bancos de dados relacionais gerenciados com o Amazon RDS (Relational Database Service) PostgreSQL. Arquiteturas de alta disponibilidade e failover multi-AZ. Comparativo conceitual, operacional e administrativo: rodar PostgreSQL em máquinas EC2 autogerenciadas (IaaS) vs delegar backups e replicação ao RDS (PaaS).",
                "devops": "Automação de testes de regressão. Integração de testes automatizados unitários (`pytest`) na esteira de CI, forçando a falha da build e impedindo deploy caso alguma alteração quebre os cálculos estatísticos fundamentais."
            },
            "tarefa": "Implementar `teste_shapiro_wilk` em `app/core/hypothesis.py`. Conectar a aplicação ao banco de dados Amazon RDS PostgreSQL provisionado.",
            "validacao": "Validado testando a hipótese de normalidade da latência usando o teste estatístico Shapiro-Wilk.",
            "exercicios": [
                "Você realizou a análise de normalidade da temperatura de um motor industrial obtendo os seguintes valores de teste:\n\nW = 0.985\np-valor = 0.012\n\na) Considerando um nível de significância alpha = 0.05, você aceita ou rejeita a hipótese nula (H0) de normalidade?\nb) Se a distribuição da temperatura for considerada não-normal, o que isso pode indicar do ponto de vista de oscilações mecânicas da máquina?",
                "Considere o seguinte dilema corporativo: provisionar um banco PostgreSQL no RDS custa $50/mês e realiza backup automatizado por padrão. Provisioná-lo no EC2 custa $30/mês, mas exige que a equipe gaste 2 horas semanais gerenciando backups e atualizações. Sabendo que o custo da hora do engenheiro da equipe é de $25, monte uma planilha conceitual e justifique a melhor decisão econômica para a fábrica."
            ]
        },
        7: {
            "title": "Associação Categórica & SDK Boto3",
            "icon": "fa-solid fa-table-cells-large",
            "conteudo": {
                "cd": "Estudo de associação qualitativa de falhas. Teste de **Qui-Quadrado ($\\chi^2$) de Independência** baseado na comparação entre frequências observadas ($O_i$) e esperadas ($E_i$) em tabelas de contingência cruzando turnos de trabalho e falhas:\n$$\\chi^2 = \\sum_{i=1}^{k} \\frac{(O_i - E_i)^2}{E_i}$$\nMedimos se o turno de trabalho afeta significativamente a taxa de falhas das máquinas.",
                "cloud": "Integração programática e desenvolvimento em nuvem utilizando o SDK oficial da AWS para Python (Boto3). Configuração de credenciais locais de desenvolvimento, instanciação de recursos S3 no script, gravação de dados em formato JSON em tempo real e tratamento de exceções de conexão.",
                "devops": "Gerenciamento de repositórios de imagens de container. Registro e publicação automática da imagem compilada da aplicação no Docker Hub via workflows do GitHub Actions utilizando GitHub Secrets para gerenciar tokens e credenciais seguras."
            },
            "tarefa": "Implementar `teste_qui_quadrado_associacao` em `app/core/hypothesis.py`. Adicionar código no pipeline para gerar a tag da imagem Docker e enviar ao Docker Hub.",
            "validacao": "Validado rodando o teste qui-quadrado de independência sobre tabelas de contingência de endpoints.",
            "exercicios": [
                "Analise a seguinte tabela de contingência contendo a quantidade de falhas mecânicas cruzadas por turno de trabalho:\n\n- Turno Diurno: 10 Falhas | 90 Normais\n- Turno Noturno: 35 Falhas | 65 Normais\n\na) Utilize a sua função `teste_qui_quadrado_associacao` para calcular a estatística Qui-Quadrado e o p-valor correspondente.\nb) Explique qual a conclusão estatística obtida e o que ela representa para a gerência da fábrica.",
                "Escreva um trecho de código em Python usando a biblioteca Boto3 para carregar o arquivo local 'sensores.csv' para o bucket S3 'indudata-sensor-logs', definindo um tratamento de exceções (try/except) completo para possíveis erros de conexão."
            ]
        },
        8: {
            "title": "Correlação & Monitoramento (CloudWatch)",
            "icon": "fa-solid fa-link",
            "conteudo": {
                "cd": "Quantificação do relacionamento linear entre variáveis quantitativas com o **Coeficiente de Correlação de Pearson ($r$)**:\n$$r = \\frac{\\sum_{i=1}^{n} (x_i - \\bar{x})(y_i - \\bar{y})}{\\sqrt{\\sum_{i=1}^{n} (x_i - \\bar{x})^2 \\sum_{i=1}^{n} (y_i - \\bar{y})^2}}$$\nInterpretação do coeficiente linear variando em $[-1, 1]$ para mensurar a relação de temperatura vs RPM e nível de óleo do motor.",
                "cloud": "Monitoramento centralizado e logs com Amazon CloudWatch. Criação de métricas de performance operacionais personalizadas (ex: latências de sensores). Configuração de alarmes de custos e limites técnicos e análise da precificação baseada no tráfego de ingestão de logs do sistema.",
                "devops": "Entrega Contínua (CD) clássica para ambientes IaaS (EC2). Escrita de scripts de shell com conexões SSH automatizadas via GitHub Actions para realizar pull da imagem Docker atualizada no Docker Hub e reiniciar o container na produção."
            },
            "tarefa": "Implementar `calcular_correlacao_pearson` em `app/core/time_series.py`. Integrar o script de deploy automatizado por SSH na pipeline do GitHub Actions.",
            "validacao": "Validado rodando o cálculo de Pearson entre requisições de entrada e uso de CPU.",
            "exercicios": [
                "Você calculou a correlação de Pearson entre o Uso de CPU (%) e a Temperatura Interna (C) do servidor industrial a partir de 5 registros:\n\nCPU (X) = [10, 20, 30, 40, 50]\nTemperatura (Y) = [12, 22, 44, 61, 85]\n\na) Obtenha o coeficiente de Pearson (r) para estas séries.\nb) Se o coeficiente de correlação for r = 0.992, o que podemos concluir em relação à associação entre o processamento do servidor e o calor gerado?",
                "Projete um script em Bash (shell script) que conecte em uma instância EC2 (IP público 54.12.34.56) via chave SSH, faça o download da última imagem Docker do repositório 'indudata-app:latest', pare o container rodando atualmente e inicie a nova versão na porta 5000."
            ]
        },
        9: {
            "title": "Sazonalidade & Computação Serverless (Lambda)",
            "icon": "fa-solid fa-hourglass-half",
            "conteudo": {
                "cd": "Modelagem estatística em Séries Temporais. Componentes de dados organizados no tempo: Tendência ($T_t$), Sazonalidade ($S_t$) e o Ruído/Irregularidade ($I_t$). Comportamento periódico diário e sazonal de tráfego de requisições de sensores na nuvem.",
                "cloud": "Arquiteturas Serverless orientadas a eventos. Provisionamento computacional sem gerência de servidores com o AWS Lambda e exposição de endpoints HTTP redundantes com o Amazon API Gateway. Mapeamento de cobrança por memória e tempo de execução contra manter instâncias de computação dedicada ligadas 24/7.",
                "devops": "Deploy Serverless automatizado. Escrita de workflows GitHub Actions voltados para o empacotamento, empacotamento em zip e upload automatizado do código Python para funções AWS Lambda utilizando ferramentas de linha de comando CLI."
            },
            "tarefa": "Desenvolver uma função simples em Python para rodar como Lambda na AWS. Estimar o custo de rodar essa função comparado a manter uma instância EC2 rodando direto.",
            "validacao": "Atividade validada por meio de entrega dos relatórios de custos e códigos Serverless no repositório.",
            "exercicios": [
                "Identifique qual dos três componentes de Séries Temporais (Tendência, Sazonalidade ou Ruído) está associado a cada comportamento operacional:\n\na) O desgaste progressivo das escovas de um motor de indução ao longo de 6 meses.\nb) O pico de energia consumido pela planta de refrigeração todos os dias ao meio-dia.\nc) A oscilação instantânea da tensão da rede elétrica devido a um raio na região.",
                "Calcule o custo mensal estimado de processar dados em nuvem utilizando AWS Lambda para a seguinte carga de trabalho:\n\n- Número de Execuções: 10 milhões de requisições por mês\n- Tempo Médio de Execução: 200 ms por chamada\n- Memória Alocada na Função: 512 MB\n\nConsidere que a AWS cobra $0.0000008333 por GB-segundo executado."
            ]
        },
        10: {
            "title": "Decomposição & Filas Assíncronas (SQS/SNS)",
            "icon": "fa-solid fa-wave-square",
            "conteudo": {
                "cd": "Decomposição aditiva clássica de Séries Temporais:\n$$Y_t = T_t + S_t + I_t$$\nAplicação de técnicas de suavização de médias móveis para isolar e remover ruídos rápidos da telemetria ($I_t$) de modo a evidenciar desvios crônicos de temperatura ou vibração no longo prazo.",
                "cloud": "Arquiteturas de mensageria assíncronas e desacopladas para comunicação entre microsserviços. Utilização do Amazon SQS (Simple Queue Service) para buffers de mensagens resilientes (comparativo FIFO vs Standard) e Amazon SNS (Simple Notification Service) para disparo automático de e-mails/SMS de falha mecânica.",
                "devops": "Observabilidade e centralização de registros de container. Configuração dos drivers de log nativos do Docker (Docker Log Drivers) para encaminhar automaticamente a saída padrão de execução do container Flask para o CloudWatch Logs da AWS."
            },
            "tarefa": "Implementar a função `decompor_serie_temporal` em `app/core/time_series.py`. Integrar alertas automatizados por e-mail com Amazon SNS.",
            "validacao": "Validado rodando decomposição aditiva de uso de CPU com sazonalidade.",
            "exercicios": [
                "Você realizou a decomposição aditiva da temperatura de um motor industrial ao longo de 24 horas (período=6) e obteve a série decomposta:\n\nObservado em t=12: 55°C | Tendência em t=12: 45°C | Sazonalidade em t=12: 8°C\n\na) Calcule manualmente o valor correspondente ao componente de Ruído (Irregularidade) em t=12.\nb) O que esse valor indica em relação ao comportamento anômalo da máquina?",
                "Estime o custo mensal da infraestrutura de filas na AWS sabendo que:\n\n- A fábrica envia 20 milhões de mensagens mensais ao AWS SQS FIFO\n- Cada mensagem tem tamanho médio de 128 KB\n- O AWS SQS FIFO cobra $0.50 por milhão de requisições enviadas"
            ]
        },
        11: {
            "title": "Capacity Planning & Containers Serverless (ECS Fargate)",
            "icon": "fa-solid fa-magnifying-glass-chart",
            "conteudo": {
                "cd": "Capacity Planning estatístico utilizando Regressão Linear Simples por Mínimos Quadrados ($y = ax + b$). Cálculo dos coeficientes angular ($a$) e linear ($b$):\n$$a = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sum (x_i - \\bar{x})^2}$$\n$$b = \\bar{y} - a\\bar{x}$$\nProjeção de quando a memória RAM do servidor ou disco atingirá o limite crítico.",
                "cloud": "Alta disponibilidade e balanceamento de carga com Amazon ELB (Elastic Load Balancing) e grupos de autoescalonamento (Auto Scaling Groups). Implantação e orquestração de containers sob demanda no Amazon ECS Fargate sem necessidade de gerenciar o cluster EC2 subjacente.",
                "devops": "Deploy de containers em serviços serverless em nuvem. Configuração e automação do processo de implantação contínua para hospedar o container Flask no AWS App Runner ou AWS ECS Fargate, configurando regras de roteamento."
            },
            "tarefa": "Implementar `ajuste_regressao_linear` em `app/core/time_series.py`. Rodar o deploy automatizado da aplicação para um serviço gerenciado escalável (App Runner/ECS).",
            "validacao": "Validado computando inclinação (a) e intercepto (b) da reta de tendência de RAM.",
            "exercicios": [
                "Considere os seguintes registros de tempo (t em horas) e uso de memória RAM (%) coletados de um servidor:\n\nt = [1, 2, 3, 4, 5]\nRAM = [30, 35, 41, 47, 52]\n\na) Ajuste a equação de regressão linear (y = a*x + b) para estes dados.\nb) Estime após quantas horas de operação contínua o servidor sofrerá um travamento por falta de memória (RAM >= 100%).",
                "Considere que um container Flask roda no ECS Fargate consumindo 0.5 vCPU e 1 GB de RAM. A AWS cobra:\n\n- vCPU por hora: $0.04048\n- RAM por hora: $0.004445\n\nCalcule o custo mensal para manter este container rodando ininterruptamente 24 horas por dia durante 30 dias."
            ]
        },
        12: {
            "title": "Métricas & Gestão de Segredos (Secrets Manager)",
            "icon": "fa-solid fa-key",
            "conteudo": {
                "cd": "Métricas de validação de modelos de regressão de sensores. Erro Médio Absoluto (MAE) e Raiz do Erro Quadrático Médio (RMSE):\n$$\\text{MAE} = \\frac{1}{n} \\sum_{i=1}^{n} |y_i - \\hat{y}_i|$$\n$$\\text{RMSE} = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2}$$\nComparação de confiabilidade entre modelos matemáticos preditivos em ambientes de manutenção.",
                "cloud": "Criptografia de dados com chaves gerenciadas no AWS KMS (Key Management Service). Segurança de segredos de aplicação, senhas de banco RDS e tokens através do AWS Secrets Manager com rotação automatizada integrada no ciclo de deploy.",
                "devops": "Configuração de conexões seguras sem chaves estáticas. Autenticação baseada em OIDC (OpenID Connect) para que o GitHub Actions se comunique com a AWS gerando tokens temporários seguros, eliminando credenciais de longo prazo."
            },
            "tarefa": "Configurar o AWS Secrets Manager para gerenciar a senha do RDS. Integrar a leitura do segredo na aplicação utilizando o Boto3.",
            "validacao": "Segurança e segredos integrados! Valide o fluxo de credenciais seguras no pipeline de deploy.",
            "exercicios": [
                "Você projetou dois modelos estatísticos diferentes para prever a temperatura de motores com base nas leituras dos sensores e obteve os seguintes erros em relação aos dados reais:\n\nModelo A: MAE = 1.8°C | RMSE = 4.2°C\nModelo B: MAE = 2.0°C | RMSE = 2.2°C\n\na) Justifique qual dos dois modelos apresenta erros de previsão mais homogêneos (menos sensíveis a picos/outliers).\nb) Qual modelo você selecionaria para implantação em produção?",
                "O AWS Secrets Manager cobra $0.40 por segredo ativo por mês e $0.05 a cada 10.000 requisições de leitura. Calcule o custo de armazenar a senha do RDS sabendo que o backend da InduData faz a consulta deste segredo a cada inicialização (estimado em 50 vezes por dia) ao longo de 30 dias."
            ]
        },
        13: {
            "title": "Dashboard Final & Infraestrutura como Código (IaC)",
            "icon": "fa-solid fa-trowel-bricks",
            "conteudo": {
                "cd": "Consolidação e visualização integrada do painel preditivo. Arquitetura de dados para alimentar o dashboard final e plotagem de relatórios integrados.",
                "cloud": "Fundamentos teóricos de Infraestrutura como Código (IaC) na nuvem. Mapeamento de recursos declarativos de rede e computação AWS de forma automatizada e idempotente utilizando scripts baseados na sintaxe HCL do Terraform.",
                "devops": "Escrita e provisionamento de infraestrutura usando Terraform. Configuração de arquivos declarativos HCL (`main.tf`, `variables.tf`) para provisionar de forma reprodutível instâncias EC2, buckets S3 e redes VPC no pipeline."
            },
            "tarefa": "Escrever um script simplificado de Terraform (`main.tf`) para provisionar o bucket S3 do projeto e validar a execução sintática no workflow.",
            "validacao": "Atividade prática avaliada qualitativamente pelo professor via análise do código Terraform submetido.",
            "exercicios": [
                "Escreva a sintaxe HCL em Terraform (`main.tf`) correspondente para criar um Bucket S3 da AWS chamado 'indudata-deploy-archive' e configure regras para bloquear todo o acesso público de gravação de arquivos por padrão.",
                "No arquivo de estado local do Terraform (terraform.tfstate), são mantidas credenciais importantes e dados lidos da AWS. Explique qual a forma mais segura de gerenciar este arquivo em ambientes de produção com equipes e os riscos de expô-lo no repositório público do GitHub."
            ]
        },
        14: {
            "title": "Observabilidade & Otimização de Custos (FinOps)",
            "icon": "fa-solid fa-scale-balanced",
            "conteudo": {
                "cd": "Análise crítica de relatórios e tomada de decisão preditiva baseada em evidências estatísticas compiladas ao longo das semanas de coleta contínua.",
                "cloud": "Estudo aprofundado do AWS Well-Architected Framework com ênfase no pilar de Cost Optimization (Otimização de Custos). Boas práticas operacionais do modelo FinOps para monitoramento e redimensionamento de recursos computacionais ociosos (Rightsizing).",
                "devops": "Introdução às arquiteturas modernas de observabilidade de microsserviços. Conceitos básicos de exportação e coleta de telemetria baseada em métricas e logs consolidados em painéis unificados usando Prometheus (coleta e alertas) e Grafana (visualização)."
            },
            "tarefa": "Revisar a arquitetura da aplicação para identificar desperdícios de custos em instâncias sobredimensionadas. Preparar o relatório final de FinOps com estimativas de custos.",
            "validacao": "Dashboard consolidado! O repositório está pronto para a entrega final de produção.",
            "exercicios": [
                "Explique teoricamente por que o Rightsizing de instâncias EC2 (redimensionamento de recursos baseado em CPU/RAM ociosos) é um pilar crucial na cultura de FinOps em nuvem.",
                "Se a sua aplicação está rodando sob um container Docker em uma instância EC2 m5.xlarge que custa $136/mês, e a telemetria mostra que o uso médio de CPU não excede 5% e o de RAM não passa de 15%, qual o tipo de instância ideal para a qual você migraria para economizar e qual seria a redução de custo em porcentagem?"
            ]
        },
        15: {
            "title": "Defesa Final de Produção & FinOps",
            "icon": "fa-solid fa-trophy",
            "conteudo": {
                "cd": "Defesa acadêmica final do projeto integrador. Apresentação do modelo matemático final à banca.",
                "cloud": "Análise e defesa da infraestrutura final de produção do projeto integrador InduData, mapeando os requisitos de computação, banco relacional gerenciado RDS, segurança de redes (VPC) e dimensionamento de custos FinOps na nuvem AWS.",
                "devops": "Validação de ponta a ponta: fluxo completo de deploy contínuo (Git Commit -> GitHub Actions Linter -> Tests -> Build Docker Image -> Docker Hub Push -> SSH Server Deployment) funcionando de forma integrada."
            },
            "tarefa": "Apresentar a arquitetura completa ao professor e à banca. Demonstrar a esteira rodando em tempo real com commit provocando o auto-deploy.",
            "validacao": "Parabéns! O semestre foi concluído com sucesso e o deploy está online e seguro na AWS!",
            "exercicios": [
                "Projete uma arquitetura conceitual em bloco de manutenção preditiva industrial unindo os seguintes elementos que você desenvolveu no curso:\n\n- Coleta de dados com APIs\n- Filas SQS FIFO e Processamento\n- Banco RDS PostgreSQL\n- Alertas SNS por e-mail\n- Modelagem no Dashboard\n\nDescreva como as informações fluem de ponta a ponta.",
                "Calcule o custo mensal total estimado para hospedar a plataforma InduData em produção na AWS com a seguinte carga de recursos:\n\n- 2 instâncias t3.small no ECS Fargate ($15/mês cada)\n- 1 banco de dados RDS PostgreSQL db.t3.micro ($20/mês)\n- Armazenamento S3 e tráfego de saída estimado em 200 GB ($18/mês)\n- Chamadas extras de monitoramento no CloudWatch ($7/mês)"
            ]
        }
    }
    return semanas.get(num, {})
