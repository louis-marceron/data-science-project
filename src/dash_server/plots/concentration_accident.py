import plotly.express as px
import pandas as pd
from dash import dcc


def generate_accident_concentration_histogram(df):
    # Créer un histogramme en utilisant la commune comme variable
    fig = px.histogram(df, 
                       x='Code_INSEE_Commune',  # Utilisez la colonne de la commune comme variable x
                       color='Gravité',  # Colorer les barres par gravité
                       labels={'Code_INSEE_Commune': 'Commune'},
                       title='Concentration des Accidents par Commune en Histogramme')

    return fig