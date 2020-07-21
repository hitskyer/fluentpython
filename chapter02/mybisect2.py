import bisect
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
	i = bisect.bisect_left(breakpoints, score)
	return grades[i]
print([(score, grade(score)) for score in [33, 99, 77, 70, 89, 90, 100]])
