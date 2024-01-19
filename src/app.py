from dash import Dash
from .dash_server.layouts.home_layout import generate_home_layout

app = Dash(__name__)
app.layout = generate_home_layout(app)
server = app.server  # Expose the Flask server

if __name__ == '__main__':
    app.run_server(debug=False)
