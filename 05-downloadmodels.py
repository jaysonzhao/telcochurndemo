from minio import Minio
from minio.error import S3Error

# Create the MinIO client
client = Minio(
    "minio-svc.minio-store.svc.cluster.local:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False  # Set to True if you are using HTTPS
)

AWS_S3_BUCKET = "openshift"

# Download a file 
object_name = 'models/customer_churn_prediction_model_brfc.pkl'
file_path = 'models/customer_churn_prediction_model_brfc.pkl'
bucket_name = 'openshift'

try:
 client.fget_object(AWS_S3_BUCKET, object_name, file_path)
 print(f"'{object_name}' is successfully downloaded to '{file_path}'.")
except S3Error as e:
 print("Error occurred: ", e)

# Download a file 
object_name = 'models/customer_churn_prediction_model_lgbm.pkl'
file_path = 'models/customer_churn_prediction_model_lgbm.pkl'
bucket_name = 'openshift'

try:
 client.fget_object(AWS_S3_BUCKET, object_name, file_path)
 print(f"'{object_name}' is successfully downloaded to '{file_path}'.")
except S3Error as e:
 print("Error occurred: ", e)
