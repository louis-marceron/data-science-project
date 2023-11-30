import os
import pandas as pd

"""
Quand quelqu'un voudra clean les données, il devra mettre le/les fichiers dans un dossier qui aura pour nom l'année.
Après, il devra changer la constante ANNEE par l'année de son fichier
Il retrouvera ses fichiers clean dans le dossier qui sera créé /ANNEE-clean/

ATTENTION : le fichier clean-data.py ne doit pas être dans le même dossier que les données
"""



ANNEE = 2016

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


ATTRUBUTES_USAGERS = [
    'num_veh'
]
ATTRUBUTES_LIEUX = [
    'voie',
    'v1',
    'v2',
    'pr',
    'pr1',
    'lartpc'
]
ATTRUBUTES_CARACTERISTIQUES = [
    'com',
    'adr'
]
ATTRUBUTES_VEHICULES = [
    'num_veh',
    'choc',
    'motor',
    'occutc'
]



def cleanData(files_with_path, files_without_path, listAttributes):
    df = pd.read_csv(files_with_path, delimiter=';', dtype={'lartpc': str})
    df.drop(listAttributes, axis=1, inplace=True)
    if (files_without_path == FILE_VEHICULES):
        valeurs_a_remplacer = ["1", "4", "5", "6", "8", "9", "11", "12", "16", "17", "18", "19", "20", "21", "39", "40", "41", "42", "43", "50", "60", "80"]
        # Convert "catv" column to string and remove leading/trailing whitespaces
        df["catv"] = df["catv"].astype(str).str.strip()
        df["catv"] = df["catv"].replace(valeurs_a_remplacer, "99")
    df.to_csv("./data-clean/"+str(ANNEE)+"-clean/"+files_without_path, sep=';', index=False)    


def createDir():
    data_folder = "./data-clean"
    if not (os.path.exists(os.path.join(data_folder, str(ANNEE) + "-clean"))):
        os.makedirs(os.path.join(data_folder, str(ANNEE)+"-clean"))


def getFileName():
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk("./data/"+str(ANNEE)):
        for file in f:
            files.append(os.path.join(r, file))
    return files
    

if __name__ == '__main__':
    createDir()

    files_with_path = getFileName()
    files_without_path = []
    for i in range(len(files_with_path)):
        files_without_path.append(os.path.basename(files_with_path[i]))
    
    for file in files_with_path:
        file_without_path = os.path.basename(file)

        #print("file path : "+file)
        #print("file name : "+file_without_path)

        if ((file_without_path == FILE_USAGERS) or (file_without_path == FILE_USAGERS_2)):
            cleanData(file, file_without_path, ATTRUBUTES_USAGERS)
            print("USAGER : OK")
        elif ((file_without_path == FILE_CARACTERISTIQUES) or (file_without_path == FILE_CARACTERISTIQUES_2) or (file_without_path == FILE_CARACTERISTIQUES_3) or (file_without_path == FILE_CARACTERISTIQUES_4)):
            cleanData(file, file_without_path, ATTRUBUTES_CARACTERISTIQUES)
            print("CARACTERISTIQUES : OK")
        elif ((file_without_path == FILE_LIEUX) or (file_without_path == FILE_LIEUX_2)):
            cleanData(file, file_without_path, ATTRUBUTES_LIEUX)
            print("LIEUX : OK")
        elif ((file_without_path == FILE_VEHICULES) or (file_without_path == FILE_VEHICULES_2)):
            cleanData(file, file_without_path, ATTRUBUTES_VEHICULES)
            print("VEHICULES : OK")
        else:
            print("Erreur\n")
