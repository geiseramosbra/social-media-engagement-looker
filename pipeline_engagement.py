import pandas as pd
import glob

print("⏳ Iniciando processamento...")

# Procurar qualquer arquivo que termine com .csv na pasta
arquivos = glob.glob("*.csv")

if not arquivos:
    print("❌ Erro: Não encontrei o arquivo CSV. Verifique se ele está na mesma pasta que este script!")
    exit()

# Pega o primeiro CSV que encontrar
df = pd.read_csv(arquivos[0])
print(f"✅ Analisando o arquivo: {arquivos[0]}")

# Cálculos de Engajamento para a vaga
df['Engagement_Rate'] = (df.get('Likes', 0) + df.get('Comments', 0) + df.get('Shares', 0)) / df.get('Impressions', 1)
df['CTR'] = df.get('Clicks', 0) / df.get('Impressions', 1)

# Salva o resultado final
df.to_csv('resultado_agileengine.csv', index=False)

print("\n" + "="*30)
print("🚀 SUCESSO! O arquivo 'resultado_agileengine.csv' foi criado!")
print("="*30)