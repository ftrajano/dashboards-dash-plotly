import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv(r'C:\Users\PICHAU\Desktop\publica\dash\Plotly-Dashboards-with-Dash-master\Data\mocksurvey.csv')


data = [go.Bar(x=df['Unnamed: 0'] , y=df[col], name=col) for col in df.columns] 

layout = go.Layout(title='Survey', barmode='stack')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)