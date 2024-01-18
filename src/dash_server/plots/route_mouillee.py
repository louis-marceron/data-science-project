import plotly.express as px
from dash import dcc

def generate_weather_graph(df):
    # Grouper les données par conditions atmosphériques et compter le nombre d'accidents par condition
    accidents_par_conditions = df.groupby('Conditions_Atmosphériques').size().reset_index(name='Nombre d\'accidents')

    # Créer un graphique à barres avec Plotly Express
    fig = px.bar(accidents_par_conditions, x='Conditions_Atmosphériques', y='Nombre d\'accidents',
                 color='Nombre d\'accidents',
                 labels={'Nombre d\'accidents': 'Nombre d\'accidents'},
                 title='Nombre d\'accidents en fonction des conditions atmosphériques')

    # Personnaliser la mise en page si nécessaire
    fig.update_layout(xaxis_title='Conditions Atmosphériques', yaxis_title='Nombre d\'accidents', xaxis_tickangle=-45)
    
    # Retourner le graphique Plotly Express en tant que composant Dash
    return fig
