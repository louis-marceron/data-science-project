from dash import html, dcc
import pandas as pd

from ..plots.plot1 import create_line_plot
from ..plots.plot_taux_homme_femme import generate_sexe_plot
from ..plots.vitesse_max import generate_speed_plot
from ..plots.vehicule_plus_accident import generate_vehicle_accident_count_plot
from ..plots.vehicule_usager_ACM import perform_mca_and_visualize

def get_home_layout():
    df_usager_2019 = pd.read_csv("clean_data/2019_clean/usagers-2019.csv", sep=";")
    df_usager_2020 = pd.read_csv("clean_data/2020_clean/usagers-2020.csv", sep=";")
    df_usager_2021 = pd.read_csv("clean_data/2021_clean/usagers-2021.csv", sep=";")
    df_usager_2022 = pd.read_csv("clean_data/2022_clean/usagers-2022.csv", sep=";")
    df_top_10_2022 = pd.read_csv("clean_data/2022_clean/top_10_percent_dataset.csv", sep=";")

    return html.Div([
        html.Header(html.H1("Gravité et fréquence des accidents de la route"), className='header'),

        dcc.Tabs([
            dcc.Tab(label='Hypothèses / Préjugés', children=[
                # html.Div([
                #     create_line_plot()
                # ], className='tab-content'),

                html.Div([
                    perform_mca_and_visualize(df_top_10_2022)
                ], className='tab-content'),


                html.Div([
                    # Contenu pour les attributs les plus agravants
                    generate_vehicle_accident_count_plot(df_top_10_2022)
                   
                ], className='tab-content'),

            ], className='custom-tab'),
            dcc.Tab(label='Attributs Agravants', children=[
                html.Div([
                    # Contenu pour les attributs les plus agravants
                    generate_sexe_plot(df_usager_2022)
                   
                ], className='tab-content'),

                html.Div([
                    # Contenu pour les attributs les plus agravants
                    generate_speed_plot(df_top_10_2022)
                   
                ], className='tab-content'),
                
            ], className='custom-tab'),
            dcc.Tab(label='Augmentation de la Fréquence', children=[
                html.Div([
                    # Contenu pour les attributs qui augmentent la fréquence des accidents
                ], className='tab-content'),
            ], className='custom-tab'),
            dcc.Tab(label='Géographie des Accidents', children=[
                html.Div([
                    # Contenu pour la géographie des accidents
                ], className='tab-content'),
            ], className='custom-tab'),
            dcc.Tab(label='Conseils', children=[
                html.Div([
                    # Contenu pour les conseils de sécurité routière
                ], className='tab-content'),
            ], className='custom-tab'),
        ], className='custom-tabs'),
    ], className='main-container')


home_layout = get_home_layout()
