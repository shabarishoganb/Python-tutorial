print([x for x in range(100, 1000) if sum(map(int, str(x))) % 9 == 0])
