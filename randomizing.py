import random

with open('data.txt', 'w') as f:
    for _ in range(10000000):
        f.write(f"{random.randint(1, 10000)}\n")
