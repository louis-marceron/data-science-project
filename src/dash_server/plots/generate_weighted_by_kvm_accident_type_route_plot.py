import plotly.express as px


def generate_weighted_by_kvm_accident_type_route_plot(df):
    # Définir le trafic pour chaque catégorie de route en milliards de véhicules-kilomètres
    traffic_by_category = {
        "Autoroute": 200,
        "Route nationale": 210,
        "Route Départementale et Voie Communale": 415  # Fusion de ces deux catégories
    }

    # Fusionner les catégories "Route Départementale" et "Voie Communale"
    df['Catégorie_Route'] = df['Catégorie_Route'].replace(
        {"Route Départementale": "Route Départementale et Voie Communale",
         "Voie Communale": "Route Départementale et Voie Communale"}
    )

    # Filtrer les catégories de routes souhaitées et créer une copie indépendante
    filtered_df = df[
        df['Catégorie_Route'].isin(traffic_by_category.keys())
    ].copy()

    # Compter les identifiants d'accidents uniques pour chaque catégorie de route
    accidents_count = filtered_df.groupby('Catégorie_Route')['Identifiant_Accident'].nunique()

    # Transformer le décompte en DataFrame et réinitialiser l'index
    accidents_df = accidents_count.reset_index()
    accidents_df.columns = ['Catégorie_Route', 'Nombre_d_accidents_uniques']

    # Joindre les données de trafic
    accidents_df['Trafic (milliards de véhicules-km)'] = accidents_df['Catégorie_Route'].map(traffic_by_category)

    # Calculer les accidents par milliard de véhicules-kilomètres
    accidents_df['Accidents_par_milliard_vkm'] = accidents_df['Nombre_d_accidents_uniques'] / accidents_df[
        'Trafic (milliards de véhicules-km)']

    # Créer un graphique en barres pondéré
    fig = px.bar(
        accidents_df,
        x='Catégorie_Route',
        y='Accidents_par_milliard_vkm',
        labels={'x': 'Catégorie de Route', 'y': 'Accidents par milliard de véhicules-km'},
        title='Accidents par milliard de véhicules-kilomètres pour chaque catégorie de route',
        category_orders={'Catégorie_Route': ["Autoroute", "Route nationale", "Route Départementale et Voie Communale"]}
    )

    return fig
