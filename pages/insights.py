import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.
There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.
The layout of your app should be built as a series of rows of columns.
We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""
# column0 = dbc.Col(
#     [
#     dcc.Markdown("""filler text"""),
#     ]
#  md = 4,   
# )

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## CitiBike users have been taking longer trips!
            (they also are a bit more likely to be female, and they are a tiny bit older on average) 
            
            What are some reasons this may be the case?

            If I were to propose changes at CitiBike to accomodate riders, I would increase the maximum trip time from 45 minutes to an hour and 15 minutes to accomodate the longer trips people are doing.
            """
        ),
    ],
    md=4,
)



column2 = dbc.Col(
    [
        html.Img(src='assets/FeatureImportance.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])