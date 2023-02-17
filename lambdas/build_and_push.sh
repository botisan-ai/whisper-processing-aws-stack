#!/bin/sh

set -ex

export ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
export IMAGE_NAME=whisper-processing-lambdas

export REPO_URI=$ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
export IMAGE_URI=$REPO_URI/$IMAGE_NAME:latest

# Build the docker image

docker build -t $IMAGE_URI .

# Login to ECR
aws ecr get-login-password | docker login --username AWS --password-stdin $REPO_URI

# Push it to ECR so that it can be deployed

docker push $IMAGE_URI