import os
import pandas as pd

from src.TextData import TextData

"""
Quand quelqu'un voudra clean les données, il devra mettre le/les fichiers dans un dossier qui aura pour nom l'année.
Après, il devra changer la constante ANNEE par l'année de son fichier
Il retrouvera ses fichiers clean dans le dossier qui sera créé /ANNEE-clean/

ATTENTION : le fichier clean-data.py ne doit pas être dans le même dossier que les données
"""

ANNEE = 2022

FILE_USAGERS = "usagers-" + str(ANNEE) + ".csv"
FILE_USAGERS_2 = "usagers_" + str(ANNEE) + ".csv"
FILE_LIEUX = "lieux-" + str(ANNEE) + ".csv"
FILE_LIEUX_2 = "lieux_" + str(ANNEE) + ".csv"
FILE_VEHICULES = "vehicules-" + str(ANNEE) + ".csv"
FILE_VEHICULES_2 = "vehicules_" + str(ANNEE) + ".csv"
FILE_CARACTERISTIQUES = "caracteristiques-" + str(ANNEE) + ".csv"
FILE_CARACTERISTIQUES_2 = "carcteristiques-" + str(ANNEE) + ".csv"
FILE_CARACTERISTIQUES_3 = "caracteristiques_" + str(ANNEE) + ".csv"
FILE_CARACTERISTIQUES_4 = "carcteristiques_" + str(ANNEE) + ".csv"

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


def cleanData(file_path, columns_to_remove):
    file_name = os.path.basename(file_path)
    output_dir = "./data-clean/" + str(ANNEE) + "-clean/"

    data = TextData(file_path)
    data.read_csv(file_path) \
        .drop_attributes(columns_to_remove)

    if file_name == FILE_VEHICULES:
        values_to_replace = ["1", "4", "5", "6", "8", "9", "11", "12",
                             "16", "17", "18", "19", "20", "21", "39",
                             "40", "41", "42", "43", "50", "60", "80"]

        data.convert_columns_to_string(["catv"])
        data.replace_column_values("catv", values_to_replace, "99")

    data.output_csv(output_dir + file_name)


def createDir():
    data_folder = "./data-clean"
    if not (os.path.exists(os.path.join(data_folder, str(ANNEE) + "-clean"))):
        os.makedirs(os.path.join(data_folder, str(ANNEE) + "-clean"))


def getFileName():
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk("./data/" + str(ANNEE)):
        for file in f:
            files.append(os.path.join(r, file))
    return files


"""
def clean_and_quote_csv(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=',')
        writer = csv.writer(outfile, delimiter=';')

        try:
            # Écrire l'en-tête avec des guillemets
            header = next(reader)
            writer.writerow([f"'{col}'" for col in header])

            # Écrire chaque ligne avec des guillemets et remplacer les virgules par des points-virgules
            for row in reader:
                writer.writerow(["'{}'".format(cell) for cell in row])
        except StopIteration:
            print("Le fichier CSV est vide.")
    os.remove(input_path)
"""

if __name__ == '__main__':
    createDir()

    files_with_path = getFileName()
    files_without_path = []
    for i in range(len(files_with_path)):
        files_without_path.append(os.path.basename(files_with_path[i]))

    for file in files_with_path:

        file_name = os.path.basename(file)

        """
        base_name, _ = os.path.splitext(file_without_path)
        newPath = "./data/"+str(ANNEE)+"/"+base_name+"_v"+str(2)+".csv"
        clean_and_quote_csv(file, newPath)
        file_without_path = os.path.basename(file)
        print(file_without_path)
        """
        if ((file_name == FILE_USAGERS) or (file_name == FILE_USAGERS_2)):
            cleanData(file, ATTRIBUTES_USAGERS)
        elif ((file_name == FILE_CARACTERISTIQUES) or (file_name == FILE_CARACTERISTIQUES_2) or (
                file_name == FILE_CARACTERISTIQUES_3) or (file_name == FILE_CARACTERISTIQUES_4)):
            cleanData(file, ATTRIBUTES_CARACTERISTIQUES)
        elif ((file_name == FILE_LIEUX) or (file_name == FILE_LIEUX_2)):
            cleanData(file, ATTRIBUTES_LIEUX)
        elif ((file_name == FILE_VEHICULES) or (file_name == FILE_VEHICULES_2)):
            cleanData(file, ATTRIBUTES_VEHICULES)
        else:
            print("Erreur\n")
