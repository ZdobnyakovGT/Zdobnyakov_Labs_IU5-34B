data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

print(sorted(data, key=abs, reverse=True))
print(sorted(data, key=lambda n: abs(n), reverse=True))