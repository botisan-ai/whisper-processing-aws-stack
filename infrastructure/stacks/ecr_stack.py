from aws_cdk import Stack
import aws_cdk.aws_ecr as ecr

class WhisperProcessingECRStack(Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.lambda_ecr_repo = ecr.Repository(self, id + '-lambdas', repository_name="whisper-processing-lambdas")
        self.batch_ecr_repo = ecr.Repository(self, id + '-batch', repository_name="whisper-processing-batch")
