def reverse_string(user_input):
	rev = ""
	for ch in user_input:
		rev = ch + rev
	return rev
user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")
