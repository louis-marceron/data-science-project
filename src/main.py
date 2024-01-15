import os
from src.TextData import TextData

ANNEE = 2022

# Attributes to drop
ATTRIBUTES_USAGERS = [
    'num_veh'
]
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
    data_folder = "../data-clean"
    if not (os.path.exists(os.path.join(data_folder, str(ANNEE) + "-clean"))):
        os.makedirs(os.path.join(data_folder, str(ANNEE) + "-clean"))
    return "../data-clean/" + str(ANNEE) + "-clean/"


if __name__ == '__main__':
    output_dir_path = create_output_dir()

    # Clean usagers 2022
    raw_usagers_path = '../data/2022/usagers-2022.csv'
    usagers = TextData(raw_usagers_path)
    usagers.read_csv() \
        .drop_attributes(ATTRIBUTES_USAGERS) \
        .output_csv(output_dir_path + os.path.basename(raw_usagers_path))

    # Clean lieux 2022
    raw_lieux_path = '../data/2022/lieux-2022.csv'
    lieux = TextData(raw_lieux_path)
    lieux.read_csv() \
        .drop_attributes(ATTRIBUTES_LIEUX) \
        .output_csv(output_dir_path + os.path.basename(raw_lieux_path))

    # Clean caracteristiques 2022
    raw_caracteristiques_path = '../data/2022/carcteristiques-2022.csv'
    caracteristiques = TextData(raw_caracteristiques_path)
    caracteristiques.read_csv() \
        .drop_attributes(ATTRIBUTES_CARACTERISTIQUES) \
        .output_csv(output_dir_path + os.path.basename(raw_caracteristiques_path))

    # Clean vehicules 2022
    raw_vehicules_path = '../data/2022/vehicules-2022.csv'
    values_to_replace = ["1", "4", "5", "6", "8", "9", "11", "12",
                         "16", "17", "18", "19", "20", "21", "39",
                         "40", "41", "42", "43", "50", "60", "80"]
    vehicules = TextData(raw_vehicules_path)
    vehicules.read_csv() \
        .drop_attributes(ATTRIBUTES_VEHICULES) \
        .convert_columns_to_string(["catv"]) \
        .replace_column_values("catv", values_to_replace, "99") \
        .output_csv(output_dir_path + os.path.basename(raw_vehicules_path))
