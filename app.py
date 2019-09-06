from flask import Flask, request
import pandas as pd
import boto3
import pickle
import os

app = Flask(__name__)

def get_model():
    session = boto3.Session(aws_access_key_id=os.getenv('AWS_ADMIN_ACCESS'),
                            aws_secret_access_key=os.getenv('AWS_ADMIN_SECRET'))

    client = session.client('s3')

    # TODO: make these environment vars
    bucket = 'gwilson253awsprojects'
    key = 'neptune/wine_model.pkl'

    obj = client.get_object(Bucket=bucket, Key=key)
    return pickle.loads(obj['Body'].read())

model = get_model()

@app.route('/')
def index():
    return 'yo!'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.json
        df = pd.read_json(data)
        df['_pred'] = model.predict(df.values)
        return df.to_json(orient='split')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
