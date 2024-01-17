import pandas as pd

from src.utils.utils import *
from .top_lieu_accident import generate_accidents_graph
from .afc import generate_afc_and_acm_graph
from .descriptive_statistics import generate_descriptive_statistics_graphs


def generate_plots(annee):
    plots_folder_path = create_plots_images_folder(annee)

    ten_percent_data_file_path = get_top_10_percent_data_file_path(annee)
    df_10_percent = pd.read_csv(ten_percent_data_file_path, sep=";", low_memory=False)

    generate_accidents_graph(df_10_percent, plots_folder_path)
    generate_afc_and_acm_graph(df_10_percent, plots_folder_path)
    generate_descriptive_statistics_graphs(df_10_percent, plots_folder_path)
