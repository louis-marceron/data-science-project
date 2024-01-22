import plotly.express as px

def generate_vehicle_accident_count_plot(df):
    vehicle_accident_counts = df['Catégorie_Véhicule'].value_counts()

    fig = px.bar(
        x=vehicle_accident_counts.index, 
        y=vehicle_accident_counts.values,
        labels={'x': 'Type de Véhicule', 'y': 'Nombre d\'accidents'},
        title='Nombre d\'accidents par type de véhicule'
    )

    return fig
