import plotly.express as px
from dash import dcc
import pandas as pd

def generate_speed_plot(df):
    # Calculer le décompte des vitesses maximales autorisées
    speed_counts = df['Vitesse_Maximale_Autorisée'].value_counts()

    # Créer un graphique en barres
    fig = px.bar(
        x=speed_counts.index, 
        y=speed_counts.values,
        labels={'x': 'Vitesse Maximale Autorisée', 'y': "Nombre d'accidents"},
        title="Répartition des accidents par vitesse maximale autorisée"
    )

    # Retourner le graphique sous forme de dcc.Graph
    return dcc.Graph(figure=fig)

# Note: Vous devez passer votre dataframe à la fonction generate_speed_plot pour obtenir le résultat.
