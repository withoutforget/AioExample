from typing import Protocol


class Usecase(Protocol):
    async def __call__(self, *args, **kwargs):
        raise NotImplementedError
