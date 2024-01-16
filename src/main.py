import os
from data_cleaner.clean_usagers import clean_usagers
from data_cleaner.clean_vehicules import clean_vehicules
from data_cleaner.clean_lieux import clean_lieux
from data_cleaner.clean_caracteristiques import clean_caracteristiques


def get_path_caracteristiques(annee):
    return "data/" + str(annee) + "/caracteristiques-" + str(annee) + ".csv"


def get_path_usagers(annee):
    return "data/" + str(annee) + "/usagers-" + str(annee) + ".csv"


def get_path_lieux(annee):
    return "data/" + str(annee) + "/lieux-" + str(annee) + ".csv"


def get_path_vehicules(annee):
    return "data/" + str(annee) + "/vehicules-" + str(annee) + ".csv"


def create_output_dir(folder_name, annee):
    if not (os.path.exists(os.path.join(folder_name, str(annee) + "-clean"))):
        os.makedirs(os.path.join(folder_name, str(annee) + "-clean"))
    output_dir_path = folder_name + "/" + str(annee) + "-clean/"
    return output_dir_path


def create_output_grap_dir(folder_name, annee):
    if not (os.path.exists(os.path.join(folder_name, str(annee)))):
        os.makedirs(os.path.join(folder_name, str(annee)))
    output_dir_path = folder_name + "/" + str(annee)
    return output_dir_path


def clean_and_merge(annee):
    output_dir_path = create_output_dir('data-clean', annee)

    print("Cleaning usagers...")
    df_usagers = clean_usagers(get_path_usagers(annee), output_dir_path + os.path.basename(get_path_usagers(annee)))
    print("")

    print("Cleaning vehicules...")
    df_vehicules = clean_vehicules(get_path_vehicules(annee), output_dir_path + os.path.basename(get_path_vehicules(annee)))
    print("")

    print("Cleaning lieux...")
    df_lieux = clean_lieux(get_path_lieux(annee), output_dir_path + os.path.basename(get_path_lieux(annee)))
    print("")

    print("Cleaning caracteristiques...")
    df_caracteristiques = clean_caracteristiques(get_path_caracteristiques(annee),
                                                 output_dir_path + os.path.basename(get_path_caracteristiques(annee)))
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


if __name__ == '__main__':
    clean_and_merge(2022)
    graphs_dir_path = create_output_grap_dir('graphs_images', 2022)
