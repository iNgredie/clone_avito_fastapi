from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    # database_url: str = 'sqlite:///./db.sqlite3'
    database_url: str = 'postgresql://postgres:passwordtest@localhost:5432/avito'
    # jwt_secret: str = 'SSmzYFXG-GmMgv6M2Pm6CH5QHa-ZdXxSrTpQ8H-4xJc' # example
    jwt_secret: str = 'SSmzYFXG-GmMgv6M2Pm6CH5QHa-ZdXxSrTpQ8H-4xJc'
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
