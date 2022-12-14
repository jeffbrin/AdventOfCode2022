for x in range(1, 10000):
    if 1501 // x % 23 == 0 and 1862 // x % 23 == 0 and 60 // x % 19 == 0 and 71 // x % 19 == 0 and 80 // x % 19 == 0 and 81 // x % 19 == 0 and 6241 // x % 13 == 0 and 3600 // x % 13 == 0 and 9409 // x % 13 == 0:
        print(x)