# Sistema de Observabilidade com OpenTelemetry

## Por que devemos observar?

No desenvolvimento de software moderno, sistemas são cada vez mais distribuídos, complexos e dinâmicos. Containers, microsserviços e APIs se comunicam constantemente, criando cenários onde:

- **Problemas não são óbvios**: uma lentidão pode vir de um serviço que você nem sabia que existia
- **Erros são esporádicos**: falhas que acontecem de vez em quando são difíceis de reproduzir
- **Impacto é invisível**: você só descobre que algo quebrou quando o usuário reclama

**Observar não é opcional. É necessidade.**

Sem observabilidade, você está dirigindo um carro sem painel. Pode até funcionar por um tempo, mas quando algo falhar, você não terá ideia do que aconteceu, onde foi ou como consertar.

## Introdução à Observabilidade

Observabilidade é a capacidade de entender o estado interno de um sistema apenas observando seus dados externos. Em outras palavras, é conseguir responder perguntas como:

| Pergunta | O que você precisa |
|----------|---------------------|
| "O sistema está vivo?" | Métricas de saúde |
| "Por que está lento?" | Traces para ver o caminho da requisição |
| "O que causou o erro?" | Logs com detalhes do evento |



Sem observabilidade, você está dirigindo um carro sem painel. Pode até funcionar por um tempo, mas quando algo falhar, você não terá ideia do que aconteceu, onde foi ou como consertar.



### Os Três Pilares

MÉTRICAS ────► O QUE aconteceu?
Exemplo: CPU em 95%, 500 erros por segundo

LOGS ────────► O QUE aconteceu em detalhe?
Exemplo: "Falha de conexão com banco na linha 42"

TRACES ──────► ONDE aconteceu no fluxo?
Exemplo: API → Auth → Banco (2s aqui!) → Cache


## O que este projeto oferece

Uma stack completa e pronta para uso de observabilidade baseada no ecossistema Grafana e OpenTelemetry, integrando métricas, logs e traces em uma única plataforma.

## Componentes

| Componente | Função |
|------------|--------|
| **Gateway** | Ponto de entrada das requisições |
| **APP** | Aplicação com lógica de negócio |
| **Collector Otel** | Coleta e distribui os sinais |
| **Tempo** | Armazena traces |
| **Loki** | Armazena logs |
| **Mimir** | Armazena métricas |
| **Grafana** | Visualização unificada |

## Fluxo de Dados

1. Usuário acessa o sistema através do Gateway
2. Gateway encaminha requisições para a APP
3. APP executa a lógica de negócio e emite sinais via OTLP
4. Collector Otel recebe os sinais e distribui para os backends
5. Grafana consulta os backends e exibe as informações



## Como Testar
# Rolar dado 10 vezes
for i in {1..10}; do curl http://localhost:5000/; echo ""; sleep 1; done

# Health check 5 vezes
for i in {1..5}; do curl http://localhost:5000/health; echo ""; sleep 1; done

# Endpoint de erro 3 vezes
for i in {1..3}; do curl http://localhost:5000/fail; echo ""; sleep 1; done

## Como subir

```bash
docker-compose up -d