st = input()
result = ""
for ch in st:

	if ch.isalnum() or ch == " ":
		result += ch

print(result)

