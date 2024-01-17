from dash import html, dcc

from ..plots.plot1 import create_line_plot

def get_home_layout():
    return html.Div([
        html.Header(html.H1("Gravité et fréquence des accidents de la route"), className='header'),

        dcc.Tabs([
            dcc.Tab(label='Hypothèses / Préjugés', children=[
                html.Div([
                    create_line_plot()
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


home_layout = get_home_layout()
