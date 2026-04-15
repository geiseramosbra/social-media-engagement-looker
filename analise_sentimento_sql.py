import pandas as pd
import sqlite3

print("⏳ Analisando Sentimento vs. Engajamento...")

# 1. Carregar os dados
df = pd.read_csv('resultado_agileengine.csv')
df.columns = [c.lower() for c in df.columns]
df = df.loc[:, ~df.columns.duplicated()]

conn = sqlite3.connect(':memory:')
df.to_sql('comunicacao', conn, index=False, if_exists='replace')

# 2. QUERY: Relação Sentimento e Engajamento
# Aqui usamos CASE para deixar o resultado mais bonito se o dado for numérico
query = """
SELECT 
    platform as Plataforma,
    sentiment_score as Sentimento,
    COUNT(*) as Total_Posts,
    ROUND(AVG(engagement_rate) * 100, 2) as Engajamento_Medio_Perc
FROM 
    comunicacao
GROUP BY 
    platform, sentiment_score
ORDER BY 
    platform, Engajamento_Medio_Perc DESC
"""

try:
    df_sentimento = pd.read_sql_query(query, conn)
    print("\n💡 INSIGHT DE SENTIMENTO POR PLATAFORMA:")
    print(df_sentimento)
    
    # Salva para usarmos no Looker depois
    df_sentimento.to_csv('base_sentimento_looker.csv', index=False)
    print("\n✅ Arquivo 'base_sentimento_looker.csv' gerado!")

except Exception as e:
    print(f"❌ Erro na query: {e}")