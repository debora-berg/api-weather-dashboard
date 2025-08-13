# API Weather Dashboard

Projeto em Python que consome a API pública da OpenWeatherMap para exibir dados climáticos de diversas cidades brasileiras.  
Os dados são apresentados em tabela com `pandas` e visualizados em gráfico com `matplotlib`.

---

## Funcionalidades

- Busca automática de clima em várias cidades
- Retorna: temperatura, umidade, condição do tempo e velocidade do vento
- Geração de gráfico com `matplotlib`
- Exportação dos dados para CSV (opcional)
- Uso seguro de chave de API via `.env`

---

## Tecnologias Utilizadas

- Python 3.x
- [Requests](https://pypi.org/project/requests/) – Requisições HTTP
- [Pandas](https://pandas.pydata.org/) – Manipulação de dados
- [Matplotlib](https://matplotlib.org/) – Geração de gráficos
- API pública [OpenWeatherMap](https://openweathermap.org/api)

---

## Como Executar

1. **Clone o repositório**

```terminal
git clone https://github.com/debora-berg/api-weather-dashboard.git
cd api-weather-dashboard
