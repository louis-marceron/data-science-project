import plotly.express as px
import pandas as pd
from dash import dcc

# Charger votre dataframe à partir de votre source de données
# df = pd.read_csv('votre_fichier.csv')

def generate_accident_concentration_plot(df):
    # Créer un nuage d'individus (scatter plot) en utilisant la commune comme variable
    fig = px.scatter(df, 
                     x='Code_INSEE_Commune',  # Utilisez la colonne de la commune
                     color='Gravité',
                     size_max=10,  # Ajuster la taille des points selon votre préférence
                     labels={'Code_INSEE_Commune': 'Commune'},
                     title='Concentration des Accidents par Commune')

    return fig

# Appeler la fonction avec votre dataframe
# fig = generate_accident_concentration_plot(df)
# fig.show()  # Afficher le graphique

