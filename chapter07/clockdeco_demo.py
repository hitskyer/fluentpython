import time
from clockdeco import clock
@clock
def snooze(seconds):
	'''snooze'''
	time.sleep(seconds)
@clock
def factorial(n):
	return 1 if n < 2 else n*factorial(n-1)
@clock
def mine(a, b, c, name='xxj'):
	return "{}, {} and {} belong to name={}".format(a, b, c, name)
if __name__ == "__main__":
	print('*'*40, 'Calling snooze(.123)')
	snooze(.123)
	print('*'*40, 'Calling factorial(6)')
	factorial(6)
	print('*'*40, 'Calling mine(1,2,3, name="chanor")')
	mine(1,2,3, name="chanor")
