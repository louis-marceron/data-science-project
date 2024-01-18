import plotly.express as px

def generate_weighted_by_vkm_fatal_accident_type_route_plot(df):
    traffic_by_category = {
        "Autoroute": 200,
        "Route nationale": 210,
        "Route Départementale et Voie Communale": 415  # Fusion de ces deux catégories
    }

    # Fusionner les catégories "Route Départementale" et "Voie Communale" si nécessaire
    df['Catégorie_Route'] = df['Catégorie_Route'].replace(
        {"Route Départementale": "Route Départementale et Voie Communale",
         "Voie Communale": "Route Départementale et Voie Communale"}
    )

    # Filtrer pour les accidents mortels et les catégories de routes souhaitées
    filtered_df = df[
        (df['Gravité'] == 'Tué') &
        df['Catégorie_Route'].isin(traffic_by_category.keys())
    ].copy()

    # Compter les accidents mortels uniques pour chaque catégorie de route
    fatal_accidents_count = filtered_df.groupby('Catégorie_Route').size()

    # Transformer en DataFrame et réinitialiser l'index
    accidents_df = fatal_accidents_count.reset_index()
    accidents_df.columns = ['Catégorie_Route', 'Nombre_d_accidents_mortels']

    # Joindre les données de trafic
    accidents_df['Trafic (milliards de véhicules-km)'] = accidents_df['Catégorie_Route'].map(traffic_by_category)

    # Calculer les accidents mortels par milliard de véhicules-kilomètres
    accidents_df['Accidents_mortels_par_milliard_vkm'] = accidents_df['Nombre_d_accidents_mortels'] / accidents_df[
        'Trafic (milliards de véhicules-km)']

    # Créer un graphique en barres pondéré
    fig = px.bar(
        accidents_df,
        x='Catégorie_Route',
        y='Accidents_mortels_par_milliard_vkm',
        labels={'x': 'Catégorie de Route', 'y': 'Accidents mortels par milliard de véhicules-km'},
        title='Accidents mortels par milliard de véhicules-kilomètres pour chaque catégorie de route',
        category_orders={'Catégorie_Route': list(traffic_by_category.keys())}
    )

    return fig
