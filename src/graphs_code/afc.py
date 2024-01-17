from datetime import datetime

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt
import seaborn as sns


# Conversion de l'année de naissance en tranche d'âge
def convert_birth_year_to_age_group(year):
    current_year = datetime.now().year
    age = current_year - year
    if age < 20:
        return '<20'
    elif age < 40:
        return '20-39'
    elif age < 60:
        return '40-59'
    else:
        return '60+'


def create_graph_afc(data, output_dir_path):
    # Préparation des données pour l'AFC
    data['Tranche_d_age'] = data['Année_Naissance'].apply(convert_birth_year_to_age_group)
    afc_columns = [
        'Conditions_Éclairage', 'Conditions_Atmosphériques', 'Type_Collision',
        'Etat_Surface', 'Place_Occupée', 'Sexe', 'Tranche_d_age',
        'Équipement_Sécurité_1', 'Gravité'
    ]
    # Copie du DataFrame pour éviter SettingWithCopyWarning
    data_afc = data[afc_columns].copy()

    print("copy done")

    # Encodage des variables catégorielles pour l'AFC
    label_encoders = {}
    for column in afc_columns:
        label_encoders[column] = LabelEncoder()
        # Utilisation de .loc pour les modifications en place
        data_afc.loc[:, column] = label_encoders[column].fit_transform(data_afc[column])

    print("encoding done")

    # Réalisation de l'Analyse Factorielle
    fa = FactorAnalysis(n_components=2)
    data_afc_transformed = fa.fit_transform(data_afc)

    # Affichage des résultats de l'AFC
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x=data_afc_transformed[:, 0], y=data_afc_transformed[:, 1], hue=data_afc['Gravité'],
                    palette='viridis')
    plt.xlabel('Facteur 1')
    plt.ylabel('Facteur 2')
    plt.title('Analyse Factorielle des Correspondances')
    plt.legend(title='Gravité', bbox_to_anchor=(1.05, 1), loc='upper left')

    output_file_path = f'{output_dir_path}/afc.png'
    plt.savefig(output_file_path)
