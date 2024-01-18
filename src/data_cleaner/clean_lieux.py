import csv

import pandas as pd
from .validate_csv import validate_csv

ATTRIBUTES_TO_DROP = [
    'Numéro_Route',
    'Indice_Numérique_Route',
    'Lettre_Indice_Route',
    'Numéro_PR',
    'Distance_PR',
    'Largeur_Terre_Plein_Central'
]

# Define mappings for the LIEUX attributes
catr_mapping = {
    1: "Autoroute",
    2: "Route nationale",
    3: "Route Départementale",
    4: "Voie Communale",
    5: "Hors réseau public",
    6: "Parc de stationnement ouvert à la circulation publique",
    7: "Route de métropole urbaine",
    9: "Autre"
}

circ_mapping = {
    -1: "Non renseigné",
    1: "A sens unique",
    2: "Bidirectionnelle",
    3: "A chaussées séparées",
    4: "Avec voies d’affectation variable"
}

vosp_mapping = {
    -1: "Non renseigné",
    0: "Sans objet",
    1: "Piste cyclable",
    2: "Bande cyclable",
    3: "Voie réservée"
}

prof_mapping = {
    -1: "Non renseigné",
    1: "Plat",
    2: "Pente",
    3: "Sommet de côte",
    4: "Bas de côte"
}

plan_mapping = {
    -1: "Non renseigné",
    1: "Partie rectiligne",
    2: "En courbe à gauche",
    3: "En courbe à droite",
    4: "En « S »"
}

surf_mapping = {
    -1: "Non renseigné",
    1: "Normale",
    2: "Mouillée",
    3: "Flaques",
    4: "Inondée",
    5: "Enneigée",
    6: "Boue",
    7: "Verglacée",
    8: "Corps gras – huile",
    9: "Autre",
}

infra_mapping = {
    -1: "Non renseigné",
    0: "Aucun",
    1: "Souterrain - tunnel",
    2: "Pont - autopont",
    3: "Bretelle d’échangeur ou de raccordement",
    4: "Voie ferrée",
    5: "Carrefour aménagé",
    6: "Zone piétonne",
    7: "Zone de péage",
    8: "Chantier",
    9: "Autres"
}

situ_mapping = {
    -1: "Non renseigné",
    0: "Aucun",
    1: "Sur chaussée",
    2: "Sur bande d’arrêt d’urgence",
    3: "Sur accotement",
    4: "Sur trottoir",
    5: "Sur piste cyclable",
    6: "Sur autre voie spéciale",
    8: "Autres"
}

columns_mapping = {
    "Num_Acc": "Identifiant_Accident",
    "catr": "Catégorie_Route",
    "voie": "Numéro_Route",
    "v1": "Indice_Numérique_Route",
    "v2": "Lettre_Indice_Route",
    "circ": "Régime_Circulation",
    "nbv": "Nombre_Voies",
    "vosp": "Voie_Réservée",
    "prof": "Profil_Long",
    "pr": "Numéro_PR",
    "pr1": "Distance_PR",
    "plan": "Tracé_Plan",
    "lartpc": "Largeur_Terre_Plein_Central",
    "larrout": "Largeur_Chaussée",
    "surf": "Etat_Surface",
    "infra": "Aménagement_Infrastructure",
    "situ": "Situation_Accident",
    "vma": "Vitesse_Maximale_Autorisée",
}


def clean_lieux(input_path, output_path):
    # Read the CSV file
    lieux = pd.read_csv(input_path, delimiter=';', dtype={6: str})

    # Convert 'Num_Acc' to string
    lieux['Num_Acc'] = lieux['Num_Acc'].astype(str)

    lieux['voie'] = lieux['voie'].fillna("Non renseigné")
    lieux['v2'] = lieux['v2'].fillna("Non renseigné")

    # If v1 is empty, replace it with "Non renseigné"
    lieux['v1'] = lieux['v1'].fillna("Non renseigné")

    # Handle 'lartpc', convert empty strings to -1
    lieux['lartpc'] = pd.to_numeric(lieux['lartpc'], errors='coerce').fillna(-1)

    # Remove white spaces in 'larrout' if it's a string, and replace empty strings with -1
    if lieux['larrout'].dtype == object:
        lieux['larrout'] = lieux['larrout'].str.strip()
    lieux['larrout'] = lieux['larrout'].fillna(0)

    lieux['lartpc'] = lieux['lartpc'].replace("", -1)

    # Apply mappings
    lieux["catr"].replace(catr_mapping, inplace=True)
    lieux["circ"].replace(circ_mapping, inplace=True)
    lieux["vosp"].replace(vosp_mapping, inplace=True)
    lieux["prof"].replace(prof_mapping, inplace=True)
    lieux["plan"].replace(plan_mapping, inplace=True)
    lieux["surf"].replace(surf_mapping, inplace=True)
    lieux["infra"].replace(infra_mapping, inplace=True)
    lieux["situ"].replace(situ_mapping, inplace=True)

    # Rename columns as needed
    lieux.rename(columns=columns_mapping, inplace=True)

    # Drop specified attributes
    # lieux.drop(columns=ATTRIBUTES_TO_DROP, inplace=True)

    lieux.to_csv(output_path, index=False, sep=';', quoting=csv.QUOTE_NONNUMERIC)
    validate_csv(output_path, delimiter=';')

    return lieux
