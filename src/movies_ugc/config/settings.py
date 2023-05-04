import os
from pathlib import Path

from pydantic import BaseSettings, validator

BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR.parent
ROOT_DIR = SRC_DIR.parent


class BaseSettingsConfigMixin(BaseSettings):
    class Config:
        env_file = os.path.join(ROOT_DIR, ".env"), os.path.join(ROOT_DIR, ".env.local")
        env_file_encoding = "utf-8"


class AppSettings(BaseSettingsConfigMixin):
    APP_HOST: str
    APP_PORT: int
    ENVIRONMENT: str = "production"
    DEBUG: bool = False
    PROJECT_NAME: str = "UGC service"
    PROJECT_ID: str = "ugc_service"
    BASE_API_PREFIX: str = "api"
    API_V1_PREFIX: str = "v1"
    API_V2_PREFIX: str = "v2"

    @validator("DEBUG")
    def set_debug(cls, v, values):  # noqa
        return v and values["ENVIRONMENT"] == "development"


class CHSettings(BaseSettingsConfigMixin):
    CH_NODE_HOST: str = "localhost"
    CH_HTTP_PORT: int
    CH_NODE_PORT: int
    CH_CLUSTER_NAME: str
    CH_DB_MOVIES: str
    CH_MIGRATIONS_REPOSITORY_PATH: str = str(ROOT_DIR / "init_db" / "clickhouse")


class MongoSettings(BaseSettingsConfigMixin):
    MONGO_ROUTER_HOST: str
    MONGO_ROUTER_PORT: int
    MONGO_CONFIG_SERVER_HOST: str
    MONGO_CONFIG_SERVER_PORT: int
    MONGO_CLUSTER_CONFIG_PATH: str = str(ROOT_DIR / "init_db/mongo/cluster-config.json")
    MONGO_DB_MOVIES: str


class KafkaSettings(BaseSettingsConfigMixin):
    KAFKA_CONNECTION_HOST: str
    KAFKA_CONNECTION_PORT: int
    KAFKA_SCHEMA_REGISTRY_CONNECTION_HOST: str
    KAFKA_SCHEMA_REGISTRY_CONNECTION_PORT: int
    KAFKA_TOPIC_MOVIE_PLAYBACK_EVENT: str
    KAFKA_TOPIC_CURRENT_PLAYBACK_POSITION: str
    KAFKA_TOPIC_MOVIE_VIEWING: str
    KAFKA_SCHEMA_MOVIE_PLAYBACK_EVENT: str
    KAFKA_SCHEMA_CURRENT_PLAYBACK_POSITION: str
    KAFKA_SCHEMA_MOVIE_VIEWING: str
    KAFKA_MIGRATIONS_REPOSITORY_PATH: str = str(ROOT_DIR / "init_db" / "kafka")


app_settings: AppSettings = AppSettings()
ch_settings: CHSettings = CHSettings()
kafka_settings: KafkaSettings = KafkaSettings()
mongo_settings: MongoSettings = MongoSettings()
