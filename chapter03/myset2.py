import time

small = {i:1 for i in range(1000)}
big   = {i for i in range(1000*1000*10)}
start = time.time()
found = len(set(small) & set(big))
print(time.time()-start)

start = time.time()
found = set(small).intersection(big)
print(time.time()-start)
