import plotly.express as px
import pandas as pd
from dash import dcc


def generate_sexe_plot(df):
    sexe_counts = df['Sexe'].value_counts()

    fig = px.bar(df, 
        x=sexe_counts.index, 
        y=sexe_counts.values,
        color=['Homme', 'Femme'],
        labels={'x': 'Sexe', 'y': "Nombre d'usagers"},
        title='Répartition des usagers par sexe')

    return fig
    # return dcc.Graph(figure=fig)