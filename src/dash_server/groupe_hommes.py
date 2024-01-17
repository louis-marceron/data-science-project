import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-annee', type='number', placeholder='Entrez une année'),
    html.Button('Soumettre', id='submit-val', n_clicks=0),
    dcc.Graph(id='graph-accidents')
])


def getMergedData(annee):
    return "__data__-clean/" + str(annee) + "-clean/merged_dataset.csv"


def analyze_accidents_by_gender_composition(df):
    # Filtrer les données pour les véhicules occupés uniquement par des hommes
    male_only_vehicles = df[df['Sexe'] == 'Masculin']

    # Filtrer les données pour les véhicules avec une composition mixte
    mixed_gender_vehicles = df[df['Sexe'] != 'Masculin']

    # Compter le nombre d'accidents dans chaque catégorie
    accidents_male_only = len(male_only_vehicles)
    accidents_mixed_gender = len(mixed_gender_vehicles)

    # Créer un dictionnaire avec les résultats
    results = {
        'Accidents dans les véhicules avec uniquement des hommes': accidents_male_only,
        'Accidents dans les véhicules avec une composition mixte': accidents_mixed_gender
    }

    return results


@app.callback(
    Output('graph-accidents', 'figure'),
    [Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-annee', 'value')]
)
def update_graph(n_clicks, annee):
    if annee is None:
        return {}

    file_path = getMergedData(annee)
    try:
        df = pd.read_csv(file_path, sep=";")
        results = analyze_accidents_by_gender_composition(df)

        # Calculer le nombre total d'hommes et de femmes impliqués dans des accidents
        total_hommes = df[df['Sexe'] == 'Masculin'].shape[0]
        total_femmes = df[df['Sexe'] == 'Féminin'].shape[0]

        # Calculer le nombre total d'accidents impliquant des hommes et des femmes
        accidents_hommes = results['Accidents dans les véhicules avec uniquement des hommes']
        accidents_femmes = results['Accidents dans les véhicules avec une composition mixte']

        # Calculer le taux d'accidents pondéré par homme et par femme en pourcentage
        taux_accidents_hommes = (accidents_hommes / total_hommes) * 100
        taux_accidents_femmes = (accidents_femmes / total_femmes) * 100

        # Créer un DataFrame avec les taux pondérés en pourcentage
        taux_df = pd.DataFrame({'Catégorie de véhicules': ['Hommes', 'Femmes'],
                                'Taux d\'accidents pondéré (%)': [taux_accidents_hommes, taux_accidents_femmes]})

        # Utiliser Plotly Express pour créer un graphique à barres empilées
        fig = px.bar(taux_df, x='Catégorie de véhicules', y='Taux d\'accidents pondéré (%)',
                     labels={'Catégorie de véhicules': 'Catégorie de véhicules', 'Taux d\'accidents pondéré (%)': 'Taux d\'accidents pondéré (%)'},
                     title=f'Taux d\'accidents pondérés par genre de passagers pour {annee}',
                     color='Catégorie de véhicules')

        return fig
    except FileNotFoundError:
        return {}



if __name__ == '__main__':
    app.run_server(debug=True)
