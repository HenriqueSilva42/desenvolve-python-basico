import pandas as pd

# Caminho do arquivo CSV (assumindo que está na mesma pasta que o script)
file_path = 'spotify-2023.csv'

# Lendo o arquivo CSV
df = pd.read_csv(file_path, encoding='latin-1')

# Filtrando apenas as colunas de interesse
df = df[['track_name', 'artist(s)_name', 'artist_count', 'released_year', 'streams']]

# Convertendo as colunas 'released_year' e 'streams' para inteiros
df['released_year'] = pd.to_numeric(df['released_year'], errors='coerce')
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

# Filtrando apenas os anos de interesse
df = df[(df['released_year'] >= 2012) & (df['released_year'] <= 2022)]

# Removendo linhas com valores NaN
df = df.dropna(subset=['released_year', 'streams'])

# Agrupando por ano e encontrando a música com mais streams em cada ano
most_streamed_songs = df.loc[df.groupby('released_year')['streams'].idxmax()]

# Selecionando apenas as colunas de interesse
result = most_streamed_songs[['track_name', 'artist(s)_name', 'released_year', 'streams']].values.tolist()

# Imprimindo a lista final
print(result)
