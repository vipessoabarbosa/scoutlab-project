# **DOCUMENTO DE PLANEJAMENTO E GUIA DO PROJETO**

## **Tabela de Revisões**

| Data       | Versão | Descrição de Alteração                                                                 | Autor             |
|------------|--------|-----------------------------------------------------------------------------------------|-------------------|
| 2023-10-04 | 1.1    | Remoção de referências ao SofaScore, reforço do foco em análise de jogadores            | Equipe de Revisão |
| 2025-01-09 | 1.2    | Inclusão da hierarquia de dados, ajustes na arquitetura relacional e eliminação redundâncias | Equipe Scoutlab   |

---

## **1. Introdução**

A análise de dados no futebol moderno vai muito além das estatísticas de gols e assistências. Este projeto utiliza ferramentas como Python, bibliotecas especializadas (*e.g.*, `soccerdata`) e fontes confiáveis (FBref, WhoScored) para coletar, processar e analisar estatísticas avançadas, com foco no desempenho individual dos jogadores.

---

## **2. Objetivos e Escopo**

### **2.1 Objetivos Gerais**

- Desenvolver um sistema capaz de coletar e analisar estatísticas de futebol focando em métricas de jogadores.
- Criar relatórios e comparativos para subsidiar discussões sobre desempenho individual, evolução ao longo da temporada e scouting.

### **2.2 Objetivos Específicos**

- Coleta de dados: Usar `soccerdata` e scripts complementares para obter estatísticas individuais.
- Tratamento de dados: Consolidar informações em bases padronizadas.
- Criação de métricas: Implementar indicadores ofensivos, defensivos e avançados (xG, xA etc.).
- Comparações: Permitir análises entre jogadores e evolução ao longo da temporada.
- Visualizações: Gerar gráficos estáticos e interativos com foco no desempenho individual.

### **2.3 Escopo Inicial**

- Ligas alvo: Ligue 1, Premier League, Serie A, Brasileirão etc.
- Cobertura: Estatísticas exclusivamente voltadas para jogadores.
- Documentação auxiliar: Dicionário de métricas e guias explicativos.

---

## **3. Configurações e Ambiente**

Ferramentas necessárias:

1. **Linguagem**: Python 3.x
2. **Bibliotecas**: `soccerdata`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`.
3. **IDE/Editor**: Visual Studio Code
4. **Controle de versão**: Git + GitHub
5. **Ambiente virtual**: `venv` ou `conda`
6. **Armazenamento**: CSV ou SQLite (podendo evoluir para PostgreSQL)
7. **Logs**: Diretório para logs de erros/processos

---

## **4. Estrutura de Diretórios**

```
01_SCOUTLAB-PROJECT/
├─ .vscode/
│  ├─ launch.json
│  ├─ python.code-snippets
│  └─ settings.json
├─ data/
│  ├─ raw/
│  │  ├─ fbref/
│  │  └─ whoscored/
│  └─ processed/
├─ documentation/
│  ├─ config_ambiente.md
│  └─ plan_proj.md
├─ logs/
├─ notebooks/
├─ scripts/
├─ tests/
│  └─ test_setup.py
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ setup.cfg
└─ venv/  # Apesar de listada no .gitignore, a pasta pode ser mencionada para fins de organização do projeto.
```

*Observação*: Cada projeto pode personalizar conforme a necessidade, adicionando subpastas (por exemplo, `analysis/`, `visualization/`) para manter a modularização.

---

## **5. Metodologia de Desenvolvimento**

O projeto segue uma abordagem **iterativa e incremental**, dividida em etapas:

1. **Planejamento Inicial**: Definição de objetivos, escopo e métricas mínimas (documento atual).
2. **Coleta de Dados**: Implementação de scripts para baixar dados via `soccerdata`.
3. **Tratamento e Limpeza**: Normalizar colunas, remover duplicadas, corrigir valores nulos. Converter métricas para “por 90 min” quando necessário.
4. **Análise Exploratória**: Utilizar notebooks para investigar padrões, correlações e possíveis outliers.
5. **Criação de Métricas Avançadas**: Implementar indicadores como xG, xA, progressão, passes-chaves etc., **sempre com foco no atleta**.
6. **Comparações e Visualizações**: Geração de gráficos e relatórios finais, comparando jogadores e evidenciando sua evolução.
7. **Validação e Testes**: Garantir coerência dos dados.
8. **Iteração Contínua**: Ajustar configurações, refinar métricas, adicionar funcionalidade de relatórios automatizados.

---

## **6. Hierarquia de Dados e Arquitetura Relacional**

Os dados são organizados em três níveis principais:

### **6.1 Nível Temporada (Agregado)**

#### Tabelas

1. **Game Schedule** (FBref + WhoScored): calendário consolidado com IDs únicos (`season_id`, `game_id`).
2. Estatísticas agregadas:
   - *Team Season Stats* (FBref): estatísticas por equipe.
   - *Player Season Stats* (FBref): métricas por jogador.

#### Justificativa

FBref oferece dados consolidados ideais para análises sazonais.

---

### **6.2 Nível Partida (Intermediário)**

#### Tabelas

1. Estatísticas por partida:
   - *Team Match Stats* (FBref): passes, posse etc.
   - *Player Match Stats* (FBref): desempenho individual.
2. Informações contextuais:
   - *Line Ups* (FBref): escalações.
   - *Missing Players* (WhoScored): ausências por lesão/suspensão.

#### Justificativa

Combinar dados do FBref com ausências do WhoScored enriquece a análise contextual.

---

### **6.3 Nível Evento (Granular)**

#### Tabelas

1. Eventos detalhados:
   - *Events SPADL* (WhoScored): coordenadas espaciais/temporais.
   - *Shot Events* (FBref): finalizações simplificadas.

#### Justificativa

O formato SPADL do WhoScored é mais detalhado para análises táticas; o FBref serve como comparação.

---

### **6.4 Eliminação de Redundâncias e Organização do Banco de Dados**

#### Estratégias

1. Escolher:
   - Estatísticas agregadas: FBref.
   - Eventos detalhados: WhoScored.
2. Unificar:
   - Calendário consolidado (*Game Schedule*).
3. Descartar:
   - Tabelas duplicadas ou redundantes (*e.g.*, "atomic-spadl").

#### Modelo Relacional

Adotar um esquema estrela (*star schema*) com tabelas dimensionais (**Temporada**, **Equipes**, **Jogadores**) vinculadas às tabelas fato (**Partidas**, **Eventos**) via chaves primárias/estrangeiras.

---

## **7. Scripts e Notebooks**

1. **`main.py`**
   - **Função**: ponto central de execução — exibe menu interativo para escolher ligas e iniciar rotinas de coleta e análise.

2. **`data_collection.py`**
   - **Função**: coleta de dados usando `soccerdata`. Pode incluir funções para extrair de diferentes fontes (FBRef, WhoScored).
   - **Resultado**: arquivos CSV salvos em `data/raw/`.

3. **`data_processing.py`**
   - **Função**: limpeza, padronização de colunas, tratamento de valores nulos e conversão de métricas.
   - **Resultado**: dados consolidados em `data/processed/`.

4. **`analysis.py`**
   - **Função**: cálculo de métricas avançadas (xG, xA, passes-chaves, etc.) e **comparações entre jogadores**.
   - **Resultado**: DataFrames com indicadores prontos para visualização.

5. **`visualization.py`**
   - **Função**: criação de gráficos estáticos e/ou interativos (radar charts, scatter plots, heatmaps).
   - **Resultado**: figuras salvas em `reports/` ou exibidas dinamicamente.

6. **Notebooks (ex.: `Exploratory.ipynb`)**
   - **Função**: análises manuais, testes de métricas, *plot* inicial de visualizações, verificação de dados.

---

## **8. Métricas e Análises**

### **8.1 Métricas Básicas**

- Gols, Assistências, Finalizações, xG, xA
- Passes, Passes-Chave, Precisão (%)
- Desarmes, Interceptações, Duelos Aéreos
- Etc.

### **8.2 Métricas Avançadas & Compostas**

- Índice de Pressão Efetiva, Índice de Criação de Chances, Eficiência de Finalização Ajustada (EFA), entre outras.
- Métricas específicas por posição (atacantes, meio-campistas, defensores, goleiros).

### **8.3 Comparações e Rankings**

- Melhor jogador por posição baseado em percentil em métricas-chave.
- Evolução de desempenho ao longo de rodadas.
- Comparação entre 2 ou mais jogadores (ex.: radar charts).

---

## **9. Visualizações**

### **9.1 Gráficos Estáticos**

- **Scatter Plots**: correlação entre métricas (e.g., xG vs Finalizações).
- **Barras**: comparação direta de métricas básicas (e.g., gols por 90min).
- **Heatmaps**: para mostrar zonas de ação dos jogadores no campo (quando dados de evento estiverem disponíveis).

### **9.2 Gráficos Interativos**

- **Radar / Spider Charts**: comparar atributos de 2+ jogadores.
- **Dashboards**: via Plotly/Dash ou Streamlit para seleção dinâmica de jogadores, ligas e métricas.

---

## **10. Exportação e Integrações**

1. **Relatórios**
   - Exportação de relatórios em PDF ou HTML.
   - Arquivos CSV com métricas finais para uso em outras ferramentas (Power BI, Tableau).

2. **Integrações Futuras**
   - API interna para fornecer dados a sistemas de scouting ou plataformas táticas.
   - Integração com bancos de dados relacionais (PostgreSQL) para escalabilidade.

---

## **11. Validação e Testes**

- **Testes Unitários**: verificar se funções de coleta, limpeza e métricas retornam o esperado.
- **Testes de Integração**: garantir que o pipeline de coleta → processamento → análise → visualização funciona sem falhas.
- **Validação Estatística**: checar outliers, valores nulos, consistência de métricas (e.g., xG não exceder total de chutes).

---

## **12. Menu Interativo e Execução Centralizada**

O `main.py` conterá um **menu** que permitirá ao usuário:

1. Escolher liga e/ou temporada.
2. Executar coleta de dados.
3. Processar e limpar dados.
4. Gerar análises (comparações, rankings de jogadores).
5. Visualizar resultados (em janela ou exportar relatórios).

Essa estratégia minimiza a necessidade de múltiplos scripts ou parametrizações manuais nos notebooks.

---

## **13. Melhorias Futuras**

1. **Automação de Rotina**: Atualizar dados de forma periódica, integrando pipelines no GitHub Actions ou outra ferramenta de CI/CD.
2. **Dashboard Web**: Criar uma aplicação (React + Flask/Streamlit) para dar acesso público ou interno às análises de jogadores.
3. **Uso de Dados de Tracking**: Incluir coordenadas de movimentação no campo, quando disponível, para mapas de ação mais avançados.
4. **Machine Learning / Modelos Preditivos**: Futuramente, prever desempenho de jogadores ou identificar potenciais de contratação.
5. **Integração com Opcionais**: Usar TransferMarkt para dados de valor de mercado, Wyscout, InStat ou outras plataformas (quando fizer sentido para o projeto).

---

## **14. Considerações Finais**

Este documento serve como **guia base** para o desenvolvimento do projeto de Análise de Dados de Futebol, cobrindo desde a coleta e estrutura de diretórios até sugestões de métricas e visualizações. Como o objetivo principal é **analisar estatisticamente o desempenho individual de jogadores**, todo o pipeline (coleta, limpeza, análise e visualização) foi adaptado para refletir esse foco. A criação de documentações auxiliares (ex.: dicionário de métricas) ajudará a manter a clareza e o alinhamento do projeto, atendendo a diferentes níveis de desenvolvedores e analistas.
