from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_secretsmanager as secretsmanager,
    aws_s3 as s3,
    core
)
from config.env_config import DB_SECRET_NAME, DB_REGION_NAME


class BookManagementAppStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # S3 bucket for model storage
        bucket = s3.Bucket(self, "BookManagementModelBucket")

        # Retrieve RDS secret
        db_credentials_secret = secretsmanager.Secret.from_secret_name_v2(self, "DBCredentialsSecret", DB_SECRET_NAME)

        # Lambda function
        lambda_function = _lambda.Function(
            self,
            "BookManagementFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="main.handler",
            code=_lambda.Code.from_asset("implementation/lambda"),
            environment={
                "DB_SECRET_NAME": db_credentials_secret.secret_name,
                "DB_REGION_NAME": DB_REGION_NAME,
                "BUCKET_NAME": bucket.bucket_name
            },
            timeout=core.Duration.minutes(5),
            memory_size=1024,
        )

        # Grant Lambda permissions
        db_credentials_secret.grant_read(lambda_function)
        bucket.grant_read_write(lambda_function)

        # API Gateway
        api = apigateway.LambdaRestApi(
            self, "BookManagementAPI",
            handler=lambda_function,
            proxy=False
        )

        books = api.root.add_resource("books")
        books.add_method("POST")
        books.add_method("GET")
        book = books.add_resource("{id}")
        book.add_method("GET")
        book.add_method("PUT")
        book.add_method("DELETE")

        reviews = book.add_resource("reviews")
        reviews.add_method("POST")
        reviews.add_method("GET")

        summaries = book.add_resource("summary")
        summaries.add_method("GET")

        recommendations = api.root.add_resource("recommendations")
        recommendations.add_method("GET")

        generate_summary = api.root.add_resource("generate-summary")
        generate_summary.add_method("POST")