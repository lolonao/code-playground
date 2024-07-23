"""Pydantic は、そのまますぐにmypyと連携して動作します。

ただし、Pydantic には、コードの型チェック機能を向上させる重要な pydantic 固有の機能がいくつか mypy に追加される mypy プラグインも付属しています。

たとえば、次のスクリプトを考えてみましょう
"""
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Model(BaseModel):
    age: int
    first_name: str = 'John'
    last_name: Optional[str] = None
    signup_ts: Optional[datetime] = None
    list_of_ints: List[int]


# m = Model(age=42, list_of_ints=[1, '2', b'3'])
m = Model(age=42, list_of_ints=[1, 2, 3])
print(m.last_name)  # not a model field!

Model(age=42, list_of_ints=[1, 2, 3])
# Model()  # will raise a validation error for age and list_of_ints


"""
特別な設定を行わないと、mypy は欠落しているモデル フィールド アノテーションをキャッチせず、 list_of_intsPydantic が正しく解析する引数について警告します。

プラグインを有効にする¶
プラグインを有効にするには、mypy 構成ファイルpydantic.mypyのプラグインのリストに を 追加するだけです ( 、、 のいずれかに なります)。mypy.inipyproject.tomlsetup.cfg

mypy.iniファイルに以下を作成するだけです。

[mypy]
plugins = pydantic.mypy

"""

