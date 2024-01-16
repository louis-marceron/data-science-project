import os

import pandas as pd

from data_cleaner.clean_usagers import clean_usagers
from data_cleaner.clean_vehicules import clean_vehicules
from data_cleaner.clean_lieux import clean_lieux
from data_cleaner.clean_caracteristiques import clean_caracteristiques

from graphs_code.top_lieu_accident import generate_accidents_graph

from graphs_code.top_lieu_accident import generate_accidents_graph
from graphs_code.descriptive_statistics import generate_descriptive_statistics_graphs

from dash import Dash, html, dcc, callback, Output, Input, dash
import plotly.express as px

import prince


def get_path_caracteristiques(annee):
    return "data/" + str(annee) + "/caracteristiques-" + str(annee) + ".csv"


def get_path_usagers(annee):
    return "data/" + str(annee) + "/usagers-" + str(annee) + ".csv"


def get_path_lieux(annee):
    return "data/" + str(annee) + "/lieux-" + str(annee) + ".csv"


def get_path_vehicules(annee):
    return "data/" + str(annee) + "/vehicules-" + str(annee) + ".csv"


def getMergedData(annee):
    return "data-clean/" + str(annee) + "-clean/merged_dataset.csv"


def getGraphFolder(annee):
    return "graphs_images/" + str(annee)


def create_output_dir(folder_name, annee):
    if not (os.path.exists(os.path.join(folder_name, str(annee) + "-clean"))):
        os.makedirs(os.path.join(folder_name, str(annee) + "-clean"))
    output_dir_path = folder_name + "/" + str(annee) + "-clean/"
    return output_dir_path


def create_output_grap_dir(folder_name, annee):
    if not (os.path.exists(os.path.join(folder_name, str(annee)))):
        os.makedirs(os.path.join(folder_name, str(annee)))
    output_dir_path = folder_name + "/" + str(annee)
    return output_dir_path


def clean_and_merge(annee):
    output_dir_path = create_output_dir('data-clean', annee)

    print("Cleaning usagers...")
    df_usagers = clean_usagers(get_path_usagers(annee), output_dir_path + os.path.basename(get_path_usagers(annee)))
    print("")

    print("Cleaning vehicules...")
    df_vehicules = clean_vehicules(get_path_vehicules(annee),
                                   output_dir_path + os.path.basename(get_path_vehicules(annee)))
    print("")

    print("Cleaning lieux...")
    df_lieux = clean_lieux(get_path_lieux(annee), output_dir_path + os.path.basename(get_path_lieux(annee)))
    print("")

    print("Cleaning caracteristiques...")
    df_caracteristiques = clean_caracteristiques(get_path_caracteristiques(annee),
                                                 output_dir_path + os.path.basename(get_path_caracteristiques(annee)))
    print("")

    print("Merging datasets...")
    df_merged = df_caracteristiques.merge(df_lieux, on='Identifiant_Accident')
    df_merged = df_merged.merge(df_vehicules, on='Identifiant_Accident')
    df_merged = df_merged.merge(df_usagers, on='Identifiant_Accident')
    df_merged.to_csv(output_dir_path + 'merged_dataset.csv', sep=';')
    print("")

    # Sélectionner les 10% premières données
    print("Selecting top 10% of the dataset...")
    df_top_ten_percent = df_merged.head(int(len(df_merged) * 0.1))
    df_top_ten_percent.to_csv(output_dir_path + 'top_10_percent_dataset.csv', sep=";")
    print("Done")


# Application Dash
app = Dash(__name__)

if __name__ == '__main__':
    # Chargement des données
    df_2022 = pd.read_csv(getMergedData(2022), sep=";", low_memory=False)

    # Sélection des colonnes pertinentes pour l'ACM, y compris la gravité des accidents
    selected_columns = [
        'Gravité',  # Remplacez par le nom réel de votre colonne de gravité
        'Conditions_Éclairage',
        'Type_Intersection',
        'Conditions_Atmosphériques',
        'Type_Collision',
        'Catégorie_Route',
        # Ajoutez d'autres variables qui pourraient être pertinentes
    ]
    df_selected = df_2022[selected_columns].copy()

    # Suppression des lignes avec des données manquantes pour les variables sélectionnées
    df_selected.dropna(subset=selected_columns, inplace=True)

    # ACM avec les colonnes sélectionnées
    acm = prince.MCA(n_components=2, n_iter=3, random_state=42)
    acm.fit(df_selected)

    # Projections des catégories
    category_projections = acm.transform(df_selected)

    # Création d'un graphique avec Plotly, colorié par gravité
    fig = px.scatter(
        category_projections,
        x=0,
        y=1,
        color=df_selected['Gravité'].astype(str),  # Assurez-vous que c'est une chaîne pour la légende
        title="Analyse des Correspondances Multiples - Fréquence et Gravité des Accidents",
        labels={'0': 'Axe 1', '1': 'Axe 2'},
        # hover_data=df_selected.columns.tolist()  # Convertissez les noms des colonnes en liste
    )

    # Amélioration du graphique
    fig.update_traces(marker=dict(size=5))
    fig.update_layout(legend_title_text='Gravité')

    # Affichage dans Dash
    app.layout = html.Div([
        html.H1("ACM des Accidents de Voiture selon la Gravité"),
        dcc.Graph(figure=fig)
    ])

    # Exécution de l'application Dash
    app.run_server(debug=True)
