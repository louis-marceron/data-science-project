import plotly.express as px


def generate_accident_type_route_plot(df):
    # Filtrer les catégories de routes souhaitées
    filtered_df = df[
        df['Catégorie_Route'].isin(["Autoroute", "Route nationale", "Route Départementale", "Voie Communale"])]

    # Créer un histogramme pour visualiser le nombre d'accidents par catégorie de route
    fig = px.histogram(
        filtered_df,
        x='Catégorie_Route',
        labels={'x': 'Catégorie de Route', 'y': 'Nombre d\'accidents'},
        title='Nombre d\'accidents par catégorie de route',
        category_orders={'Catégorie_Route': ["Autoroute", "Route nationale", "Route Départementale", "Voie Communale"]}
    )

    return fig
