"""
basic types of python
"""

number: int = 10
decimal: float = 2.5
text: str = 'Hello'
active: bool = False

names: list = ['Bob', 'Anna', 'Luigi']
coordinates: tuple = (1.5, 2.5)
unique: set = {1, 2, 3, 3}
data: dict = {'name': 'Bob', 'age': 20}

dictlist: list = [data]

print("dictlist", dictlist)

print('---')

import pprint as pp
pp.pprint(dictlist[0])

###############################

name: str = 'Bob'
age: int = 20
age = 'hoge'
print(age)
print('変数ageは、int型であるにも関わらず、文字列を代入でき、しかも表示もできてしまう。')
print('つまり、エディタ上のチェックは働いても、実際には代入できてしまうということ。')

###

from typing import Final
VERSION: Final[str] = '1.0.12'  # 以降代入できない
VERSION = 'hoge2'
print(VERSION)

##########################

from datetime import datetime

print('This is the current time:')
print(datetime.now())




