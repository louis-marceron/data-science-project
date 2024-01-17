import pandas as pd
import matplotlib.pyplot as plt

def create_graph_cat_route(annee):
    # Charger les données depuis le fichier CSV
    path = "__data__-clean/"+str(annee)+"-clean/lieux-"+str(annee)+".csv"
    df = pd.read_csv(path, sep=";")

    # Compter le nombre d'hommes et de femmes
    cat_route = df['Catégorie_Route'].value_counts()
    print(cat_route.index)

    # Créer un diagramme à barres
    plt.bar(cat_route.index, cat_route.values, color=['blue', 'pink', 'red', 'yellow', 'green', 'purple', 'grey', 'brown'])

    # Ajouter des étiquettes et un titre
    plt.xlabel('Catégorie')
    plt.ylabel('Nombre de route')
    plt.title('Répartition des catégories de route')

    # Placer la légende à droite du graphique
    plt.legend(labels=cat_route.index, title='Catégories')#, bbox_to_anchor=(1.05, 1), loc='upper left')
    # Supprimer les étiquettes sous l'axe x
    plt.xticks([])

    # Afficher le diagramme
    plt.savefig("./graphs_images/"+str(annee)+"/categorie_route.png")


if __name__ == '__main__':
    create_graph_cat_route(2022)