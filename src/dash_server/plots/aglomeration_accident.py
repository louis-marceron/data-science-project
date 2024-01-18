import plotly.express as px
from dash import dcc

def generate_accidents_graph(df):
    # Grouper les données par localisation et compter le nombre d'accidents par lieu
    accidents_par_lieu = df.groupby('Localisation').size().reset_index(name='Nombre d\'accidents')

    # Trier les lieux par nombre d'accidents (du plus grand au plus petit)
    accidents_par_lieu = accidents_par_lieu.sort_values(by='Nombre d\'accidents', ascending=False)

    # Afficher les 10 premiers lieux avec le plus d'accidents
    top_lieux = accidents_par_lieu.head(10)

    # Créer un graphique à barres avec Plotly Express
    fig = px.bar(top_lieux, x='Localisation', y='Nombre d\'accidents', color='Nombre d\'accidents',
                 labels={'Nombre d\'accidents': 'Nombre d\'accidents'},
                 title=f'Top 10 des lieux avec le plus d\'accidents en France')

    # Customize the layout if needed
    fig.update_layout(xaxis_title='Localisation', yaxis_title='Nombre d\'accidents', xaxis_tickangle=-45)
    
    # Return the Plotly Express graph as a Dash component
    return dcc.Graph(figure=fig)