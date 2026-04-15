# Social Media Insights: Engajamento e Sentimento com Python, SQL & Looker Studio

## O Projeto
Este repositório contém uma análise de ponta a ponta (End-to-End) de um dataset de redes sociais com 10.000 registros, integrando engenharia de dados, análise estatística e Business Intelligence.
Empresas geram volumes massivos de dados em redes sociais (Instagram, LinkedIn, Medium e YouTube), mas muitas vezes falham em correlacionar o **sentimento** do público com a **eficiência real de engajamento**. O desafio era transformar dados brutos e desestruturados em insights acionáveis para marketing estratégico.

###  Minha missão foi construir uma pipeline que pudesse:
1. Limpar e normalizar métricas de engajamento que apresentavam distorções.
2. Segmentar a performance por plataforma e polaridade de sentimento.
3. Criar um dashboard interativo que permitisse a tomada de decisão baseada em dados (Data-Driven).

### Para solucionar o problema, segui os seguintes passos técnicos:
* **ETL & Processamento (Python):** Utilizei a biblioteca **Pandas** para tratar dados duplicados, converter tipos e normalizar métricas.
* **Análise Avançada (SQL):** Implementei consultas via **SQLite** para realizar agregações complexas, calculando médias móveis e rankings de eficiência por plataforma.
* **Infraestrutura em Nuvem (Looker Studio):** Desenvolvi o dashboard conectando as bases tratadas, onde criei **campos calculados customizados** (via fórmulas de BI) para corrigir erros de agregação de porcentagem e garantir a precisão estatística de 10,05% no engajamento global.

### **R - Resultado (Result)**
* **Dashboard Executivo:** Visualização clara da liderança do Instagram em engajamento.
* **Identificação de Nichos:** Descoberta de que o Medium retém o público com sentimento mais positivo.
* **Precisão Técnica:** Correção de métricas infladas (de >1000% para os reais 10,05%), eliminando falsos positivos na análise de ROI.

## Ferramentas e Tecnologias
* **Linguagem:** Python 3.12 (Pandas, NumPy, SQLite3)
* **IDE:** VS Code (Ambiente configurado com Conda)
* **Visualização:** Looker Studio (Google Data Studio)
* **Dataset:** 10.000 registros simulando interações reais de mercado.

## Visualização do Dashboard
[![Dashboard Preview](Captura%20de%20tela%202026-04-15%20122103.png)](https://datastudio.google.com/s/nw9KvR06jTM)

## Estrutura do Repositório
* `/scripts`: Códigos Python de ETL e Análise SQL.
* `/data`: Bases de dados originais e processadas.
* `README.md`: Documentação do projeto.

---
**Desenvolvido por Geiseanne Ramos** *Especialista Data Science & AI.*
