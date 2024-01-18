import pandas as pd
import plotly.express as px
from dash import dcc


# Données de population par tranche d'âge
population_par_age = {
    "20-24 ans": 3960928,
    "25-29 ans": 3785179,
    "30-34 ans": 4025795,
    "35-39 ans": 4246212,
    "40-44 ans": 4332710,
    "45-49 ans": 4141330,
    "50-54 ans": 4538614,
    "55-59 ans": 4427076,
    "60-64 ans": 426843,
    "65-69 ans": 3931306,
    "75 ans ou plus": 7106175
}

# Ajouter une colonne de pondération au DataFrame
def generate_age_accident_box_plot(df):
    df = df[~((df['Catégorie_Usager'] == 'Conducteur') & (df['Année_Naissance'] > 2004))] 
    # Pondérer les données directement dans la fonction
    df_pondere = df.copy()
    df_pondere['Poids'] = df_pondere['Catégorie_Usager'].map(population_par_age)

    fig = px.box(
        df_pondere,
        x='Catégorie_Usager',
        y='Année_Naissance',
        labels={'Catégorie_Usager': 'Catégorie d\'Usager', 'Année_Naissance': 'Année de Naissance'},
        title='Distribution des accidents par groupe d\'âge (pondéré)'
    )
    fig.update_yaxes(range=[1900, 2050])

    return fig
    # return dcc.Graph(figure=fig)

