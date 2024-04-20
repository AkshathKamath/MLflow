import pandas as pd
import mlflow
logged_model = 'runs:/6269d000a2464eb2af40bd4027e8e390/RandomForestClassifier' ## From mlflow ui

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
data = [[
                1.0, ## Sample test data
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