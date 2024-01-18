import pandas as pd
import prince
import plotly.express as px
from dash import dcc

def create_acm_plot2(df):
    columns = ['Gravité', 'Équipement_Sécurité_1', 'Équipement_Sécurité_2', 'Équipement_Sécurité_3']
    df_acm = df[columns]

    acm = prince.MCA(
        n_components=2,
        n_iter=3,
        copy=True,
        check_input=True,
        engine='sklearn',
        random_state=42
    )
    acm = acm.fit(df_acm)
    
    coordinates = acm.row_coordinates(df_acm)

    coordinates['Gravité'] = df_acm['Gravité']
    coordinates['Équipement_Sécurité_1'] = df_acm['Équipement_Sécurité_1']
    coordinates['Équipement_Sécurité_2'] = df_acm['Équipement_Sécurité_2']
    coordinates['Équipement_Sécurité_3'] = df_acm['Équipement_Sécurité_3']
    coordinates['index'] = df_acm.index 

    fig = px.scatter(
        coordinates,
        x=0,
        y=1,
        hover_data=coordinates.columns,
        title="Analyse des Correspondances Multiples sur les équipements portés lors des accidents selon la gravité de l'accident"
    )
    
    fig.update_traces(
        hovertemplate="<br>".join([
            "Gravité: %{customdata[0]}",
            "Équipement Sécurité 1: %{customdata[2]}",
            "Équipement Sécurité 2: %{customdata[1]}",
            "Équipement Sécurité 3: %{customdata[3]}",
        ])
    )

    return dcc.Graph(figure=fig)
