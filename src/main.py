import os
import pandas as pd
from cleanUsagers import cleanUsagers
from cleanVehicules import cleanVehicules
from cleanLieux import cleanLieux
from cleanCaracteristiques import cleanCaracteristiques

ANNEE = 2019


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
    df_usagers = cleanUsagers(getPathUsagers(ANNEE), output_dir_path + os.path.basename(getPathUsagers(ANNEE)))
    print("")

    print("Cleaning vehicules...")
    df_vehicules = cleanVehicules(getPathVehicules(ANNEE), output_dir_path + os.path.basename(getPathVehicules(ANNEE)))
    print("")

    print("Cleaning lieux...")
    df_lieux = cleanLieux(getPathLieux(ANNEE), output_dir_path + os.path.basename(getPathLieux(ANNEE)))
    print("")

    print("Cleaning caracteristiques...")
    df_caracteristiques = cleanCaracteristiques(getPathCaracteristiques(ANNEE),
                                                output_dir_path + os.path.basename(getPathCaracteristiques(ANNEE)))
    print("")

    # Merge datasets
    df_merged = df_caracteristiques.merge(df_lieux, on='Identifiant_Accident')
    df_merged = df_merged.merge(df_vehicules, on='Identifiant_Accident')
    df_merged = df_merged.merge(df_usagers, on='Identifiant_Accident')

    # Save the merged dataset
    print("Merging datasets...")
    df_merged.to_csv(output_dir_path + 'merged_dataset.csv', index=False)
    print("")

    # Sélectionner les 10% premières données
    print("Selecting top 10% of the dataset...")
    df_top_ten_percent = df_merged.head(int(len(df_merged) * 0.1))
    df_top_ten_percent.to_csv(output_dir_path + 'top_10_percent_dataset.csv', index=False)
    print("Done")
