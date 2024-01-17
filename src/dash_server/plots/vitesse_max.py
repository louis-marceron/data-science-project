import plotly.express as px

def generate_speed_plot(df):
    # Filtrer les données pour inclure uniquement les accidents où la vitesse maximale autorisée est <= 150
    filtered_df = df[df['Vitesse_Maximale_Autorisée'] <= 150]

    # Créer un histogramme pour visualiser ces données
    fig = px.histogram(
        filtered_df,
        x='Vitesse_Maximale_Autorisée',
        nbins=30,  # Le nombre de bins peut être ajusté pour une meilleure visualisation
        labels={'x': 'Vitesse Maximale Autorisée', 'y': 'Nombre d\'accidents'},
        title='Nombre d\'accidents par vitesse maximale autorisée (jusqu\'à 150)'
    )

    # Retourner le graphique sous forme de dcc.Graph
    return fig
