import pandas as pd
import sqlite3

print("⏳ Iniciando análise SQL...")

# 1. Carregar os dados
df = pd.read_csv('resultado_agileengine.csv')


# transformar todos os nomes de colunas em minúsculas para não confundir o SQL
df.columns = [c.lower() for c in df.columns]

# Agora remover qualquer duplicata que tenha sobrado
df = df.loc[:, ~df.columns.duplicated()]

# 2. Conectar ao SQL
conn = sqlite3.connect(':memory:')

# 3. Enviar para o SQL (Agora os nomes estão todos padronizados em minúsculo)
df.to_sql('comunicacao', conn, index=False, if_exists='replace')

# 4. A QUERY SQL (Ajustada para os novos nomes minúsculos)
query = """
SELECT 
    platform as plataforma,
    COUNT(*) as total_posts,
    AVG(engagement_rate) as media_engajamento,
    AVG(ctr) as media_ctr,
    SUM(likes) as total_likes
FROM 
    comunicacao
GROUP BY 
    platform
ORDER BY 
    media_engajamento DESC
"""

# 5. Executar
try:
    df_sql = pd.read_sql_query(query, conn)
    print("\n📊 TABELA ANALÍTICA GERADA COM SUCESSO:")
    print(df_sql)
    
    # 6. Exportar para o Looker
    df_sql.to_csv('base_para_looker.csv', index=False)
    print("\n✅ Arquivo 'base_para_looker.csv' criado com sucesso!")

except Exception as e:
    print(f"❌ Erro na query SQL: {e}")

