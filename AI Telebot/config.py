from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    bot_token = SecretStr

    model_config = SettingsConfigDict(env_file='token.env', env_file_encoding='utf-8')

confif = Settings()