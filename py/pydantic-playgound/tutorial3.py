"""
Pydanticを使用する理由
例） - ヒントを入力するだけ

https://docs.pydantic.dev/latest/why/#strict-lax
"""

from typing import Annotated, Dict, List, Literal, Tuple

from annotated_types import Gt
from pydantic import BaseModel


class Fruit(BaseModel):
    name: str
    color: Literal["red", "gren"]
    weight: Annotated[float, Gt(0)]
    bazam: Dict[str, List[Tuple[int, bool, float]]]


fruit = Fruit(name="Apple", color="red", weight=4.2, bazam={"foobar": [(1, True, 0.1)]})

print(fruit)

# name='Apple' color='red' weight=4.2 bazam={'foobar': [(1, True, 0.1)]}
