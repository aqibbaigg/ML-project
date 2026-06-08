## end to end machine learning project
import dagshub
dagshub.init(repo_owner='aqibbaigg', repo_name='ML-project', mlflow=True)
MLflow_Tracking_URI=https://dagshub.com/aqibbaigg/ML-project.mlflow
MLflow_Tracking_username=aqibbaigg
MLflow_Tracking_password=588d48298611dfc2ba6e910509eca9137cf44885
import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
  