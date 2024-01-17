from dash import Dash
# from .layouts.home_layout import home_layout
from .layouts.home_layout import all

app = Dash(__name__)
server = app.server  # Expose the Flask server for deployment
app.layout = all(app)


def run_server():
    app.run_server(debug=True)
