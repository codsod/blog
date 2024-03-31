p = [1, 23, 4, 5]
while True:
    try:
        print(p.index(6))
    except ValueError:
        print("没有找到")
