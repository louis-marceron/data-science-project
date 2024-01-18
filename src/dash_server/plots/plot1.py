import plotly.express as px
import pandas as pd
from dash import dcc


def create_line_plot(df):
    df2 = pd.DataFrame({
        "X": [1, 2, 3, 4, 5],
        "Y": [3, 1, 6, 5, 4]
    })

    fig = px.line(df2, x='X', y='Y', title='Sample Line Plot')
    return fig
