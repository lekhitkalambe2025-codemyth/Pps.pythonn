m1, m2, m3, m4 = map(int, input().split())

total = m1 + m2 + m3 + m4

aggregate = total / 4

print(total)

print(f"{aggregate:.2f}")

if aggregate > 75:
    print("Distinction")
elif aggregate >= 60:
    print("First Division")
elif aggregate >= 50:
    print("Second Division")
elif aggregate >= 40:
    print("Third Division")
else:
    print("Fail")


