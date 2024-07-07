from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_secretsmanager as secretsmanager,
    aws_iam as iam,
    core,
)

class BookManagementAppStack(core.Stack):
    
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Retrieve RDS secret
        db_credentials_secret = secretsmanager.Secret.from_secret_name_v2(self, "DBCredentialsSecret", "dev/db-creds")

        # Lambda function
        lambda_function = _lambda.Function(
            self, 
            "BookManagementFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="main.handler",
            code=_lambda.Code.from_asset("implementation/lambda"),
            environment={
                "DB_SECRET_NAME": db_credentials_secret.secret_name,
                "DB_REGION_NAME": "us-east-1"  # Change to your region
            }
        )

        # Grant Lambda access to secrets
        db_credentials_secret.grant_read(lambda_function)

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