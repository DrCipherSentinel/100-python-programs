def is_palindrome(s):
	string=''.join(s.split()).lower()
	return string==string[ : :-1]

s=input("enter a string:")
if is_palindrome(s):
	print("entered string is a palindrome")
else:
	print("entered string is not a palindrome")
