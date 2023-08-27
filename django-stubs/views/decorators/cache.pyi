from collections.abc import Callable
from typing import Any, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

def cache_page(
    timeout: float, *, cache: Any | None = ..., key_prefix: Any | None = ...
) -> Callable[[_F], _F]: ...
def cache_control(**kwargs: Any) -> Callable[[_F], _F]: ...
def never_cache(view_func: _F) -> _F: ...
