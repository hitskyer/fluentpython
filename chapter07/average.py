def make_averager():
	series = []
	def averager(new_value):
		series.append(new_value)
		return sum(series)/len(series)
	return averager
def make_averager2():
	count = 0
	total = 0
	def average(new_value):
		count += 1
		total += new_value
		return total/count
	return average
def make_averager3():
	count = 0
	total = 0
	def average(new_value):
		nonlocal count, total
		count += 1
		total += new_value
		return total/count
	return average
