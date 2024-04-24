# Image-API

This application retrieves images from an S3 bucket and serves them in response to HTTP requests.

## AWS Lambda

The application is deployed on AWS using a Lambda function. This function is triggered by HTTP requests.

## Environment Variables

The application utilizes the following environment variables, which need to be configured on AWS:

- `BOOKS_AWS_ACCESS_KEY_ID`
- `BOOKS_AWS_SECRET_ACCESS_KEY`
- `BOOKS_AWS_REGION`
- `BUCKET_NAME`

**Note:** To avoid explicitly passing the access key, secret access key, and region, it is recommended to use an appropriate Service Account.

## Pipeline

To perform code linting, execute:

```bash
make lint
```

To create the `app.zip` file, which is to be uploaded to AWS as the Lambda function, use:

```bash
make build
```

This file should then be uploaded to AWS to deploy the Lambda function.