import csv

import pandas as pd
import data_cleaner.utils as utils

ATTRIBUTES_TO_DROP = []

# Define mappings for the USAGERS attributes
catu_mapping = {
    1: "Conducteur",
    2: "Passager",
    3: "Piéton"
}

grav_mapping = {
    1: "Indemne",
    2: "Tué",
    3: "Blessé hospitalisé",
    4: "Blessé léger"
}

sexe_mapping = {
    1: "Masculin",
    2: "Féminin",
    -1: "Non renseigné"
}

trajet_mapping = {
    -1: "Non renseigné",
    0: "Non renseigné",
    1: "Domicile – travail",
    2: "Domicile – école",
    3: "Courses – achats",
    4: "Utilisation professionnelle",
    5: "Promenade – loisirs",
    9: "Autre"
}

secu_mapping = {
    -1: "Non renseigné",
    0: "Aucun équipement",
    1: "Ceinture",
    2: "Casque",
    3: "Dispositif enfants",
    4: "Gilet réfléchissant",
    5: "Airbag (2RM/3RM)",
    6: "Gants (2RM/3RM)",
    7: "Gants + Airbag (2RM/3RM)",
    8: "Non déterminable",
    9: "Autre"
}

locp_mapping = {
    -1: "Non renseigné",
    0: "Sans objet",
    1: "A + 50 m du passage piéton",
    2: "A – 50 m du passage piéton",
    3: "Sans signalisation lumineuse",
    4: "Avec signalisation lumineuse",
    5: "Sur trottoir",
    6: "Sur accotement",
    7: "Sur refuge ou BAU",
    8: "Sur contre allée",
    9: "Inconnue"
}

actp_mapping = {
    "-1": "Non renseigné",
    "0": "Non renseigné ou sans objet",
    "1": "Sens véhicule heurtant",
    "2": "Sens inverse du véhicule",
    "3": "Traversant",
    "4": "Masqué",
    "5": "Jouant – courant",
    "6": "Avec animal",
    "9": "Autre",
    "A": "Monte/descend du véhicule",
    "B": "Inconnue"
}

etatp_mapping = {
    -1: "Non renseigné",
    1: "Seul",
    2: "Accompagné",
    3: "En groupe"
}

# Define mappings for the USAGERS column names
columns_mapping = {
    "Num_Acc": "Identifiant_Accident",
    "id_usager": "Identifiant_Usager",
    "id_vehicule": "Identifiant_Vehicule",
    "num_veh": "Numéro_Véhicule",
    "place": "Place_Occupée",
    "catu": "Catégorie_Usager",
    "grav": "Gravité",
    "sexe": "Sexe",
    "an_nais": "Année_Naissance",
    "trajet": "Motif_Déplacement",
    "secu1": "Équipement_Sécurité_1",
    "secu2": "Équipement_Sécurité_2",
    "secu3": "Équipement_Sécurité_3",
    "locp": "Localisation_Piéton",
    "actp": "Action_Piéton",
    "etatp": "État_Piéton"
}


def cleanUsagers(input_path, output_path):
    # Read the CSV file
    usagers = pd.read_csv(input_path, delimiter=';')

    # Convert 'Année_Naissance' to integer
    usagers['an_nais'] = pd.to_numeric(usagers['an_nais'], errors='coerce').fillna(0).astype(int)

    # Replace empty strings with NaN in the 'Année_Naissance' column
    usagers['an_nais'].replace('', pd.NA, inplace=True)

    # Convert identifiers to string
    usagers['Num_Acc'] = usagers['Num_Acc'].astype(str)

    # Check if 'id_usager' column exists (fix for 2020 and 2019 datasets)
    if 'id_usager' in usagers.columns:
        usagers['id_usager'] = usagers['id_usager'].astype(str)

    usagers['id_vehicule'] = usagers['id_vehicule'].astype(str)

    # Remove white spaces in the actp column
    usagers["actp"] = usagers["actp"].str.strip()

    # Rename values of VEHCULES attributes
    usagers["catu"].replace(catu_mapping, inplace=True)
    usagers["grav"].replace(grav_mapping, inplace=True)
    usagers["sexe"].replace(sexe_mapping, inplace=True)
    usagers["trajet"].replace(trajet_mapping, inplace=True)
    usagers["secu1"].replace(secu_mapping, inplace=True)
    usagers["secu2"].replace(secu_mapping, inplace=True)
    usagers["secu3"].replace(secu_mapping, inplace=True)
    usagers["locp"].replace(locp_mapping, inplace=True)
    usagers["actp"].replace(actp_mapping, inplace=True)
    usagers["etatp"].replace(etatp_mapping, inplace=True)

    # Rename columns
    usagers.rename(columns=columns_mapping, inplace=True)

    # Drop specified attributes
    # usagers.drop(columns=ATTRIBUTES_TO_DROP, inplace=True)

    usagers.to_csv(output_path, index=False, sep=';', quoting=csv.QUOTE_NONNUMERIC)
    utils.validate_csv(output_path, delimiter=';')

    return usagers
