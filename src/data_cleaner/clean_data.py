import os

from .clean_caracteristiques import clean_caracteristiques
from .clean_lieux import clean_lieux
from .clean_usagers import clean_usagers
from .clean_vehicules import clean_vehicules
from ..utils import *


def clean_and_merge(annee):
    clean_data_folder_path = create_clean_data_folder(annee)

    print("Cleaning usagers...")
    usager_input_path = get_usager_file_path(annee)
    usager_output_path = clean_data_folder_path + os.path.basename(usager_input_path)
    df_usagers = clean_usagers(usager_input_path, usager_output_path)
    print("")

    print("Cleaning vehicules...")
    vehicules_input_path = get_vehicules_file_path(annee)
    vehicules_output_path = clean_data_folder_path + os.path.basename(vehicules_input_path)
    df_vehicules = clean_vehicules(vehicules_input_path, vehicules_output_path)
    print("")

    print("Cleaning lieux...")
    lieux_input_path = get_lieux_file_path(annee)
    lieux_output_path = clean_data_folder_path + os.path.basename(lieux_input_path)
    df_lieux = clean_lieux(lieux_input_path, lieux_output_path)
    print("")

    print("Cleaning caracteristiques...")
    caracteristiques_input_path = get_caracteristiques_file_path(annee)
    caracteristiques_output_path = clean_data_folder_path + os.path.basename(caracteristiques_input_path)
    df_caracteristiques = clean_caracteristiques(caracteristiques_input_path, caracteristiques_output_path)
    print("")

    print("Merging datasets...")
    df_merged = df_caracteristiques.merge(df_lieux, on='Identifiant_Accident')
    df_merged = df_merged.merge(df_vehicules, on='Identifiant_Accident')
    df_merged = df_merged.merge(df_usagers, on='Identifiant_Accident')
    df_merged.to_csv(clean_data_folder_path + 'merged_dataset.csv', sep=';')
    print("")

    # Sélectionner les 10% premières données
    print("Selecting top 10% of the dataset...")
    df_top_ten_percent = df_merged.head(int(len(df_merged) * 0.1))
    df_top_ten_percent.to_csv(clean_data_folder_path + 'top_10_percent_dataset.csv', sep=";")
    print("Done")


def clean_and_merge_all():
    for annee in range(2019, 2023):
        clean_and_merge(annee)
