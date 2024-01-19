from prince import MCA
import plotly.express as px

def perform_mca_concentration(df):


    # Sélection des colonnes pour l'ACM
    columns_to_use = ['Conditions_Éclairage', 'Conditions_Atmosphériques', 'Gravité', 'Situation_Accident']
    mca_df = df[columns_to_use]

    # Réalisation de l'ACM
    mca = MCA(n_components=2)
    mca.fit(mca_df)

    # Transformation des données pour la visualisation
    mca_results = mca.transform(mca_df)

    # Création d'un graphique pour visualiser les résultats de l'ACM
    fig = px.scatter(
        mca_results, 
        x=0, 
        y=1, 
        color=df['Conditions_Atmosphériques'],
        labels={'0': 'Composante 1', '1': 'Composante 2'},
        title="Visualisation des résultats de l'ACM : Étudiez les associations entre les conditions d'éclairage, les conditions atmosphérique, la situation de l'accident et la gravité des accidents."
    )

    return fig

