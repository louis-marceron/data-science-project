from datetime import datetime

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt
import seaborn as sns
import prince


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

    # Utilisation de MCA de la bibliothèque prince pour l'AFC
    mca = prince.MCA(
        n_components=2,
        n_iter=3,
        copy=True,
        check_input=True,
        engine='sklearn',  # Change this to 'sklearn', 'scipy', or 'fbpca'
        random_state=42
    )
    mca = mca.fit(data_afc.drop('Gravité', axis=1))  # On ajuste uniquement sur les variables explicatives

    # Transformation des données
    data_mca = mca.transform(data_afc.drop('Gravité', axis=1))

    # Obtain the row coordinates
    row_coords = mca.row_coordinates(data_afc.drop('Gravité', axis=1))

    # Now create a plot using matplotlib
    plt.figure(figsize=(12, 8))
    ax = sns.scatterplot(
        x=row_coords[0],  # First principal component
        y=row_coords[1],  # Second principal component
        hue=data_afc['Gravité'],  # Color by 'Gravité'
        palette='viridis'
    )
    ax.set_xlabel('Facteur 1')
    ax.set_ylabel('Facteur 2')
    ax.set_title('Biplot pour l\'Analyse des Correspondances Multiples')
    plt.legend(title='Gravité', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    output_file_path = f'{output_dir_path}/mca_biplot.png'
    plt.savefig(output_file_path)

    # Afficher les contributions des variables aux deux premières composantes
    eigenvalues = mca.eigenvalues_
    explained_inertia = eigenvalues / eigenvalues.sum()

    print(f'Eigenvalues:\n{eigenvalues}')
    print(f'Explained inertia:\n{explained_inertia}')

    # Calcul de l'importance des attributs
    feature_contributions = pd.DataFrame(mca.column_contributions_, index=data_afc.drop('Gravité', axis=1).columns)
    feature_contributions.columns = ['Contribution to Factor 1', 'Contribution to Factor 2']
    print(feature_contributions.sort_values(by='Contribution to Factor 1', ascending=False))

    # Enregistrement des contributions dans un fichier
    feature_contributions.to_csv(f'{output_dir_path}/feature_contributions.csv')

    return output_file_path
