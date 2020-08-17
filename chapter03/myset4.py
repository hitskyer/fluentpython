import time
import random
import timeit
haystackDict = {}
while len(haystackDict) < 1000*1000*10:
	haystackDict[random.random()] = 1
haystackSet = set(haystackDict)
haystackList = list(haystackSet)
needleDict = {i:1 for i in random.sample(haystackList, 500)}
while len(needleDict) < 1000:
	needleDict[random.random()] = 1
needles = list(needleDict.keys())

haystackDict_1k = {i:1 for i in random.sample(list(haystackDict), 1000)}
haystackDict_10k = {i:1 for i in random.sample(list(haystackDict), 1000*10)}
haystackDict_100k = {i:1 for i in random.sample(list(haystackDict), 1000*100)}
haystackDict_1m = {i:1 for i in random.sample(list(haystackDict), 1000*1000)}
haystackDict_10m = {i:1 for i in random.sample(list(haystackDict), 1000*1000*10)}

haystackSet_1k = {i for i in random.sample(haystackSet, 1000)}
haystackSet_10k = {i for i in random.sample(haystackSet, 1000*10)}
haystackSet_100k = {i for i in random.sample(haystackSet, 1000*100)}
haystackSet_1m = {i for i in random.sample(haystackSet, 1000*1000)}
haystackSet_10m = {i for i in random.sample(haystackSet, 1000*1000*10)}

haystackList_1k = random.sample(haystackList, 1000)
haystackList_10k = random.sample(haystackList, 1000*10)
haystackList_100k = random.sample(haystackList, 1000*100)
haystackList_1m = random.sample(haystackList, 1000*1000)
haystackList_10m = random.sample(haystackList, 1000*1000*10)

def test1():
	found = 0
	for f in needles:
		if f in haystackDict_1k:
			found += 1
def test2():
	found = 0
	for f in needles:
		if f in haystackDict_10k:
			found += 1
def test3():
	found = 0
	for f in needles:
		if f in haystackDict_100k:
			found += 1
def test4():
	found = 0
	for f in needles:
		if f in haystackDict_1m:
			found += 1
def test5():
	found = 0
	for f in needles:
		if f in haystackDict_10m:
			found += 1
def test6():
	found = 0
	for f in needles:
		if f in haystackSet_1k:
			found += 1
def test7():
	found = 0
	for f in needles:
		if f in haystackSet_10k:
			found += 1
def test8():
	found = 0
	for f in needles:
		if f in haystackSet_100k:
			found += 1
def test9():
	found = 0
	for f in needles:
		if f in haystackSet_1m:
			found += 1
def test10():
	found = 0
	for f in needles:
		if f in haystackSet_10m:
			found += 1
def test11():
	found = len(set(needles) & haystackSet_1k)
def test12():
	found = len(set(needles) & haystackSet_10k)
def test13():
	found = len(set(needles) & haystackSet_100k)
def test14():
	found = len(set(needles) & haystackSet_1m)
def test15():
	found = len(set(needles) & haystackSet_10m)
def test16():
	found = 0
	for f in needles:
		if f in haystackList_1k:
			found += 1
def test17():
	found = 0
	for f in needles:
		if f in haystackList_10k:
			found += 1
def test18():
	found = 0
	for f in needles:
		if f in haystackList_100k:
			found += 1
def test19():
	found = 0
	for f in needles:
		if f in haystackList_1m:
			found += 1
def test20():
	found = 0
	for f in needles:
		if f in haystackList_10m:
			found += 1
print("dict")
print(timeit.timeit(stmt=test1,setup="from __main__ import test1",number=1))
print(timeit.timeit(stmt=test2,setup="from __main__ import test2",number=1))
print(timeit.timeit(stmt=test3,setup="from __main__ import test3",number=1))
print(timeit.timeit(stmt=test4,setup="from __main__ import test4",number=1))
print(timeit.timeit(stmt=test5,setup="from __main__ import test5",number=1))
print("set")
print(timeit.timeit(stmt=test6,setup="from __main__ import test6",number=1))
print(timeit.timeit(stmt=test7,setup="from __main__ import test7",number=1))
print(timeit.timeit(stmt=test8,setup="from __main__ import test8",number=1))
print(timeit.timeit(stmt=test9,setup="from __main__ import test9",number=1))
print(timeit.timeit(stmt=test10,setup="from __main__ import test10",number=1))
print("&set")
print(timeit.timeit(stmt=test11,setup="from __main__ import test11",number=1))
print(timeit.timeit(stmt=test12,setup="from __main__ import test12",number=1))
print(timeit.timeit(stmt=test13,setup="from __main__ import test13",number=1))
print(timeit.timeit(stmt=test14,setup="from __main__ import test14",number=1))
print(timeit.timeit(stmt=test15,setup="from __main__ import test15",number=1))
print("list")
print(timeit.timeit(stmt=test16,setup="from __main__ import test16",number=1))
print(timeit.timeit(stmt=test17,setup="from __main__ import test17",number=1))
print(timeit.timeit(stmt=test18,setup="from __main__ import test18",number=1))
print(timeit.timeit(stmt=test19,setup="from __main__ import test19",number=1))
print(timeit.timeit(stmt=test20,setup="from __main__ import test20",number=1))
