import pandas as pd

ATTRIBUTES_USAGERS = []  # Specify the attributes you want to drop


def cleanUsagers(input_path, output_path):
    # Read the CSV file
    usagers = pd.read_csv(input_path, delimiter=';')

    # Drop specified attributes
    usagers.drop(columns=ATTRIBUTES_USAGERS, inplace=True)

    # Convert 'Année_Naissance' to integer
    # It's important to handle missing or invalid values to avoid errors
    usagers['an_nais'] = pd.to_numeric(usagers['an_nais'], errors='coerce').fillna(0).astype(int)

    # Replace 0 back with NaN if you want to keep missing values as NaN
    usagers['an_nais'].replace(0, pd.NA, inplace=True)

    # Define mappings for various columns
    catu_mapping = {
        1: "Conducteur",
        2: "Passager",
        3: "Piéton"
    }

    grav_mapping = {
        1: "Indemne",
        2: "Tué",
        3: "Blessé hospitalisé",
        4: "Blessé léger"
    }

    sexe_mapping = {
        1: "Masculin",
        2: "Féminin"
    }

    trajet_mapping = {
        -1: "Non renseigné",
        0: "Non renseigné",
        1: "Domicile – travail",
        2: "Domicile – école",
        3: "Courses – achats",
        4: "Utilisation professionnelle",
        5: "Promenade – loisirs",
        9: "Autre"
    }

    secu_mapping = {
        -1: "Non renseigné",
        0: "Aucun équipement",
        1: "Ceinture",
        2: "Casque",
        3: "Dispositif enfants",
        4: "Gilet réfléchissant",
        5: "Airbag (2RM/3RM)",
        6: "Gants (2RM/3RM)",
        7: "Gants + Airbag (2RM/3RM)",
        8: "Non déterminable",
        9: "Autre"
    }

    locp_mapping = {
        -1: "Non renseigné",
        0: "Sans objet",
        1: "A + 50 m du passage piéton",
        2: "A – 50 m du passage piéton",
        3: "Sans signalisation lumineuse",
        4: "Avec signalisation lumineuse",
        5: "Sur trottoir",
        6: "Sur accotement",
        7: "Sur refuge ou BAU",
        8: "Sur contre allée",
        9: "Inconnue"
    }

    actp_mapping = {
        "-1": "Non renseigné",
        "0": "Non renseigné ou sans objet",
        "1": "Sens véhicule heurtant",
        "2": "Sens inverse du véhicule",
        "3": "Traversant",
        "4": "Masqué",
        "5": "Jouant – courant",
        "6": "Avec animal",
        "9": "Autre",
        "A": "Monte/descend du véhicule",
        "B": "Inconnue"
    }

    etatp_mapping = {
        -1: "Non renseigné",
        1: "Seul",
        2: "Accompagné",
        3: "En groupe"
    }

    # Remove white spaces in the actp column
    usagers["actp"] = usagers["actp"].str.strip()

    # Apply mappings
    usagers["catu"].replace(catu_mapping, inplace=True)
    usagers["grav"].replace(grav_mapping, inplace=True)
    usagers["sexe"].replace(sexe_mapping, inplace=True)
    usagers["trajet"].replace(trajet_mapping, inplace=True)
    usagers["secu1"].replace(secu_mapping, inplace=True)
    usagers["secu2"].replace(secu_mapping, inplace=True)
    usagers["secu3"].replace(secu_mapping, inplace=True)
    usagers["locp"].replace(locp_mapping, inplace=True)
    usagers["actp"].replace(actp_mapping, inplace=True)
    usagers["etatp"].replace(etatp_mapping, inplace=True)

    # Rename columns
    rename_mapping = {
        "Num_Acc": "Identifiant_Accident",
        "id_usager": "Identifiant_Usager",
        "id_vehicule": "Identifiant_Vehicule",
        "num_veh": "Numéro_Véhicule",
        "place": "Place_Occupée",
        "catu": "Catégorie_Usager",
        "grav": "Gravité",
        "sexe": "Sexe",
        "an_nais": "Année_Naissance",
        "trajet": "Motif_Déplacement",
        "secu1": "Équipement_Sécurité_1",
        "secu2": "Équipement_Sécurité_2",
        "secu3": "Équipement_Sécurité_3",
        "locp": "Localisation_Piéton",
        "actp": "Action_Piéton",
        "etatp": "État_Piéton"
    }

    usagers.rename(columns=rename_mapping, inplace=True)

    # Output to a CSV file
    usagers.to_csv(output_path, index=False, sep=';')