import os
from cleanUsagers import cleanUsagers
from cleanVehicules import cleanVehicules
from cleanLieux import cleanLieux
from cleanCaracteristiques import cleanCaracteristiques

ANNEE = 2022

def getPathCaracteristiques(annee):
    return "data/" + str(annee) + "/caracteristiques-" + str(annee) + ".csv"


def getPathUsagers(annee):
    return "data/" + str(annee) + "/usagers-" + str(annee) + ".csv"


def getPathLieux(annee):
    return "data/" + str(annee) + "/lieux-" + str(annee) + ".csv"


def getPathVehicules(annee):
    return "data/" + str(annee) + "/vehicules-" + str(annee) + ".csv"


def create_output_dir():
    data_folder = "data-clean"
    if not (os.path.exists(os.path.join(data_folder, str(ANNEE) + "-clean"))):
        os.makedirs(os.path.join(data_folder, str(ANNEE) + "-clean"))
    output_dir_path = data_folder + "/" + str(ANNEE) + "-clean/"
    return output_dir_path


if __name__ == '__main__':
    output_dir_path = create_output_dir()

    print("Cleaning usagers...")
    cleanUsagers(getPathUsagers(ANNEE), output_dir_path + os.path.basename(getPathUsagers(ANNEE)))
    print("")

    print("Cleaning vehicules...")
    cleanVehicules(getPathVehicules(ANNEE), output_dir_path + os.path.basename(getPathVehicules(ANNEE)))
    print("")

    print("Cleaning lieux...")
    cleanLieux(getPathLieux(ANNEE), output_dir_path + os.path.basename(getPathLieux(ANNEE)))
    print("")

    print("Cleaning caracteristiques...")
    cleanCaracteristiques(getPathCaracteristiques(ANNEE),
                          output_dir_path + os.path.basename(getPathCaracteristiques(ANNEE)))
    print("")
