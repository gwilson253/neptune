import boto3
import pickle
import json
import pandas as pd
from datetime import datetime
from io import StringIO

def lambda_handler(event, context):
    model = get_model()

    pickle_event_body(event['body'])
    data_json = json.loads(json.loads(event['body']))
    df = pd.DataFrame(columns=data_json['columns'],
                      data=data_json['data'],
                      index=data_json['index'])
    save_dataframe(df)
    df['_pred'] = model.predict(df.values)

    return {
        'statusCode': 200,
        'body': json.dumps(df.to_json(orient='split'))
    }

def get_model():
    s3 = boto3.client('s3')

    bucket = 'gwilson253awsprojects'
    key = 'neptune/wine_model.pkl'

    try:
        obj = s3.get_object(Bucket=bucket, Key=key)
        return pickle.loads(obj['Body'].read())

    except Exception as e:
        print(e)
        raise e

def save_dataframe(dataframe):
    bucket = 'gwilson253awsprojects'
    key = 'neptune/input_df.csv'
    csv_buffer = StringIO()
    dataframe.to_csv(csv_buffer, index=False)
    s3 = boto3.resource('s3')
    s3.Object(bucket, key).put(Body=csv_buffer.getvalue())

def text_save(input, filename):
    bucket = 'gwilson253awsprojects'
    key = 'neptune/{}.txt'.format(filename)
    txt_buffer = StringIO(str(input))
    s3 = boto3.resource('s3')
    s3.Object(bucket, key).put(Body=txt_buffer.getvalue())

def pickle_event_body(event_body):
    bucket = 'gwilson253awsprojects'
    key = 'neptune/event_body.pkl'
    bytes_obj = pickle.dumps(event_body,
                             protocol=pickle.HIGHEST_PROTOCOL)
    s3 = boto3.resource('s3')
    s3.Object(bucket, key).put(Body=bytes_obj)
