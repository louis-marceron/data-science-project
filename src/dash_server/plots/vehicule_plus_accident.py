import plotly.express as px
from dash import dcc
import pandas as pd

def generate_vehicle_accident_count_plot(df):
    # Calculer le nombre d'accidents par type de véhicule
    vehicle_accident_counts = df['Catégorie_Véhicule'].value_counts()

    # Créer un graphique en barres pour visualiser ces données
    fig = px.bar(
        x=vehicle_accident_counts.index, 
        y=vehicle_accident_counts.values,
        labels={'x': 'Type de Véhicule', 'y': 'Nombre d\'accidents'},
        title='Nombre d\'accidents par type de véhicule'
    )

    # Retourner le graphique sous forme de dcc.Graph
    return fig
    # return dcc.Graph(figure=fig)

# Utilisez cette fonction en passant votre dataframe
