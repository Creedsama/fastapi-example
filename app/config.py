from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_password: str = "testing123"
    database_name: str = "fastapi"
    database_username: str = "vakul"
    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm: str = "HS256"
    acess_token_expire_in_minutes: int = 10

    class Config:
        env_file = ".env"


settings = Settings()
