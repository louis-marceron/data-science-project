import pandas as pd
import prince
from dash import Dash, html, dcc
import plotly.express as px


def getMergedData(annee):
    return "clean_data/" + str(annee) + "_clean/merged_dataset.csv"


# Application Dash
app = Dash(__name__)


def afc_gravite_sexe(annee):
    # Chargement des données
    df_2022 = pd.read_csv(getMergedData(annee), sep=";", low_memory=False)

    # Préparation de la table de contingence
    cross_tab = pd.crosstab(df_2022['Gravité'], df_2022['Sexe'])

    # Analyse Factorielle des Correspondances
    ca = prince.CA(
        n_components=2,
        n_iter=3,
        copy=True,
        check_input=True,
        engine='sklearn',
        random_state=42
    )
    ca = ca.fit(cross_tab)

    # Affichage des résultats
    # On récupère les coordonnées des lignes et des colonnes pour le graphique
    row_coords = ca.row_coordinates(cross_tab)
    col_coords = ca.column_coordinates(cross_tab)

    # Création des figures pour les lignes (Gravité) et les colonnes (Sexe)
    fig = px.scatter(
        pd.concat([row_coords.reset_index(), col_coords.reset_index()]),  # Use pd.concat instead of .append
        x=0,
        y=1,
        # text='df.index',
        title="Analyse Factorielle des Correspondances entre Gravité et Sexe"
    )

    fig.update_traces(textposition='top center')

    # Affichage dans Dash
    app.layout = html.Div([
        html.H1("Analyse Factorielle des Correspondances entre Gravité et Sexe"),
        dcc.Graph(figure=fig)
    ])

    # Exécution de l'application Dash
    app.run_server(debug=True)
