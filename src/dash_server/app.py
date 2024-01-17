from dash import Dash
from .layouts.home_layout import home_layout

app = Dash(__name__)
server = app.server  # Expose the Flask server for deployment
app.layout = home_layout


def run_server():
    app.run_server(debug=True)
