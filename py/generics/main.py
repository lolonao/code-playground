def function[T](x: T, y: T) -> T:
    print(type(T))
    if type(x) is int and type(y) is int:
        return x + y
    x = T(0)


def main():
    result: int = function(x=1, y=2)
    print(result)

if __name__ == "__main__":
    main()
