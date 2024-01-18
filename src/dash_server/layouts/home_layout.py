from dash import dcc, html, Dash, State
from dash.dependencies import Input, Output
import pandas as pd
from ..plots.plot1 import create_line_plot
from ..plots.plot_taux_homme_femme import generate_sexe_plot
from ..plots.vehicule_plus_accident import generate_vehicle_accident_count_plot
from ..plots.aglomeration_accident import generate_accidents_graph
from ..plots.vehicule_usager_ACM import perform_mca_and_visualize
from ..plots.vitesse_max import generate_speed_plot
from ..plots.equipement_secu import create_acm_plot
from ..plots.route_mouillee import generate_weather_graph
from ..plots.accidents_type_route import generate_accident_type_route_plot
from ..plots.generate_weighted_accident_type_route_plot import generate_weighted_accident_type_route_plot
from ..plots.generate_weighted_by_kvm_accident_type_route_plot import generate_weighted_by_kvm_accident_type_route_plot

from ..plots.acm_gravite_selon_accident import create_acm_plot2
from ..plots.plot1 import create_line_plot


def load_data():
    years = ['2019', '2020', '2021', '2022']
    data = {}
    for year in years:
        df_usager = pd.read_csv(f"clean_data/{year}_clean/usagers-{year}.csv", sep=";")
        df_top_10 = pd.read_csv(f"clean_data/{year}_clean/top_10_percent_dataset.csv", sep=";")
        data[year] = {'usager': df_usager, 'top_10': df_top_10}
    return data


def all(app):
    data = load_data()

    # List of plot functions and their respective data types
    plot_functions = [
        (generate_sexe_plot, 'usager'),
        (perform_mca_and_visualize, 'top_10'),
        (generate_speed_plot, 'top_10'),
        (generate_accident_type_route_plot, 'top_10'),
        (generate_weighted_accident_type_route_plot, 'top_10'),
        (generate_weighted_by_kvm_accident_type_route_plot, 'top_10'),
        (generate_vehicle_accident_count_plot, 'top_10'),
        (generate_accidents_graph, 'top_10'),
        (generate_weather_graph, 'top_10'),
        (create_acm_plot, 'top_10'),
        (create_acm_plot2, 'top_10')    ]

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
            style={'display': 'flex', 'justify-content': 'center', 'padding-top': '25px', 'gap': '20px'}
        )

        return html.Div([
            html.Div([
                html.Header(html.H1("Gravité et fréquence des accidents de la route"), className='header'),
                radio_years
            ]),
            dcc.Tabs([
                dcc.Tab(label='Hypothèses / Préjugés', children=[
                    html.Div([
                        
                        dcc.Graph(id=generate_sexe_plot.__name__)
                    ], className='tab-content'),

                    html.Div([
                        dcc.Graph(id=perform_mca_and_visualize.__name__)
                    ], className='tab-content'),

                    html.Div([
                        dcc.Graph(id=generate_speed_plot.__name__)
                    ], className='tab-content'),

                    html.Div([
                        dcc.Graph(id=generate_accident_type_route_plot.__name__)
                    ], className='tab-content'),

                    html.Div([
                        dcc.Graph(id=generate_weighted_accident_type_route_plot.__name__)
                    ], className='tab-content'),

                    html.Div([
                        dcc.Graph(id=generate_weighted_by_kvm_accident_type_route_plot.__name__)
                    ], className='tab-content'),

                    html.Div([
                        dcc.Graph(id=generate_vehicle_accident_count_plot.__name__)
                    ], className='custom-tab'),
                ], className='custom-tab'),

                dcc.Tab(label='Lieux', children=[
                    html.Div([
                        #radio_years,
                        dcc.Graph(id=generate_accidents_graph.__name__)
                    ], className='tab-content'),
                ], className='custom-tab'),

                dcc.Tab(label='Météo', children=[
                    html.Div([
                        #radio_years,
                        dcc.Graph(id=generate_weather_graph.__name__)
                    ], className='tab-content'),
                ], className='custom-tab'),

                dcc.Tab(label='Equipements de sécurité', children=[
                    html.Div([
                        #radio_years,
                        dcc.Graph(id=create_acm_plot.__name__),
                    ], className='tab-content'),
                    
                    html.Div([
                        dcc.Graph(id=create_acm_plot2.__name__)
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
            ], className='custom-tabs'),
        ], className='main-container')

    @app.callback(
        [Output(func.__name__, 'figure') for func, _ in plot_functions],
        [Input('radio-years', 'value')]
    )
    def update_plots(year):
        results = []
        for func, data_type in plot_functions:
            df = data[year][data_type]
            results.append(func(df))
        return results

    return get_home_layout()
