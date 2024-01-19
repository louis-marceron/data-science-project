import plotly.express as px


def generate_weighted_accident_type_route_plot(df):
    # Définir les kilomètres pour chaque catégorie de route
    km_by_category = {
        "Autoroute": 11618,
        "Route nationale": 9620,
        "Route Départementale": 377890,
        "Voie Communale": 704999
    }

    # Filtrer les catégories de routes souhaitées et créer une copie indépendante
    filtered_df = df[
        df['Catégorie_Route'].isin(["Autoroute", "Route nationale", "Route Départementale", "Voie Communale"])
    ].copy()

    # Compter les identifiants d'accidents uniques pour chaque catégorie de route
    accidents_count = filtered_df.groupby('Catégorie_Route')['Identifiant_Accident'].nunique()

    # Transformer le décompte en DataFrame et réinitialiser l'index
    accidents_df = accidents_count.reset_index()
    accidents_df.columns = ['Catégorie_Route', 'Nombre_d_accidents_uniques']

    # Joindre les données de kilomètres
    accidents_df['Kilomètres'] = accidents_df['Catégorie_Route'].map(km_by_category)

    # Calculer les accidents par kilomètre
    accidents_df['Accidents_par_km'] = accidents_df['Nombre_d_accidents_uniques'] / accidents_df['Kilomètres']

    # Créer un histogramme pondéré
    fig = px.bar(
        accidents_df,
        x='Catégorie_Route',
        y='Accidents_par_km',
        labels={'x': 'Catégorie de Route', 'y': 'Accidents par kilomètre'},
        title='Accidents par kilomètre pour chaque catégorie de route',
        category_orders={'Catégorie_Route': ["Autoroute", "Route nationale", "Route Départementale", "Voie Communale"]}
    )

    return fig
