import plotly.express as px

def generate_accident_concentration_plot(df):
    # Créer un nuage d'individus (scatter plot) en utilisant la commune comme variable
    fig = px.scatter(df, 
            x='Code_INSEE_Commune',
            color='Gravité',
            size_max=10,  # Ajuster la taille des points selon votre préférence
            labels={'Code_INSEE_Commune': 'Commune'},
            title='Concentration des Accidents par Commune')

    return fig

