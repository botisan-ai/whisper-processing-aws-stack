#!/usr/bin/env python3
try:
    from aws_cdk import core as cdk
except ImportError:
    import aws_cdk as cdk

from stacks.ecr_stack import WhisperProcessingECRStack
from stacks.processing_stack import WhisperProcessingStack

app = cdk.App()
ecr_stack = WhisperProcessingECRStack(app, "whisper-processing-aws-ecr")
WhisperProcessingStack(
    app,
    'whisper-processing-aws-stack',
    lambda_ecr_repo=ecr_stack.lambda_ecr_repo,
)

app.synth()
