import pandas as pd

from src.utils.utils import *
from .top_lieu_accident import generate_accidents_graph
from .afc import create_graph_afc


def generate_plots(annee):
    plots_folder_path = create_plots_images_folder(annee)

    generate_accidents_graph(get_merged_data_file_path(annee), plots_folder_path, annee)

    df_2022 = pd.read_csv(f"clean_data/{2022}_clean/top_10_percent_dataset.csv", sep=";", low_memory=False)
    # generate_descriptive_statistics_graphs(df_2022, graphs_dir_path)
    create_graph_afc(df_2022, plots_folder_path)
    print("Done")
