# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            BASELINE:

            I looked at spring CitiBike rides in NYC in 2020 and compared to 2019. I used data from March and April of each year for my analysis. 81.5% of these spring trips took place in 2019, much simpler times those were!

            The features that I used for my model were gender, trip duration, hour of start time, and day of the week. There were no features that leaked information about the target, however there are many that overlap with each other such as information about the starting location. For instance, what is the relationship between start time, duration of trip, and end time? You can see that they are linked together so therefore it does not make sense to use all 3.

            I started by running a logistic regression on the data with the target being whether the bike ride took place before the pandemic or during. This test yielded better results than the baseline at 84.4%. Our random forest model yielded a score of 83.73% on the validation data.


            """
        ),

    ],
)

layout = dbc.Row([column1])