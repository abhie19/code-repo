import unittest

def fibonacci(n):
	if n == 0 or n == 1: return 0
	elif n == 2: return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return n * factorial(n - 1)
	
class TestFib(unittest.TestCase):
	def test_fibonacci(self):
		self.assertEqual(fibonacci(9), 21)
	
	def test_fact(self):
		self.assertEqual(factorial(4), 23)

if __name__ == '__main__':
	unittest.main()
