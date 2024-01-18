from prince import MCA
import pandas as pd
import plotly.express as px
from dash import dcc

def perform_mca_and_visualize(df):
    # Transformation de l'année de naissance en âge
    current_year = 2024  # Remplacer par l'année actuelle si nécessaire
    df['Age'] = current_year - df['Année_Naissance']

    # Catégorisation de l'âge
    bins = [18, 29, 55, 70, 120]  # 120 pour couvrir les âges supérieurs à 70
    labels = ['18-29', '30-55', '56-70', '71+']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    # Sélection des colonnes pour l'ACM
    columns_to_use = ['Catégorie_Véhicule', 'Sexe', 'Gravité', 'Age_Group']
    mca_df = df[columns_to_use]

    # Réalisation de l'ACM
    mca = MCA(n_components=2)
    mca.fit(mca_df)

    # Transformation des données pour la visualisation
    mca_results = mca.transform(mca_df)

    # Création d'un graphique pour visualiser les résultats de l'ACM
    fig = px.scatter(
        mca_results, 
        x=0, 
        y=1, 
        color=df['Catégorie_Véhicule'],
        labels={'0': 'Composante 1', '1': 'Composante 2'},
        title="Visualisation des résultats de l'ACM : Étudiez les associations entre le type de véhicule, l'âge des usagers, leur sexe, et la gravité des accidents."
    )

    # return dcc.Graph(figure=fig)
    return fig

# Utilisez cette fonction en passant votre dataframe
