import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_descriptive_statistics_graphs(df, output_dir_path):
    # Assurez-vous que les valeurs -1 et 0 dans 'Année_Naissance' sont exclues
    df_filtered = df[(df['Année_Naissance'] != 0) & (df['Année_Naissance'] != -1)]

    # Liste des colonnes pour l'analyse
    columns_of_interest = ['Conditions_Éclairage', 'Conditions_Atmosphériques', 'Type_Collision', 'Gravité', 'Sexe',
                           'Année_Naissance']

    # Création d'une figure avec des sous-graphiques pour chaque colonne
    fig, axes = plt.subplots(len(columns_of_interest), 1, figsize=(10, 20))

    # Génération des graphiques pour chaque colonne
    for i, col in enumerate(columns_of_interest):
        if col == 'Année_Naissance':
            sns.histplot(df_filtered[col], bins=30, kde=True, ax=axes[i])
            axes[i].set_title('Distribution of Year of Birth')
        else:
            # Calcul des pourcentages
            percent_distribution = df_filtered[col].value_counts(normalize=True) * 100
            sns.barplot(x=percent_distribution.values, y=percent_distribution.index, ax=axes[i])
            axes[i].set_title(f'Percentage Distribution of {col}')
            # Ajout des annotations de pourcentage
            for index, value in enumerate(percent_distribution):
                axes[i].text(value, index, f'{value:.2f}%')

        axes[i].set_xlabel('Percentage' if col != 'Année_Naissance' else 'Year of Birth')
        axes[i].set_ylabel('Frequency' if col == 'Année_Naissance' else col)

    # Ajustement de la mise en page
    plt.tight_layout()

    # Enregistrement des graphiques dans le dossier spécifié
    output_file_path = f'{output_dir_path}/descriptive_statistics_graphs.png'
    plt.savefig(output_file_path)

    return output_file_path
