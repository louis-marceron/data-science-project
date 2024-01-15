import os
from TextData import TextData
from cleanUsagers import cleanUsagers

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

    cleanUsagers(getPathUsagers(ANNEE), output_dir_path + os.path.basename(getPathUsagers(ANNEE)))

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
