import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import plotly.express as px

# Carrega o conjunto de dados nativo do Gapminder
df = px.data.gapminder()

# 1. Gráfico de Dispersão Animado (Gráfico de Bolhas)
fig = px.scatter(
    df,
    x="gdpPercap",          # PIB per capita
    y="lifeExp",            # Expectativa de vida
    size="pop",             # Tamanho da bolha baseado na população
    color="continent",      # Cor baseada no continente
    hover_name="country",   # Nome do país ao passar o mouse
    log_x=True,             # Escala lógica/logarítmica para o eixo X
    animation_frame="year", # Animação baseada nos anos
    title="Evolução de PIB e Expectativa de Vida"
)
fig.show()

# 2. Mapa Coroplético Animado (Mapa de Calor por País)
fig = px.choropleth(
    df,
    locations="iso_alpha",  # Código de 3 letras do país (ex: BRA)
    color="lifeExp",        # Cor baseada na expectativa de vida
    hover_name="country",   # Nome do país ao passar o mouse
    animation_frame="year", # Animação baseada nos anos
    color_continuous_scale="Viridis", # Paleta de cores (Viridis)
    title="Expectativa de vida no mundo"
)
fig.show()