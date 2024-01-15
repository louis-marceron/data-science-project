import os
from TextData import TextData

ANNEE = 2022


def getPathCaracteristiques(annee):
    return "data/" + str(annee) + "/caracteristiques-" + str(annee) + ".csv"


def getPathUsagers(annee):
    return "data/" + str(annee) + "/usagers-" + str(annee) + ".csv"


def getPathLieux(annee):
    return "data/" + str(annee) + "/lieux-" + str(annee) + ".csv"


def getPathVehicules(annee):
    return "data/" + str(annee) + "/vehicules-" + str(annee) + ".csv"


# Attributes to drop
ATTRIBUTES_USAGERS = []
ATTRIBUTES_LIEUX = [
    'voie',
    'v1',
    'v2',
    'pr',
    'pr1',
    'lartpc'
]
ATTRIBUTES_CARACTERISTIQUES = [
    'com',
    'adr'
]
ATTRIBUTES_VEHICULES = [
    'num_veh',
    'choc',
    'motor',
    'occutc'
]


def create_output_dir():
    data_folder = "data-clean"
    if not (os.path.exists(os.path.join(data_folder, str(ANNEE) + "-clean"))):
        os.makedirs(os.path.join(data_folder, str(ANNEE) + "-clean"))
    output_dir_path = data_folder + "/" + str(ANNEE) + "-clean/"
    return output_dir_path


if __name__ == '__main__':
    output_dir_path = create_output_dir()

    # Clean usagers 2022
    usagers = TextData(getPathUsagers(ANNEE))
    usagers.read_csv() \
        .drop_attributes(ATTRIBUTES_USAGERS) \
        .replace_column_values("grav", {
        1: "Indemne",
        2: "Tué",
        3: "Blessé hospitalisé",
        4: "Blessé léger"
    }) \
        .rename_columns({
        "Num_Acc": "Identifiant_Accident",
        "id_usager": "Identifiant_Usager",
        "id_vehicule": "Identifiant_Vehicule",
        "num_Veh": "Numéro_Véhicule",
        "place": "Place_Occupée",
        "catu": "Catégorie_Usager",
        "grav": "Gravité",
        "sexe": "Sexe",
        "An_nais": "Année_Naissance",
        "trajet": "Motif_Déplacement",
        "secu1": "Équipement_Sécurité_1",
        "secu2": "Équipement_Sécurité_2",
        "secu3": "Équipement_Sécurité_3",
        "locp": "Localisation_Piéton",
        "actp": "Action_Piéton",
        "etatp": "État_Piéton"
    }) \
        .output_csv(output_dir_path + os.path.basename(getPathUsagers(ANNEE)))

    # Clean lieux 2022
    lieux = TextData(getPathLieux(ANNEE))
    lieux.read_csv() \
        .drop_attributes(ATTRIBUTES_LIEUX) \
        .output_csv(output_dir_path + os.path.basename(getPathLieux(ANNEE)))

    # Clean caracteristiques 2022
    caracteristiques = TextData(getPathCaracteristiques(ANNEE))
    caracteristiques.read_csv() \
        .drop_attributes(ATTRIBUTES_CARACTERISTIQUES) \
        .output_csv(output_dir_path + os.path.basename(getPathCaracteristiques(ANNEE)))

    # Clean vehicules 2022
    values_to_replace = {value: "99" for value in ["1", "4", "5", "6", "8", "9", "11", "12",
                                                   "16", "17", "18", "19", "20", "21", "39",
                                                   "40", "41", "42", "43", "50", "60", "80"]}
    vehicules = TextData(getPathVehicules(ANNEE))
    vehicules.read_csv() \
        .drop_attributes(ATTRIBUTES_VEHICULES) \
        .convert_columns_to_string(["catv"]) \
        .replace_column_values("catv", values_to_replace) \
        .output_csv(output_dir_path + os.path.basename(getPathVehicules(ANNEE)))
