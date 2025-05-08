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

def min_contiguous_subsequence_sum(arr):

    min_sum = float('inf')
    current_sum = 0

    for num in arr:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum > 0:
            current_sum = 0

    return min_sum

start_time = time.time()
print(start_time)

file_path = 'data.txt'
data = read_file(file_path)
result = min_contiguous_subsequence_sum(data)
print(result)

end_time = time.time()
print(end_time)
print(end_time - start_time)