#!/usr/bin/env python
# coding: utf-8

# In[115]:


import pandas as pd


# In[116]:


df1=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/Laundry.csv")


# In[117]:


df=df1.melt(id_vars='Washers',value_vars=list(df1.columns[1:]))


# In[118]:


DF=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/cotton.csv")


# In[119]:


DF1=DF.melt(id_vars='Factors',value_vars=list(DF.columns[1:]))


# In[120]:


Df=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/Fabric.csv")


# In[121]:


Df1=Df.melt(id_vars='Factors',value_vars=list(Df.columns[1:]))



# In[122]:


dF=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/LCA.csv")


# In[123]:


dF1=dF.melt(id_vars='Factors',value_vars=list(dF.columns[1:]))




# In[124]:


dp=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/Polyester.csv")



# In[125]:


dp.dropna(axis=1,inplace=True)


# In[126]:


dp1=dp.melt(id_vars='Process',value_vars=list(dp.columns[1:]))




# In[ ]:





# In[127]:

import dash
import plotly.express as px
#from jupyter_dash import JupyterDash
from dash import dcc
from dash import  html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

# Iris bar figure
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df, x="Washers", y="value", color="variable"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

# Text field
def drawFigure1():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(DF1,x="Factors",y="value",color="variable")
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])


def drawFigure2():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(Df1,x="Factors",y="value",color="variable")
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])

def drawFigure3():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(dF1,x="Factors",y="value",color="variable")
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])

def drawFigure4():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(dp1,x="Process",y="value",color="variable")
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])
#draw text1
def drawText1():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Washers/Disinfectors environmental impact"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])


# Drawtext2
def drawText2():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("LCA impact analyses of cotton sheets"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])


def drawText3():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("LCA inventory analysis on cotton  Fabric production"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])



def drawText4():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("LCA inventory analysis on Fibre production"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])

def drawText5():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("LCA analysis of polyester/cotton shirts"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])




# Build App
app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div([

    html.Div([
        html.H1("An analysis of various reports on Commercial laundry, steam sterilisaton and LCA analysis.")
    ]),
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawText1()
                ], width=3),
                dbc.Col([
                    drawText2()
                ], width=3),
                dbc.Col([
                    drawText3()
                ], width=3),
                dbc.Col([
                    drawText4()
                ], width=3),
                ],align='center'),            
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure() 
                ], width=3),
                dbc.Col([
                    drawFigure1()
                ], width=3),
                dbc.Col([
                    drawFigure2() 
                ], width=3),
                dbc.Col([ 
                    drawFigure3()           
                    
                ],width=3),
               ],align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawText5()
                ], width=3),
                ],align='center'), 
             html.Br(),
            dbc.Row([                
                dbc.Col([ 
                    drawFigure4()       
                    
                ],width=6),
                dbc.Col([ 
                    html.P("The energy used is like burning 0.84 gallons of gasoline"), 
                    html.Br(),
                    html.P("The CO2 is like burning 1 gallon of propane"),
                    html.Br(),
                    html.P ("The water used is the average of 15 bathtubs"),
                    html.Br(),
                    html.Img(src = app.get_asset_url('logo.jpg'), className = 'logo'),
                    
                    
                ])
            ],align='center'), 
                 
        ]), color = 'dark'
    )
])

# Run app and display result inline in the notebook
app.run_server()


# In[ ]:




