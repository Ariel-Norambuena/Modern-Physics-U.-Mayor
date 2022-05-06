import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import plotly.io as pio
pio.renderers.default='browser'
import plotly.express as px
import plotly.graph_objects as go
import time

start_time = time.time()

# Fit function
def objective(x, T): 
    C1 = 3.7427e8
    C2 = 1.4388e4
    rs = 6.9598e5 
    r0 = 149597890
    return (rs/r0)**2*(C1/x**5)/(np.exp(C2/(x*T))-1)

# Import data
data = pd.read_excel(r'SolarRadiation.xlsx')
lambda_exp = pd.DataFrame(data,columns= ['Longitud de onda (micrometro)'])
B_exp = pd.DataFrame(data,columns= ['Radiacion (W/m^2/micrometro)'])

# Rephase 
lambda_exp = np.ravel(lambda_exp)
B_exp = np.ravel(B_exp)


## Plot using plotly
fig = px.area(data, x="Longitud de onda (micrometro)", y="Radiacion (W/m^2/micrometro)")
fig.update_xaxes(range=(0, 5),constrain='domain')
fig.show()

## Fit curve
popt, _ = curve_fit(objective, lambda_exp, B_exp, 1000)
T = popt
lambda_fit = np.linspace(0.001,100,100000)
B_fit = objective(lambda_fit, T)
index = np.where(B_fit==np.amax(B_fit))
lambda_max = lambda_fit[index]

print('Sun temperature = %.5f (K)\n' % T)
print('Wavelength for maximum radiation = %.5f (\u03BCm)\n' % lambda_max)


## Integration of the radiation curve
dlambda = lambda_fit[1]-lambda_fit[0]
I = np.sum(B_fit)*dlambda
print('Integral of radiation curve = %.5f (W/m^2)\n' % I)

## Percent error
K = 1361
Error = np.abs(I-K)/K*100
print('Integral of radiation curve = %.5f (W/m^2)\n' % I)
print('Percent error solar constant = %.5f %%\n' % Error)

## Plot using plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=lambda_exp, y=B_exp, name = 'Experiment'))
fig.add_trace(go.Scatter(x=lambda_fit, y=B_fit,name = 'Model'))
fig.update_xaxes(range=(0, 5),constrain='domain')
fig.show()

print("--- %s seconds ---" % (time.time() - start_time))