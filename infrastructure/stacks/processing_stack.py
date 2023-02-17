import os

import aws_cdk as cdk
import aws_cdk.aws_ecr as ecr
from aws_cdk import aws_stepfunctions as sfn
from aws_cdk import aws_stepfunctions_tasks as tasks

from stacks.chalice_docker import ChaliceDocker

LAMBDAS_SOURCE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), os.pardir, "lambdas"
)


class WhisperProcessingStack(cdk.Stack):
    def __init__(self, scope, id, lambda_ecr_repo: ecr.Repository, **kwargs):
        super().__init__(scope, id, **kwargs)
        self.chalice = ChaliceDocker(
            self,
            "ChaliceApp",
            source_dir=LAMBDAS_SOURCE_DIR,
            ecr_repo=lambda_ecr_repo,
            stage_config={
                "automatic_layer": False,
                "environment_variables": {
                    'NUMBA_CACHE_DIR': '/tmp/numba_cache',
                },
            },
        )

        self.state_machine = sfn.StateMachine(
            self,
            "StateMachine",
            definition=tasks.LambdaInvoke(
                self,
                "InvokeChaliceLambda",
                lambda_function=self.chalice.get_function("ProcessJob"),
                input_path="$.message",
            ).next(sfn.Succeed(self, "Success")),
        )
