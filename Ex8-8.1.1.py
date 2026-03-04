n = int(input("dimension: "))

print("first matrix:")
A = []
for i in range(n):
	row = list(map(int, input().split()))
	A.append(row)

print("second matrix:")
B = []
for i in range(n):
	row = list(map(int, input().split()))
	B.append(row)

C = [[0]*n for _ in range(n)]

for i in range(n):
	for j in range(n):
		for k in range(n):
			C[i][j] += A[i][k] * B[k][j]

print("Resultant Matrix:")
for i in range(n):
	print(*C[i])
