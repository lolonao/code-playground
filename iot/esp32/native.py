import micropython


class NativeObj:
    def __init__(self):
        self.name = "native"
        self.linebuf = ""

    @micropython.native
    def foo(self, arg):
        buf = self.linebuf  # Cached object
        print(f"Cashed object: {buf}")
        for i in range(10000):
            print(i)


if __name__ == "__main__":
    nativeobj = NativeObj()
    nativeobj.foo("hoge")

