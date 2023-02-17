import os
import boto3
from chalice import Chalice


app = Chalice(app_name="whisper-processing-aws-stack")


@app.route("/create_job", methods=["POST"])
def create_job():
    request = app.current_request.json_body
    return request


@app.lambda_function(name="ProcessJob")
def process_job(event, context):
    import librosa
    return event
