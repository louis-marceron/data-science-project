import os
from TextData import TextData
from cleanUsagers import cleanUsagers
from cleanVehicules import cleanVehicules
from cleanLieux import cleanLieux

ANNEE = 2022

def getPathCaracteristiques(annee):
    return "data/" + str(annee) + "/caracteristiques-" + str(annee) + ".csv"


def getPathUsagers(annee):
    return "data/" + str(annee) + "/usagers-" + str(annee) + ".csv"


def getPathLieux(annee):
    return "data/" + str(annee) + "/lieux-" + str(annee) + ".csv"


def getPathVehicules(annee):
    return "data/" + str(annee) + "/vehicules-" + str(annee) + ".csv"



ATTRIBUTES_CARACTERISTIQUES = [
    'com',
    'adr'
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
    cleanVehicules(getPathVehicules(ANNEE), output_dir_path + os.path.basename(getPathVehicules(ANNEE)))
    cleanLieux(getPathLieux(ANNEE), output_dir_path + os.path.basename(getPathLieux(ANNEE)))

    # Clean caracteristiques 2022
    caracteristiques = TextData(getPathCaracteristiques(ANNEE))
    caracteristiques.read_csv() \
        .drop_attributes(ATTRIBUTES_CARACTERISTIQUES) \
        .output_csv(output_dir_path + os.path.basename(getPathCaracteristiques(ANNEE)))
