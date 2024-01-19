# from dash import Dash
# # from .layouts.home_layout import home_layout
# from .dash_server.layouts.home_layout import all
#
# app = Dash(__name__)
# server = app.server  # Expose the Flask server
#
# if __name__ == '__main__':
#     app.layout = all(app)
#     app.run_server(debug=False)



from dash import Dash, dcc, html, Input, Output, callback
import os


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H1('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
])

@callback(Output('display-value', 'children'), Input('dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run(debug=True)