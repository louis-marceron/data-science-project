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


def perform_mca_and_create_plot(df, columns):
    # Effectuer l'ACM
    mca = prince.MCA(n_components=2)
    mca = mca.fit(df[columns])

    # Créer un graphique Plotly à partir des résultats de l'ACM
    ax = mca.row_coordinates(df[columns])
    fig = px.scatter(x=ax[0], y=ax[1], text=df[columns].apply(lambda row: ' | '.join(row.values), axis=1))
    return fig


if __name__ == '__main__':
    df_2022 = pd.read_csv(getMergedData(2022), sep=";")

    # Sélectionnez les colonnes appropriées pour l'ACM
    columns_for_mca = ['Conditions_Éclairage', 'Localisation', 'Type_Intersection', 'Conditions_Atmosphériques']

    # Effectuer l'ACM et créer le graphique
    mca_plot = perform_mca_and_create_plot(df_2022, columns_for_mca)

    # Initialiser l'application Dash
    app = Dash(__name__)
    app.layout = html.Div([
        html.H1("Visualisation de l'ACM"),
        dcc.Graph(figure=mca_plot)
    ])

    app.run_server(debug=True)
