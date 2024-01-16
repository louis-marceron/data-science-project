import csv

import pandas as pd
import data_cleaner.utils as utils

ATTRIBUTES_TO_DROP = [
    'Numéro_Véhicule',
    'Point_de_choc_initial',
    'Type_de_motorisation',
    'Nombre_occupants_transport_commun'
]

# Define mappings for the VEHICULES attributes
senc_mapping = {
    -1: "Non renseigné",
    0: "Inconnu",
    1: "Croissant",
    2: "Décroissant",
    3: "Absence de repère"
}

catv_mapping = {
    0: "Indéterminable",
    1: "Bicyclette",
    2: "Cyclomoteur <50cm3",
    3: "Voiturette",
    4: "Référence inutilisée depuis 2006 (scooter immatriculé)",
    5: "Référence inutilisée depuis 2006 (motocyclette)",
    6: "Référence inutilisée depuis 2006 (side-car)",
    7: "VL seul",
    8: "Référence inutilisée depuis 2006 (VL + caravane)",
    9: "Référence inutilisée depuis 2006 (VL + remorque)",
    10: "VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque",
    11: "Référence inutilisée depuis 2006 (VU (10) + caravane)",
    12: "Référence inutilisée depuis 2006 (VU (10) + remorque)",
    13: "PL seul 3,5T < PTCA <= 7,5T",
    14: "PL seul > 7,5T",
    15: "PL > 3,5T + remorque",
    16: "Tracteur routier seul",
    17: "Tracteur routier + semi-remorque",
    18: "Référence inutilisée depuis 2006 (transport en commun)",
    19: "Référence inutilisée depuis 2006 (tramway)",
    20: "Engin spécial",
    21: "Tracteur agricole",
    30: "Scooter < 50 cm3",
    31: "Motocyclette > 50 cm3 et <= 125 cm3",
    32: "Scooter > 50 cm3 et <= 125 cm3",
    33: "Motocyclette > 125 cm3",
    34: "Scooter > 125 cm3",
    35: "Quad léger <= 50 cm3",
    36: "Quad lourd > 50 cm3",
    37: "Autobus",
    38: "Autocar",
    39: "Train",
    40: "Tramway",
    41: "3RM <= 50 cm3",
    42: "3RM > 50 cm3 <= 125 cm3",
    43: "3RM > 125 cm3",
    50: "EDP à moteur",
    60: "EDP sans moteur",
    80: "VAE",
    99: "Autre véhicule"
}

obs_mapping = {
    -1: "Non renseigné",
    0: "Sans objet",
    1: "Véhicule en stationnement",
    2: "Arbre",
    3: "Glissière métallique",
    4: "Glissière béton",
    5: "Autre glissière",
    6: "Bâtiment, mur, pile de pont",
    7: "Support de signalisation verticale ou poste d’appel d’urgence",
    8: "Poteau",
    9: "Mobilier urbain",
    10: "Parapet",
    11: "Ilot, refuge, borne haute",
    12: "Bordure de trottoir",
    13: "Fossé, talus, paroi rocheuse",
    14: "Autre obstacle fixe sur chaussée",
    15: "Autre obstacle fixe sur trottoir ou accotement",
    16: "Sortie de chaussée sans obstacle",
    17: "Buse – tête d’aqueduc"
}

obsm_mapping = {
    -1: "Non renseigné",
    0: "Aucun",
    1: "Piéton",
    2: "Véhicule",
    4: "Véhicule sur rail",
    5: "Animal domestique",
    6: "Animal sauvage",
    9: "Autre"
}

choc_mapping = {
    -1: "Non renseigné",
    0: "Aucun",
    1: "Avant",
    2: "Avant droit",
    3: "Avant gauche",
    4: "Arrière",
    5: "Arrière droit",
    6: "Arrière gauche",
    7: "Côté droit",
    8: "Côté gauche",
    9: "Chocs multiples"
}

manv_mapping = {
    -1: "Non renseigné",
    0: "Inconnue",
    1: "Sans changement de direction",
    2: "Même sens, même file",
    3: "Entre 2 files",
    4: "En marche arrière",
    5: "A contresens",
    6: "En franchissant le terre-plein central",
    7: "Dans le couloir bus, dans le même sens",
    8: "Dans le couloir bus, dans le sens inverse",
    9: "En s'insérant",
    10: "En faisant demi-tour sur la chaussée",
    11: "Changeant de file à gauche",
    12: "Changeant de file à droite",
    13: "Déporté à gauche",
    14: "Déporté à droite",
    15: "Tournant à gauche",
    16: "Tournant à droite",
    17: "Dépassant à gauche",
    18: "Dépassant à droite",
    19: "Traversant la chaussée",
    20: "Manoeuvre de stationnement",
    21: "Manoeuvre d'évitement",
    22: "Ouverture de porte",
    23: "Arrêté (hors stationnement)",
    24: "En stationnement (avec occupants)",
    25: "Circulant sur trottoir",
    26: "Autres manœuvres"
}

motor_mapping = {
    -1: "Non renseigné",
    0: "Inconnue",
    1: "Hydrocarbures",
    2: "Hybride électrique",
    3: "Electrique",
    4: "Hydrogène",
    5: "Humaine",
    6: "Autre"
}

# Define mappings the VEHICULES column names
columns_mapping = {
    "Num_Acc": "Identifiant_Accident",
    "id_vehicule": "Identifiant_Vehicule",
    "num_veh": "Numéro_Véhicule",
    "senc": "Sens_Circulation",
    "catv": "Catégorie_Véhicule",
    "obs": "Obstacle_fixe_heurté",
    "obsm": "Obstacle_mobile_heurté",
    "choc": "Point_de_choc_initial",
    "manv": "Manoeuvre_principale_avant_accident",
    "motor": "Type_de_motorisation",
    "occutc": "Nombre_occupants_transport_commun"
}

categories_to_ignore = [
    "Bicyclette",
    "Référence inutilisée depuis 2006 (scooter immatriculé)",
    "Référence inutilisée depuis 2006 (motocyclette)",
    "Référence inutilisée depuis 2006 (side-car)",
    "Référence inutilisée depuis 2006 (VL + caravane)",
    "Référence inutilisée depuis 2006 (VL + remorque)",
    "Référence inutilisée depuis 2006 (VU (10) + caravane)",
    "Référence inutilisée depuis 2006 (VU (10) + remorque)",
    "Tracteur routier seul", "Tracteur routier + semi-remorque",
    "Référence inutilisée depuis 2006 (transport en commun)",
    "Référence inutilisée depuis 2006 (tramway)",
    "Engin spécial",
    "Tracteur agricole",
    "Train", "Tramway",
    "3RM <= 50 cm3",
    "3RM > 50 cm3 <= 125 cm3",
    "3RM > 125 cm3",
    "EDP à moteur",
    "EDP sans moteur",
    "VAE"
]


def clean_vehicules(input_path, output_path):
    vehicules = pd.read_csv(input_path, delimiter=';')

    # Convert identifiers to string
    vehicules['Num_Acc'] = vehicules['Num_Acc'].astype(str)
    vehicules['id_vehicule'] = vehicules['id_vehicule'].astype(str)
    vehicules['num_veh'] = vehicules['num_veh'].astype(str)

    # Replace missing values in 'Nombre_occupants_transport_commun' (occutc) with 0
    vehicules['occutc'] = vehicules['occutc'].fillna(0).astype(int)

    # Rename values of VEHCULES attributes
    vehicules["senc"].replace(senc_mapping, inplace=True)
    vehicules["catv"].replace(catv_mapping, inplace=True)
    vehicules["obs"].replace(obs_mapping, inplace=True)
    vehicules["obsm"].replace(obsm_mapping, inplace=True)
    vehicules["choc"].replace(choc_mapping, inplace=True)
    vehicules["manv"].replace(manv_mapping, inplace=True)
    vehicules["motor"].replace(motor_mapping, inplace=True)

    # Rename columns
    vehicules.rename(columns=columns_mapping, inplace=True)

    # Drop specified attributes
    # vehicules.drop(columns=ATTRIBUTES_TO_DROP, inplace=True)

    vehicules['Catégorie_Véhicule'] = vehicules['Catégorie_Véhicule'].replace(categories_to_ignore,
                                                                              'Autre véhicule')

    vehicules.to_csv(output_path, index=False, sep=';', quoting=csv.QUOTE_NONNUMERIC)
    utils.validate_csv(output_path, delimiter=';')

    return vehicules
