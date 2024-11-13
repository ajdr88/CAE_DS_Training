import uvicorn
from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd
from Stress_Model1 import Stress_Model1


app = FastAPI()
joblib_in = open("AverageStress_LC1.joblib","rb")
model=joblib.load(joblib_in)


@app.get('/')
def index():
    return {'message': 'Stress estimation ML API'}

@app.post('/AverageStress_LC1/predict')



def predict_stress_LC1(data:Stress_Model1):
    model_input = process_csv(data)
    prediction = model.predict(model_input)
    
    return {
        'prediction': prediction[0]
    }

def process_csv(data:Stress_Model1):
    sim_output = pd.read_csv(data)
    X = sim_output['x']
    Y = sim_output['y']
    Z = sim_output['z']
    h_stress = sim_output['hor_stress']
    #ranges for bins
    r_x = (-4.670e+01, 7.330e+01)
    r_y = (-1.800e+02, 2.000e+01)
    r_z = (3.563e+00, 6.644e+01)
    H_2, edges_2 = np.histogramdd((X, Y, Z), range=(r_x, r_y, r_z), bins = (20, 12, 7))
    node_count = H_2.flatten()
    return(node_count)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)