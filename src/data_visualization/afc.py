from datetime import datetime

import pandas as pd
from sklearn.preprocessing import LabelEncoder
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


def generate_afc_and_acm_graph(df, output_folder):
    # Préparation des données pour l'AFC
    df['Tranche_d_age'] = df['Année_Naissance'].apply(convert_birth_year_to_age_group)
    afc_columns = [
        'Conditions_Éclairage', 'Conditions_Atmosphériques', 'Type_Collision',
        'Etat_Surface', 'Place_Occupée', 'Sexe', 'Tranche_d_age',
        'Équipement_Sécurité_1', 'Gravité'
    ]
    data_afc = df[afc_columns].copy()  # Copie du DataFrame pour éviter SettingWithCopyWarning

    # Encodage des variables catégorielles pour l'AFC
    label_encoders = {}
    for column in afc_columns[:-1]:  # Exclude 'Gravité' from encoding
        label_encoders[column] = LabelEncoder()
        data_afc[column] = label_encoders[column].fit_transform(data_afc[column])

    # Utilisation de MCA de la bibliothèque prince pour l'AFC
    mca = prince.MCA(
        n_components=2,
        n_iter=3,
        copy=True,
        check_input=True,
        engine='sklearn',
        random_state=42,
    )
    mca = mca.fit(data_afc.drop('Gravité', axis=1))  # On ajuste uniquement sur les variables explicatives

    # Transformation des données
    mca.transform(data_afc.drop('Gravité', axis=1))

    # Obtain the row coordinates
    row_coords = mca.row_coordinates(data_afc.drop('Gravité', axis=1))

    # Create a plot using matplotlib
    plt.figure(figsize=(12, 8))
    ax = sns.scatterplot(
        x=row_coords.iloc[:, 0],  # First principal component
        y=row_coords.iloc[:, 1],  # Second principal component
        hue=data_afc['Gravité'],  # Color by 'Gravité'
        palette='viridis'
    )
    ax.set_xlabel('Factor 1')
    ax.set_ylabel('Factor 2')
    ax.set_title('MCA Biplot')
    plt.legend(title='Gravité', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Save the MCA biplot
    mca_biplot_path = f'{output_folder}/mca_biplot.png'
    plt.savefig(mca_biplot_path)
    plt.close()

    # Print the eigenvalues and explained inertia
    eigenvalues = mca.eigenvalues_
    explained_inertia = eigenvalues / eigenvalues.sum()

    print(f'Eigenvalues:\n{eigenvalues}')
    print(f'Explained inertia:\n{explained_inertia}')

    # Save the results
    output_file_path = f'{output_folder}/afc_results.csv'
    data_afc.to_csv(output_file_path)

    # Obtaining the coordinates of the columns (attributes)
    column_coords = mca.column_coordinates(data_afc.drop('Gravité', axis=1))

    # Calculating the squared distances from the origin (as a measure of influence)
    squared_distances = column_coords ** 2

    # Summing the squared distances for each feature across all components
    total_squared_distances = squared_distances.sum(axis=1)

    # Calculating the total sum of squared distances for normalization
    total_sum_of_squared_distances = total_squared_distances.sum()

    # Calculating the percentage contribution of each feature
    percentage_contributions = (total_squared_distances / total_sum_of_squared_distances) * 100

    # Creating a DataFrame for contributions
    contributions_df = pd.DataFrame({
        'Feature': squared_distances.index,
        'Contribution': total_squared_distances,
        'Contribution_Percentage': percentage_contributions
    })

    # Saving the contributions to a CSV file
    contributions_csv_path = f'{output_folder}feature_contributions.csv'
    contributions_df.to_csv(contributions_csv_path, index=False)

    return mca_biplot_path
