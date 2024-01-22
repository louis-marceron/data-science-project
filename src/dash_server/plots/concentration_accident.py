import plotly.express as px


def generate_accident_concentration_histogram(df):
    # Créer un histogramme en utilisant la commune comme variable
    fig = px.histogram(df, 
            x='Code_INSEE_Commune',
            color='Gravité', 
            labels={'Code_INSEE_Commune': 'Commune'},
            title='Concentration des Accidents par Commune en Histogramme')

    return fig