import mlflow
model_name = 'Prediction_Model_RF'

model_version = 1
# stage = "Production" # Staging
# mlflow.set_tracking_uri("http://0.0.0.0:5001/")
loaded_model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")

# Predict on a Pandas DataFrame.
import pandas as pd
data = [[
                1.0, ## Sample Test data
                0.0,
                0.0,
                0.0,
                0.0,
                4.98745,
                360.0,
                1.0,
                2.0,
                8.698
            ]]
print(f"Prediction is : {loaded_model.predict(pd.DataFrame(data))}")