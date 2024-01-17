from dash import dcc, html, Dash, State
from dash.dependencies import Input, Output
import pandas as pd

from ..plots.plot1 import create_line_plot
from ..plots.plot_taux_homme_femme import generate_sexe_plot
from ..plots.aglomeration_accident import generate_accidents_graph

# app = Dash(__name__)
def all(app):
    df_usager_2019 = pd.read_csv("clean_data/2019_clean/usagers-2019.csv", sep=";")
    df_usager_2020 = pd.read_csv("clean_data/2020_clean/usagers-2020.csv", sep=";")
    df_usager_2021 = pd.read_csv("clean_data/2021_clean/usagers-2021.csv", sep=";")
    df_usager_2022 = pd.read_csv("clean_data/2022_clean/usagers-2022.csv", sep=";")
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
                        # Contenu pour les attributs qui sont des préjugés
                        radio_years,
                        dcc.Graph(id='sexe-plot')
                    ], className='tab-content'),
                ], className='custom-tab'),
                dcc.Tab(label='Attributs Agravants', children=[
                    html.Div([
                        # Contenu pour les attributs qui sont agravants
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
        Output('sexe-plot', 'figure'),
        Input('radio-years', 'value')
    )
    def update_sexe_plot(value):
        available_years = {'2019': df_usager_2019, '2020': df_usager_2020, '2021': df_usager_2021, '2022': df_usager_2022}
        selected_year = available_years.get(value, df_usager_2022)
        return generate_sexe_plot(selected_year)
    
        
    return get_home_layout()
    
