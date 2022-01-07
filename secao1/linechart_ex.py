import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv(r'C:\Users\PICHAU\Desktop\publica\dash\Plotly-Dashboards-with-Dash-master\Data\2010YumaAZ.csv')

df2 = df[['DAY', 'LST_TIME','T_HR_AVG']]

days = ['TUESDASY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']


data = [go.Scatter(x=df2['LST_TIME'], 
				   y=df2[df2['DAY']==day]['T_HR_AVG'], 
				   mode='lines', 
				   name=day) for day in days]

layout = go.Layout(title='Daily temp avg')

fig = go.Figure(data=data,layout=layout)


pyo.plot(fig)