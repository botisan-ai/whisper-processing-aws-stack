# Whisper Processing AWS Stack

This is a full-stack processing pipeline for transcribing voice data using Whipser model.

It is built on top of AWS services, including S3, OpenSearch, Lambda, Step Functions, and Batch.

# Development

## Lambdas

We use AWS Chalice to develop lambdas.

## Batch

The batch jobs are just plain-old Docker containers.

# Deployment

We use AWS CDK to manage and deploy the entire stack.

## Step Functions

The step function definitions are in `infrastructure/stacks/processing_stack.py`. Please make sure to edit based on Step Functions documentation.

## Create ECR repositories

```
make deploy stack="whisper-processing-aws-ecr"
```

## Deploy Lambda Docker Image

```
make build-lambdas
```

## Deploy the Stack

```
make deploy stack="whisper-processing-aws-stack"
```
