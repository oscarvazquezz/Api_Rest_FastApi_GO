from decouple import config

class Settings:
    DATABASE_PORT: int = config("DATABASE_PORT")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD")
    POSTGRES_USER: str = config("POSTGRES_USER")
    POSTGRES_DB: str = config("POSTGRES_DB")
    POSTGRES_HOST: str = config("POSTGRES_HOST")


settings = Settings()