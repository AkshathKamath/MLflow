1. MLflow Project: 'mlflow run https://github.com/AkshathKamath/MLflow.git --experiment-name Loan-Prediction' To create a run directly from repository which will execute the script 'python loan_prediction_mlflow.py' mentioned in the MLproject file.
2. MLflow Model: Can directly access created models by their runid as logged_model in the test_model python file.
3. Mlflow Registry: After registering a model, the model can be accessed as 'models:/{model_name}/{model_version}' mentioned in the model_serve python file. This model can also be served on localhost:{port_no} by executing script 'mlflow models serve -m "models:/{model_name}/{model_version}" -p {port_no} --no-conda'. Can be tested by sending POST request to 'http://127.0.0.1:{port_no}/invocations' with sample JSON load as
   {
   "dataframe_split": {
   "columns": [
   "Gender",
   "Married",
   "Dependents",
   "Education",
   "Self_Employed",
   "LoanAmount",
   "Loan_Amount_Term",
   "Credit_History",
   "Property_Area",
   "TotalIncome"
   ],
   "data": [
   [
   1.0,
   0.0,
   0.0,
   0.0,
   0.0,
   4.98745,
   360.0,
   1.0,
   2.0,
   8.698
   ]
   ]
   }
   }
