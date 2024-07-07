import os
from pydantic import BaseSettings
from deployment.utils.common_constants import CommonConstants


class Settings(BaseSettings):
    db_secret_name: str = CommonConstants.DB_SECRET_NAME
    db_region_name: str = CommonConstants.DB_REGION_NAME

    # Retrieve RDS credentials from AWS Secrets Manager
    db_host: str = os.getenv("DB_HOST")
    db_name: str = os.getenv("DB_NAME")
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_port: str = os.getenv("DB_PORT")
    database_url: str = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    bucket_name: str = CommonConstants.BUCKET_NAME
    model_path: str = CommonConstants.MODEL_PATH


settings = Settings()