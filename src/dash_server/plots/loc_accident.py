import plotly.express as px
import pandas as pd
from dash import dcc

# Charger votre dataframe à partir de votre source de données
# df = pd.read_csv('votre_fichier.csv')

def generate_accidents_par_departement_plot(df):
    # Compter le nombre d'accidents par département
    accidents_par_departement = df['Code_INSEE_Departement'].value_counts().reset_index()
    accidents_par_departement.columns = ['Code_INSEE_Departement', 'Nombre_Accidents']

    # Créer le graphique en bâtons
    fig = px.bar(accidents_par_departement, 
                 x='Code_INSEE_Departement', 
                 y='Nombre_Accidents',
                 labels={'Code_INSEE_Departement': 'Département', 'Nombre_Accidents': 'Nombre d\'Accidents'},
                 title='Nombre d\'Accidents par Département en France')

    return fig

# Appeler la fonction avec votre dataframe
# fig = generate_accidents_par_departement_plot(df)
# fig.show()  # Afficher le graphique
