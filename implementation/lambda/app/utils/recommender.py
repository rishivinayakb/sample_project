import pickle
from boto3 import client
from pprint import pprint
import os
import tempfile
from deployment.utils.common_constants import CommonConstants

model_path = CommonConstants.MODEL_PATH
bucket_name = CommonConstants.BUCKET_NAME

# Function to download the model from S3
def download_model_from_s3():
    s3_client = client('s3')
    with tempfile.NamedTemporaryFile() as tf:
        s3_client.download_fileobj(bucket_name, model_path, tf)
        tf.seek(0)
        model = pickle.load(tf)
    return model

# Load the model
model = download_model_from_s3()

def recommend_books(genre: str, rating: float):
    recommendations = model.predict([[genre, rating]])
    return recommendations