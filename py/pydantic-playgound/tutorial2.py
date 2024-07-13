from datetime import datetime
from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]  

"""
以下のコードにおいて、b'cheese' の b は、文字列リテラルのプレフィックスとして使用されています。
これは、文字列がバイト列として解釈されることを意味します。バイト列とは、文字列を構成する各バイトの値を直接表すものです。

Python では、文字列リテラルはシングルクォート (') またはダブルクォート (") で囲まれます。
しかし、文字列リテラルの前に b プレフィックスを付けると、文字列がバイト列として解釈されるようになります。
これは、文字列がエンコードされた形式 (例：UTF-8) でではなく、生のバイト列として扱われることを意味します。

この例では、b'cheese' は 'cheese' と同じ文字列を表しますが、b'cheese' はバイト列として解釈され、'cheese' は文字列として解釈されます
"""
external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}

user = User(**external_data)  
user.id = 1
print(user.id)  
#> 123

print(user.model_dump())  
"""
{
    'id': 123,
    'name': 'John Doe',
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
}
"""
