from dash import Dash
# from .layouts.home_layout import home_layout
from .layouts.home_layout import all

app = Dash(__name__)
server = app.server  # Expose the Flask server


def run_server():
    app.layout = all(app)
    app.run_server(debug=True)
