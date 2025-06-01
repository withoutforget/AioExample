import os
from dataclasses import dataclass, field

from adaptix import Retort
from dynaconf import Dynaconf


@dataclass(slots=True)
class BotConfig:
    api_key: str
    version: str


@dataclass(slots=True)
class LoggingConfig:
    level: str
    human_readable_logs: bool = field(default=True)


@dataclass(slots=True)
class Config:
    bot: BotConfig
    logging: LoggingConfig


def get_config() -> Config:
    dyna = Dynaconf(
        settings_files=[os.getenv("CONFIG_FILE", "../config.toml")],
        envvar_prefix="BOT",
        load_dotenv=True,
        environments=True,
        default_env="default",
        merge_enabled=True,
        env_switcher="BOT_ENV",
    )
    return Retort().load(dyna, Config)


config: Config = get_config()
