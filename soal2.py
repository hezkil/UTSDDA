import time

def read_file(filename):
    with open(filename, 'r') as f:
        result = []
        for line in f:
            line = line.strip()
            line = line.replace(',', ' ')
            for token in line.split():
                try:
                    result.append(int(token))
                except ValueError:
                    continue
        return result
    

def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

start_time = time.time()
print(start_time)

filename = 'data.txt'
numbers = read_file(filename)
median = find_median(numbers)
print(median)

end_time = time.time()
print(end_time)
print(end_time - start_time)
