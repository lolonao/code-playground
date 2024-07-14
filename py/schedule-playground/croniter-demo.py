# [GitHub - kiorky/croniter](https://github.com/kiorky/croniter?tab=readme-ov-file#introduction)
from croniter import croniter
from datetime import datetime

base = datetime(2024, 7, 14, 16, 3)
iter = croniter('*/5 * * * *', base)  # every 5 minutes
print(iter.get_next(datetime))

