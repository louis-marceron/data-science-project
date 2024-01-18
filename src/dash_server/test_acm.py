import pandas as pd
import prince
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input, dash

app = Dash(__name__)

def getMergedData(annee):
    return "__data__-clean/" + str(annee) + "-clean/merged_dataset.csv"

def test_acm(annee):
    # Chargement des données
    df_2022 = pd.read_csv(getMergedData(annee), sep=";", low_memory=False)

    # Sélection des colonnes pertinentes pour l'ACM, y compris la gravité des accidents
    selected_columns = [
        'Gravité',
        'Conditions_Éclairage',
        'Type_Intersection',
        'Conditions_Atmosphériques',
        'Type_Collision',
        'Catégorie_Route',
        # Ajoutez d'autres variables qui pourraient être pertinentes
    ]
    df_selected = df_2022[selected_columns].copy()

    # Suppression des lignes avec des données manquantes pour les variables sélectionnées
    df_selected.dropna(subset=selected_columns, inplace=True)

    # ACM avec les colonnes sélectionnées
    acm = prince.MCA(n_components=2, n_iter=3, random_state=42)
    acm.fit(df_selected)

    # Projections des catégories
    category_projections = acm.transform(df_selected)

    # Création du graphique avec Plotly, en ajustant les échelles des axes
    fig = px.scatter(
        category_projections,
        x=0,
        y=1,
        color=df_selected['Gravité'].astype(str),
        title="Analyse des Correspondances Multiples - Fréquence et Gravité des Accidents",
        labels={'0': 'Axe 1', '1': 'Axe 2'},
        # hover_data=df_selected.columns.tolist(),
        range_x=[-2, 2],  # Exemple d'ajustement de l'échelle de l'axe X
        range_y=[-2, 2]  # Exemple d'ajustement de l'échelle de l'axe Y
    )

    # Augmentation de la taille des points
    fig.update_traces(marker=dict(size=10))

    # Amélioration de la légende
    fig.update_layout(
        legend_title_text='Gravité',
        legend=dict(
            title_font_size=16,
            font_size=12,
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    # Amélioration du graphique
    fig.update_traces(marker=dict(size=5))
    fig.update_layout(legend_title_text='Gravité')

    # Affichage dans Dash
    app.layout = html.Div([
        html.H1("ACM des Accidents de Voiture selon la Gravité"),
        dcc.Graph(figure=fig)
    ])

    # Exécution de l'application Dash
    app.run_server(debug=True)
