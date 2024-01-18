from dash import dcc, html, Dash, State
from dash.dependencies import Input, Output
import pandas as pd

from ..plots.plot1 import create_line_plot
from ..plots.plot_taux_homme_femme import generate_sexe_plot
from ..plots.vitesse_max import generate_speed_plot
from ..plots.vehicule_plus_accident import generate_vehicle_accident_count_plot
from ..plots.aglomeration_accident import generate_accidents_graph
from ..plots.vehicule_usager_ACM import perform_mca_and_visualize
from ..plots.age_accident import generate_age_accident_box_plot
from ..plots.loc_accident import generate_accidents_par_departement_plot
from ..plots.lieu_max_accident import generate_accident_concentration_plot
from ..plots.concentration_accident import generate_accident_concentration_histogram
from ..plots.acm_concentration import perform_mca_concentration




def all(app):
    df_usager_2019 = pd.read_csv("clean_data/2019_clean/usagers-2019.csv", sep=";")
    df_usager_2020 = pd.read_csv("clean_data/2020_clean/usagers-2020.csv", sep=";")
    df_usager_2021 = pd.read_csv("clean_data/2021_clean/usagers-2021.csv", sep=";")
    df_usager_2022 = pd.read_csv("clean_data/2022_clean/usagers-2022.csv", sep=";")
    df_top_10_2019 = pd.read_csv("clean_data/2019_clean/top_10_percent_dataset.csv", sep=";")
    df_top_10_2020 = pd.read_csv("clean_data/2020_clean/top_10_percent_dataset.csv", sep=";")
    df_top_10_2021 = pd.read_csv("clean_data/2021_clean/top_10_percent_dataset.csv", sep=";")
    df_top_10_2022 = pd.read_csv("clean_data/2022_clean/top_10_percent_dataset.csv", sep=";")

    def get_home_layout():
        radio_years = dcc.RadioItems(
            options=[
                {'label': '2019', 'value': '2019'},
                {'label': '2020', 'value': '2020'},
                {'label': '2021', 'value': '2021'},
                {'label': '2022', 'value': '2022'}
            ],
            value='2022',
            id='radio-years',
            style={'display': 'flex', 'justify-content': 'center', 'padding-top':'25px', 'gap': '20px'}
        )

        return html.Div([
            html.Header(html.H1("Gravité et fréquence des accidents de la route"), className='header'),

        dcc.Tabs([
            dcc.Tab(label='Hypothèses / Préjugés', children=[
                html.Div([
                    # Contenu pour les attributs qui sont des préjugé
                    radio_years,
                    dcc.Graph(id='sexe-plot')
                ], className='tab-content'),

                 html.Div([
                    dcc.Graph(id='perform_mca')
                ], className='tab-content'),

                 html.Div([
                    dcc.Graph(id='generate_speed')
                ], className='tab-content'),

                 html.Div([
                    dcc.Graph(id='generate_vehicle_accident_count')
                ], className='tab-content'),

                 html.Div([
                    dcc.Graph(id='generate_age_accident_box_plot')
                ], className='tab-content'),

                 html.Div([
                    dcc.Graph(id='generate_accidents_par_departement_plot')
                ], className='tab-content'),

                 html.Div([
                    dcc.Graph(id='generate_accident_concentration_plot')
                ], className='tab-content'),
    
                 html.Div([
                    dcc.Graph(id='generate_accident_concentration_histogram')
                ], className='tab-content'),

                html.Div([
                    dcc.Graph(id='perform_mca_concentration')
                ], className='tab-content'),

            ], className='custom-tab'),

                
                
            dcc.Tab(label='Attributs Agravants', children=[
                html.Div([
                    # Contenu pour les attributs les plus agravants
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

    @app.callback(
        [Output('sexe-plot', 'figure'),
        Output('perform_mca', 'figure'),
        Output('generate_speed', 'figure'),
        Output('generate_vehicle_accident_count', 'figure'),
        Output('generate_age_accident_box_plot', 'figure'),
        Output('generate_accidents_par_departement_plot', 'figure'),
        Output('generate_accident_concentration_plot', 'figure'),
        Output('generate_accident_concentration_histogram', 'figure'),
        Output('perform_mca_concentration', 'figure')],
        
        Input('radio-years', 'value')

    )
    def update_sexe_plot(value):
        available_years1 = {'2019': df_usager_2019, '2020': df_usager_2020, '2021': df_usager_2021, '2022': df_usager_2022}
        df_usager = available_years1.get(value, df_usager_2022)

        available_years2 = {'2019': df_top_10_2019, '2020': df_top_10_2020, '2021': df_top_10_2021, '2022': df_top_10_2022}
        df_top_10 = available_years2.get(value, df_top_10_2022)

        return generate_sexe_plot(df_usager), perform_mca_and_visualize(df_top_10), generate_speed_plot(df_top_10), generate_vehicle_accident_count_plot(df_top_10), generate_age_accident_box_plot(df_top_10), generate_accidents_par_departement_plot(df_top_10), generate_accident_concentration_plot(df_top_10), generate_accident_concentration_histogram(df_top_10),perform_mca_concentration(df_top_10)
    
        
    return get_home_layout()
    
