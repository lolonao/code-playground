# [GitHub - kiorky/croniter](https://github.com/kiorky/croniter?tab=readme-ov-file#introduction)
from croniter import croniter
from datetime import datetime

base = datetime(2024, 7, 14, 16, 3)
iter = croniter('*/1 * * * *', base)  # every 5 minutes
print(iter.get_next(datetime))

numbers = [1, 1, 2, 2, 3, 3, 3]
unique = {num for num in numbers}
print(unique)
