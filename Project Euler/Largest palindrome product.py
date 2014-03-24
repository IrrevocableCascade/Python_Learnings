__author__ = 'Irrevocable Cascade'

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

def is_palindrome(number):
	reverse = str(number)[::-1]
	if str(number) == reverse:
		return True
	return False

a = 111
b = 111
p = 0
palindromes = []

while a <= 999:
	while b <= 999:
		p = a * b
		if is_palindrome(p):
			#print('Palindrome found: {0}. a = {1} b = {2}'.format(p,a,b))
			palindromes.append((p))
		b += 1
	b = 111
	a += 1

print(sorted(set(palindromes)))
