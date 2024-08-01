import numpy as np
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.express as px

external_stylesheet = [
    {
        'href':"https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css",
        'rel': "stylesheet",
        'integrity': "sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N",
        'crossorigin':"anonymous"
    }
]

Patients = pd.read_csv("state_wise_daily.csv")
Total = Patients.shape[0]
active = Patients[Patients["Status"]=="Confirmed"].shape[0]
Recover = Patients[Patients["Status"]=="Recovered"].shape[0]
Death = Patients[Patients["Status"]=="Deceased"].shape[0]

options = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Hospitalized', 'value': 'Hospitalized'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}
]

options1 = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Mask', 'value': 'Mask'},
    {'label': 'Sanitizer', 'value': 'Sanitizer'},
    {'label': 'Oxygen', 'value': 'Oxygen'},
]

options2 = [
    {'label': 'Red Zone','value':'Red Zone'},
    {'label': 'Blue Zone','value':'Blue Zone'},
    {'label': 'Green Zone','value':'Green Zone'},
    {'label': 'Orange Zone','value':'Orange Zone'}
]

app = dash.Dash(__name__,external_stylesheets= external_stylesheet)

app.layout = html.Div([
    html.H1('Corona Virus Pandemic', style={'color': '#fff', 'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", className='text-light'),
                    html.H4(Total, className='text-light')
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
        html.Div([
html.Div([
                html.Div([
                    html.H3("Active Cases", className='text-light'),
                    html.H4(active, className='text-light')
                ],className='card-body')
            ],className='card bg-info')
        ],className='col-md-3'),
        html.Div([
html.Div([
                html.Div([
                    html.H3("Recovered Cases", className='text-light'),
                    html.H4(Recover, className='text-light')
                ],className='card-body')
            ],className='card bg-warning')
        ],className='col-md-3'),
        html.Div([
html.Div([
                html.Div([
                    html.H3("Total Deaths", className='text-light'),
                    html.H4(Death, className='text-light')
                ],className='card-body')
            ],className='card bg-success')
        ],className='col-md-3 ')
    ],className='row'),
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(id='plot-graph',options=options1,value='All'),
                dcc.Graph(id='graph')
            ],className='card-body')
        ],className='col-md-6'),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown', options=options2, value='Status',style={"width":"100%"}),
                    dcc.Graph('the_graph')
                ],className='card-body')
            ],className='card')
        ],className='col-md-6')
    ],className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker', options=options, value='All'),
                    dcc.Graph(id='bar')
                ],className='card-body')
            ],className='card')
        ],className = 'col-md-12')
    ],className='row')
],className='Container')


@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(type):

    if type=="All":
        return {'data':[go.Bar(x=Patients['State'],y=Patients['Total'])],
                 'layout':go.Layout(title="State Total Count",plot_bgcolor='orange')}
    if type=="Hospitalized":
        return {'data':[go.Bar(x=Patients['State'],y=Patients['Hospitalized'])],
                 'layout':go.Layout(title="State Total Count",plot_bgcolor='orange')}
    if type=="Recovered":
        return {'data':[go.Bar(x=Patients['State'],y=Patients['Recovered'])],
                 'layout':go.Layout(title="State Total Count",plot_bgcolor='orange')}
    if type=="Deceased":
        return {'data':[go.Bar(x=Patients['State'],y=Patients['Deceased'])],
                 'layout':go.Layout(title="State Total Count",plot_bgcolor='orange')}

@app.callback(Output('graph','figure'),[Input('plot-graph','value')])
def generate_graph(type):
    if type=="All":
        return{'data':[go.Line(x=Patients['Status'],y=Patients['Total'])],
               'layout':go.Layout(title="Commodities Total Count", plot_bgcolor='pink')}

    if type == "Mask":
        return {'data':[go.Line(x=Patients['Status'],y=Patients['Mask'])],
                'layout':go.Layout(title="Commodities Total Count", plot_bgcolor='pink')}

    if type == "Sanitizer":
        return {'data':[go.Line(x=Patients['Status'],y=Patients['Sanitizer'])],
                'layout':go.Layout(title="Commodities Total Count", plot_bgcolor='pink')}

    if type == "Oxygen":
        return {'data':[go.Line(x=Patients['Status'],y=Patients['Oxygen'])],
                'layout':go.Layout(title="Commodities Total Count", plot_bgcolor='pink')}


@app.callback(Output('the_graph','figure'),[Input('my_dropdown','value')])
def generate_graph(my_dropdown):
    piechart = px.pie(data_frame=Patients, names=my_dropdown,hole=0.3)
    return (piechart)


if __name__=='__main__':
    app.run_server(debug=True)