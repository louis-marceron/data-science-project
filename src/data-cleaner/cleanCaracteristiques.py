import csv

import pandas as pd
import utils

ATTRIBUTES_TO_DROP = [
    'Code_INSEE_Commune',
    'Adresse'
]

# Define mappings for the CARACTERISTIQUES attributes
lum_mapping = {
    1: "Plein jour",
    2: "Crépuscule ou aube",
    3: "Nuit sans éclairage public",
    4: "Nuit avec éclairage public non allumé",
    5: "Nuit avec éclairage public allumé"
}

agg_mapping = {
    1: "Hors agglomération",
    2: "En agglomération"
}

int_mapping = {
    1: "Hors intersection",
    2: "Intersection en X",
    3: "Intersection en T",
    4: "Intersection en Y",
    5: "Intersection à plus de 4 branches",
    6: "Giratoire",
    7: "Place",
    8: "Passage à niveau",
    9: "Autre intersection"
}

atm_mapping = {
    -1: "Non renseigné",
    1: "Normale",
    2: "Pluie légère",
    3: "Pluie forte",
    4: "Neige - grêle",
    5: "Brouillard - fumée",
    6: "Vent fort - tempête",
    7: "Temps éblouissant",
    8: "Temps couvert",
    9: "Autre"
}

col_mapping = {
    -1: "Non renseigné",
    1: "Deux véhicules - frontale",
    2: "Deux véhicules – par l’arrière",
    3: "Deux véhicules – par le côté",
    4: "Trois véhicules et plus – en chaîne",
    5: "Trois véhicules et plus - collisions multiples",
    6: "Autre collision",
    7: "Sans collision"
}

# Rename columns as needed
columns_mapping = {
    "Num_Acc": "Identifiant_Accident",
    "jour": "Jour_Accident",
    "mois": "Mois_Accident",
    "an": "Année_Accident",
    "hrmn": "Heure_Minute_Accident",
    "lum": "Conditions_Éclairage",
    "dep": "Code_INSEE_Departement",
    "com": "Code_INSEE_Commune",
    "agg": "Localisation",
    "int": "Type_Intersection",
    "atm": "Conditions_Atmosphériques",
    "col": "Type_Collision",
    "adr": "Adresse",
    "lat": "Latitude",
    "long": "Longitude"
}


# Define the function cleanCaracteristiques
def cleanCaracteristiques(input_path, output_path):
    # Read the CSV file
    caracteristiques = pd.read_csv(input_path, delimiter=';')

    # If it's the 2022 dataset, convert Accident_Id to Num_Acc
    if 'Accident_Id' in caracteristiques.columns:
        caracteristiques.rename(columns={'Accident_Id': 'Num_Acc'}, inplace=True)

    # Convert identifiers to string
    caracteristiques['Num_Acc'] = caracteristiques['Num_Acc'].astype(str)
    caracteristiques['adr'] = caracteristiques['adr'].fillna("Non renseignée")

    # Convert 'an', 'mois', and 'jour' to string and pad with zeros where necessary
    caracteristiques['an'] = caracteristiques['an'].astype(str)
    caracteristiques['mois'] = caracteristiques['mois'].astype(str).str.zfill(2)
    caracteristiques['jour'] = caracteristiques['jour'].astype(str).str.zfill(2)

    # Combine 'an', 'mois', 'jour', and 'hrmn' into a single datetime column
    caracteristiques['DateTime'] = pd.to_datetime(caracteristiques['an'] + '-' +
                                                  caracteristiques['mois'] + '-' +
                                                  caracteristiques['jour'] + ' ' +
                                                  caracteristiques['hrmn'],
                                                  format='%Y-%m-%d %H:%M', errors='coerce')

    # Drop the now redundant columns
    caracteristiques.drop(columns=['an', 'mois', 'jour', 'hrmn'], inplace=True)

    # Apply mappings
    caracteristiques["lum"].replace(lum_mapping, inplace=True)
    caracteristiques["agg"].replace(agg_mapping, inplace=True)
    caracteristiques["int"].replace(int_mapping, inplace=True)
    caracteristiques["atm"].replace(atm_mapping, inplace=True)
    caracteristiques["col"].replace(col_mapping, inplace=True)

    # Handle 'adr', 'lat', 'long' as they are (assuming no specific processing needed)
    # If specific processing is needed, add it here

    caracteristiques.rename(columns=columns_mapping, inplace=True)

    # Drop specified attributes
    # caracteristiques.drop(columns=ATTRIBUTES_TO_DROP, inplace=True)

    # Output to a CSV file
    caracteristiques.to_csv(output_path, index=False, sep=';', quoting=csv.QUOTE_NONNUMERIC)

    # Validate the CSV
    utils.validate_csv(output_path, delimiter=';')

    return caracteristiques
