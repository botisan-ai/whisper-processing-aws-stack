FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.9 AS builder

RUN yum install -y unzip
RUN pip install chalice

# project specific dependencies
RUN yum install -y libsndfile

WORKDIR /build

ADD . /build

RUN pip install -r requirements.txt

# TODO: set it to build args
ENV AWS_DEFAULT_REGION=us-west-2

RUN chalice package ./out

WORKDIR /build/out

RUN unzip ./deployment.zip -d $LAMBDA_TASK_ROOT

FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.9 AS runtime

# project specific dependencies
RUN yum install -y libsndfile

COPY --from=builder $LAMBDA_TASK_ROOT $LAMBDA_TASK_ROOT

CMD [ "app.app" ]
