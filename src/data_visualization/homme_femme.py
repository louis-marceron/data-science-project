import pandas as pd
import matplotlib.pyplot as plt

def create_grap_homme_femme(annee):
    # Charger les données depuis le fichier CSV
    path = "__data__-clean/"+str(annee)+"-clean/usagers-"+str(annee)+".csv"
    df = pd.read_csv(path, sep=";")

    # Compter le nombre d'hommes et de femmes
    sexe_counts = df['Sexe'].value_counts()
    print(sexe_counts)

    # Créer un diagramme à barres
    plt.bar(sexe_counts.index, sexe_counts.values, color=['blue', 'pink', 'grey'])

    # Ajouter des étiquettes et un titre
    plt.xlabel('Sexe')
    plt.ylabel('Nombre d\'usagers')
    plt.title('Répartition des usagers par sexe')

    # Afficher le diagramme
    plt.savefig("./graphs_images/"+str(annee)+"/homme_femme.png")


if __name__ == '__main__':
    create_grap_homme_femme(2022)