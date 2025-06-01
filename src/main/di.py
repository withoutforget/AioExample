from dishka import Provider, Scope, from_context

from src.config import Config


class DishkaProvider(Provider):
    _get_config = from_context(Config, scope=Scope.APP)
