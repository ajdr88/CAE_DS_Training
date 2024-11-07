import uvicorn
from fastapi import FastAPI
import joblib
from Stress_Model1 import Stress_Model1

app = FastAPI()
joblib_in = open("AverageStress_LC1.joblib","rb")
model=joblib.load(joblib_in)


@app.get('/')
def index():
    return {'message': 'Stress estimation ML API'}

@app.post('/Stress_LC1/predict')
def predict_stress_LC1(data:Stress_Model1):

    prediction = model.predict(data)
    
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)