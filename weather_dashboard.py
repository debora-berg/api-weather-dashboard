import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# variáveis do .env
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Função para buscar clima de uma cidade
def buscar_clima(cidade):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        clima = {
            'Cidade': cidade,
            'Temperatura (°C)': dados['main']['temp'],
            'Condição': dados['weather'][0]['description'],
            'Humidade (%)': dados['main']['humidity'],
            'Vento (m/s)': dados['wind']['speed']
        }
        return clima
    else:
        print(f'Erro ao buscar clima de {cidade}')
        return None
    
# Lista de cidades
cidades = ['Curitiba', 'São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador']

# Coletar dados
dados_clima = [buscar_clima(cidade) for cidade in cidades]
df = pd.DataFrame(dados_clima)

# Exibir dados
print(df)

# Plotar gráfico
df.plot(x='Cidade', y='Temperatura (°C)', kind='bar', legend=False, title='Temperatura Atual')
plt.ylabel('°C')
plt.tight_layout()
plt.show()
