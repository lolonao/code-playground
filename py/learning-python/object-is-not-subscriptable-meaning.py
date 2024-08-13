"""
Pythonにおける "Object is Not Subscriptable "の本当の意味とは？
[What Does "Object is Not Subscriptable" Really Mean In Python? - YouTube](https://www.youtube.com/watch?v=csmBFpixw0A)
#learning
"""

def get_data(connected: bool = True) -> dict[str, int] | None:
    return {'a': 1, 'b': 2} if connected else None

def __getitem__(self, item: int) -> int:
    return self.numbers[item]

def __setitem__(self, key, value):
    ...

def __delitem__(self, key):
    ...

def main() -> None:
    data: dict[str, int] | None = get_data(connected=False)
    print(data)
    if data is not None:
        print(data['a'])
        print(data['b'])
    else:
        print('No data...')
    # result = get_data()
    # print(result)

if __name__ == '__main__':
    main()

