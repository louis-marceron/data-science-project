import plotly.express as px
import pandas as pd


def generate_condition_atmosphere_plot(df):

    # Pivoter le DataFrame pour avoir la répartition par gravité
    pivoted_df = df.groupby(['Conditions_Atmosphériques', 'Gravité']).size().unstack(fill_value=0)

    # Créer un graphique à barres empilées
    fig = px.bar(pivoted_df, 
            x=pivoted_df.index, 
            y=pivoted_df.columns, 
            barmode='stack',
            labels={'y': 'Nombre d\'accidents', 'x': 'Conditions Atmosphériques'},
            title='Répartition des accidents par gravité et conditions atmosphériques')
    
    return fig


if __name__ == '__main__':
    df_top_10_2022 = pd.read_csv("clean_data/2022_clean/top_10_percent_dataset.csv", sep=";")
    generate_condition_atmosphere_plot(df_top_10_2022) 