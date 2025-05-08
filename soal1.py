import time

def f(x, dict):
    if x == 0:
        return 3  
    elif x == 1:
        return 5 
    
    if x in dict: 
        return dict[x]
    
    result = (f(x-2, dict)**2.5 - 8) * (f(x-1, dict) - 9)
    dict[x] = result
    return result

x_value = 2
start_time = time.time()
print(start_time)

dict = {}
result = f(x_value, dict)
print(result)

end_time = time.time()
print(end_time)
print(end_time - start_time)