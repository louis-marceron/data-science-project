import plotly.express as px


def generate_fatal_accident_type_route_plot(df):
    # Filtrer pour les accidents mortels et les catégories de routes souhaitées
    filtered_df = df[
        (df['Gravité'] == 'Tué') &
        df['Catégorie_Route'].isin(["Autoroute", "Route nationale", "Route Départementale", "Voie Communale"])]

    # Créer un histogramme pour visualiser le nombre d'accidents mortels par catégorie de route
    fig = px.histogram(
        filtered_df,
        x='Catégorie_Route',
        labels={'x': 'Catégorie de Route', 'y': 'Nombre d\'accidents mortels'},
        title='Nombre d\'accidents mortels par catégorie de route',
        category_orders={'Catégorie_Route': ["Autoroute", "Route nationale", "Route Départementale", "Voie Communale"]}
    )

    return fig
