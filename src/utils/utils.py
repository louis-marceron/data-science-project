import os.path


def get_caracteristiques_file_path(annee):
    path = "__data__/" + str(annee) + "/caracteristiques-" + str(annee) + ".csv"
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return path


def get_usager_file_path(annee):
    path = "__data__/" + str(annee) + "/usagers-" + str(annee) + ".csv"
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return path


def get_lieux_file_path(annee):
    path = "__data__/" + str(annee) + "/lieux-" + str(annee) + ".csv"
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return path


def get_vehicules_file_path(annee):
    path = "__data__/" + str(annee) + "/vehicules-" + str(annee) + ".csv"
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return path


def get_merged_data_file_path(annee):
    path = "clean_data/" + str(annee) + "_clean/merged_dataset.csv"
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return path


def get_plots_images_folder_path(annee):
    return "plots_images/" + str(annee) + "/"


def create_clean_data_folder(annee):
    if not (os.path.exists(os.path.join("clean_data", str(annee) + "_clean"))):
        os.makedirs(os.path.join("clean_data", str(annee) + "_clean"))
    clean_data_folder_path = "clean_data/" + str(annee) + "_clean/"
    return clean_data_folder_path


def create_plots_images_folder(annee):
    if not (os.path.exists(os.path.join("plots_images", str(annee)))):
        os.makedirs(os.path.join("plots_images", str(annee)))
    output_dir_path = "plots_images/" + str(annee) + "/"
    return output_dir_path
