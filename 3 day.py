class Solution:
	def is_palindrome(self, n):
		s=str(n)
		if s ==s[::-1]:
		    return "Yes"
		else:
		    return "No"
