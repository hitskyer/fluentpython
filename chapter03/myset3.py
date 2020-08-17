import time

start = time.time()
big1   = {i for i in range(1000*1000*10)}
print(time.time()-start)

start = time.time()
big2   = set([i for i in range(1000*1000*10)])
print(time.time()-start)
