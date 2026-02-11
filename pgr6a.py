import plotly.graph_objects as go
import pandas as pd

data = {
    'Car':['Honda City','Hyundai Creta','Maruti Swift','BMW 3 Series','Audi A4','Kia Seltos','Tata Nexon',
           'Toyata Fortuner','Mahindra Thar','Mercedes'],
    'Horsepower':[118,140,90,255,190,138,118,204,130,120],
    'Mileage':[17.8,16.5,22.0,15.0,14.8,17.0,18.5,12.0,15.2,9.56],
    'Price':[12,17,8,55,50,18,14,38,16,50]
    }
df = pd.DataFrame(data)

fig = go.Figure(data = [go.Scatter3d(x = df['Horsepower'], y = df['Mileage'], z = df['Price'],
      mode = 'markers + lines', marker = dict(size = 6, color = df['Mileage'], colorscale = 'Viridis'),
      line = dict(color = 'blue', width = 2))])

fig.update_layout(title = "Horsepower vs Mileage vs Price",
                  scene = dict(xaxis_title = 'Horsepower(bhp)',
                  yaxis_title = 'Mileage',
                  zaxis_title = 'Price (K)'))
fig.show()
    
