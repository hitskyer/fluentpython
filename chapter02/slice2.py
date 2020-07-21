mylist = list(range(10))
print(mylist)
mylist[2:5] = [20, 30]
print(mylist)
del mylist[5:7]
print(mylist)
mylist[3::2] = [11, 22]
print(mylist)
mylist[2:5] = [100]
print(mylist)
