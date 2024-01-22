import prince
import plotly.express as px

def create_acm_plot(df):
    columns = ['Équipement_Sécurité_1', 'Équipement_Sécurité_2', 'Équipement_Sécurité_3', 'Catégorie_Véhicule']
    df_acm = df[columns]

    if not all(col in df.columns for col in columns):
        raise ValueError("Certaines colonnes requises sont manquantes dans le DataFrame")

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

    coordinates['Équipement_Sécurité_1'] = df_acm['Équipement_Sécurité_1']
    coordinates['Équipement_Sécurité_2'] = df_acm['Équipement_Sécurité_2']
    coordinates['Équipement_Sécurité_3'] = df_acm['Équipement_Sécurité_3']
    coordinates['Catégorie_Véhicule'] = df_acm['Catégorie_Véhicule']

    fig = px.scatter(
        coordinates, 
        x=0, 
        y=1,
        hover_data=coordinates.columns,
        title="Analyse des Correspondances Multiples sur les équipements portés lors de l'accident selon la catégorie du véhicule"
    )
    fig.update_traces(
        hovertemplate="<br>".join([
            "Équipement Sécurité 1: %{customdata[2]}",
            "Équipement Sécurité 2: %{customdata[0]}",
            "Équipement Sécurité 3: %{customdata[1]}",
            "Catégorie Véhicule: %{customdata[3]}",
            
        ])
    )

    return fig


