import time

def main():
    now = time.localtime()
    print("現在時刻は {}-{}-{} {}:{}:{}".format(
        now[0], now[1], now[2], now[3], now[4], now[5]))

if __name__ == "__main__":
    main()

