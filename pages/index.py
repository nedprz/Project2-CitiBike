# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Introduction

            Citibike is a bike share program in NYC that uses docks. It was introduced in 2013, and it was the biggest bike share of the time.

            The importance of Citibike has been brought to the spotlight during the covid pandemic.

            Bike share presents the best SCALABLE alternative to densely packed public transit. 

            I've compared spring CitiBike trips in the Pre-covid era and the post-covid era to see how people are using the service differently

            Being tuned into changes in ridership patterns will help the platform run more efficiently for New Yorkers.

            """
        ),
        dcc.Link(dbc.Button("Let's Ride", color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])