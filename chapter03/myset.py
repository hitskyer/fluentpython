import time

small = {i for i in range(1000)}
big   = {i for i in range(1000*1000*10)}
start = time.time()
common1 = small&big
print(time.time()-start)

start = time.time()
common2 = {i for i in small if i in big}
print(time.time()-start)

start = time.time()
common3 = set()
for i in small:
	if i in big:
		common3.add(i)
print(time.time()-start)
