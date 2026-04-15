import pandas as pd
import sqlite3

# 1. Carregar os dados originais (mais detalhados)
df = pd.read_csv('resultado_agileengine.csv')
df.columns = [c.lower() for c in df.columns]
df = df.loc[:, ~df.columns.duplicated()]

conn = sqlite3.connect(':memory:')
df.to_sql('comunicacao', conn, index=False, if_exists='replace')

# 2. QUERY AVANÇADA: Ranking de Eficiência
# Aqui vamos ver o ROI (Retorno sobre Investimento) de posts:
# Quem gera mais curtidas com menos esforço?
query = """
SELECT 
    platform as Plataforma,
    COUNT(*) as Total_Posts,
    SUM(likes) as Total_Likes,
    ROUND(SUM(likes) * 1.0 / COUNT(*), 2) as Curtidas_por_Post,
    ROUND(AVG(engagement_rate) * 100, 2) as Taxa_Engajamento_Perc
FROM 
    comunicacao
GROUP BY 
    platform
ORDER BY 
    Curtidas_por_Post DESC
"""

try:
    df_avancado = pd.read_sql_query(query, conn)
    print("\n🔍 ANÁLISE DE EFICIÊNCIA DE CONTEÚDO:")
    print(df_avancado)
    
    # Vamos salvar essa visão mais rica para o Looker
    df_avancado.to_csv('base_avancada_looker.csv', index=False)
    print("\n✅ Nova base 'base_avancada_looker.csv' gerada!")

except Exception as e:
    print(f"❌ Erro na query: {e}")