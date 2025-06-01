from dishka import Provider, Scope, provide_all

from src.usecases.start_command import StartCommandUsecase


class UsecaseProvider(Provider):
    _get_usecase = provide_all(StartCommandUsecase, scope=Scope.REQUEST)
