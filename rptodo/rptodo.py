from typing import NamedTuple, Dict, Any


class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int
