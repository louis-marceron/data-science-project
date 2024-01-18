import pandas as pd
import prince
import plotly.express as px
from dash import dcc

def create_acm_plot(df):
    # Sélection des colonnes pour l'ACM
    columns = ['Équipement_Sécurité_1', 'Équipement_Sécurité_2', 'Équipement_Sécurité_3', 'Catégorie_Véhicule']
    df_acm = df[columns]

    # Vérification que toutes les colonnes nécessaires sont présentes
    if not all(col in df.columns for col in columns):
        raise ValueError("Certaines colonnes requises sont manquantes dans le DataFrame")

    # Création de l'objet ACM avec Prince
    acm = prince.MCA(
        n_components=2,
        n_iter=3,
        copy=True,
        check_input=True,
        engine='sklearn',  # Correction ici: 'auto' remplacé par 'sklearn'
        random_state=42
    )
    acm = acm.fit(df_acm)

    # Extraction des coordonnées pour la visualisation
    coordinates = acm.row_coordinates(df_acm)

    # Ajouter les informations de survol
    coordinates['Équipement_Sécurité_1'] = df_acm['Équipement_Sécurité_1']
    coordinates['Équipement_Sécurité_2'] = df_acm['Équipement_Sécurité_2']
    coordinates['Équipement_Sécurité_3'] = df_acm['Équipement_Sécurité_3']
    coordinates['Catégorie_Véhicule'] = df_acm['Catégorie_Véhicule']
    coordinates['index'] = df_acm.index  # Ajoutez l'index si vous voulez l'afficher

    # Création du graphique avec Plotly Express
    fig = px.scatter(
        coordinates, 
        x=0, 
        y=1,
        hover_data=coordinates.columns,
        title="Analyse des Correspondances Multiples sur les équipements portés lors de l'accident selon la catégorie du véhicule"
    )

    # Personnalisation du survol pour afficher les informations de catégorie et d'équipement
    fig.update_traces(
        hovertemplate="<br>".join([
            "Équipement Sécurité 1: %{customdata[2]}",
            "Équipement Sécurité 2: %{customdata[0]}",
            "Équipement Sécurité 3: %{customdata[1]}",
            "Catégorie Véhicule: %{customdata[3]}",
            
        ])
    )

    return dcc.Graph(figure=fig)


