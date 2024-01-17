import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


# Fonction pour obtenir le chemin du fichier de données
def getMergedData(annee):
    return "__data__-clean/" + str(annee) + "-clean/merged_dataset.csv"


# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Layout de l'application
app.layout = html.Div([
    dcc.Input(id='input-annee', type='number', placeholder='Entrez une année'),
    html.Button('Soumettre', id='submit-val', n_clicks=0),
    dcc.Graph(id='graph-gravite')
])


# Callback pour mettre à jour le graphique
@app.callback(
    Output('graph-gravite', 'figure'),
    [Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-annee', 'value')]
)
def update_graph(n_clicks, annee):
    if annee is None:
        return {}
    file_path = getMergedData(annee)
    try:
        df = pd.read_csv(file_path, sep=";")
        total_gravity_counts = df['Gravité'].value_counts(normalize=True)
        fig = px.bar(total_gravity_counts, x=total_gravity_counts.index, y=total_gravity_counts.values,
                     labels={'y': 'Proportion', 'index': 'Gravité'})
        fig.update_layout(title=f'Répartition de la Gravité des Accidents pour {annee}')
        return fig
    except FileNotFoundError:
        return {}


# Exécution de l'application
if __name__ == '__main__':
    app.run_server(debug=True)
