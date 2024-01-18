import plotly.express as px


def generate_weighted_fatal_accident_type_route_plot(df):
    km_by_category = {
        "Autoroute": 11618,
        "Route nationale": 9620,
        "Route Départementale": 377890,
        "Voie Communale": 704999
    }

    # Filtrer pour les accidents mortels et les catégories de routes souhaitées
    filtered_df = df[
        (df['Gravité'] == 'Tué') &
        df['Catégorie_Route'].isin(km_by_category.keys())
        ].copy()

    # Compter les accidents mortels uniques pour chaque catégorie de route
    fatal_accidents_count = filtered_df.groupby('Catégorie_Route').size()

    # Transformer en DataFrame et réinitialiser l'index
    accidents_df = fatal_accidents_count.reset_index()
    accidents_df.columns = ['Catégorie_Route', 'Nombre_d_accidents_mortels']

    # Joindre les données de kilomètres
    accidents_df['Kilomètres'] = accidents_df['Catégorie_Route'].map(km_by_category)

    # Calculer les accidents mortels par kilomètre
    accidents_df['Accidents_mortels_par_km'] = accidents_df['Nombre_d_accidents_mortels'] / accidents_df['Kilomètres']

    # Créer un histogramme pondéré
    fig = px.bar(
        accidents_df,
        x='Catégorie_Route',
        y='Accidents_mortels_par_km',
        labels={'x': 'Catégorie de Route', 'y': 'Accidents mortels par kilomètre'},
        title='Accidents mortels par kilomètre pour chaque catégorie de route',
        category_orders={'Catégorie_Route': list(km_by_category.keys())}
    )

    return fig
