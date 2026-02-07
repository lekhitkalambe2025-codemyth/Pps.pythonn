import math

a, b, c = map(int, input().split())

D = b*b - 4*a*c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("root1 = {:.2f}".format(root1))
    print("root2 = {:.2f}".format(root2))

elif D == 0:
    root1 = -b / (2*a)
    print("root1 = root2 = {:.2f}".format(root1))

else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print("root1 = {:.2f}+{:.2f}i".format(real, imag))
    print("root2 = {:.2f}-{:.2f}i".format(real, imag))
