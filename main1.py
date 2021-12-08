# Написать метод возведения числа а в степень b
# Решить уравнение f(x) = x^y + b


def pow(a, n):

    res = 1 # 2 ^ 4
    for i in range(n):
        res = res * a
    return res





x = int(input("Enter x: "))
y = int(input("Enter y: "))
b = int(input("Enter b: "))
res = pow(x, y) + b


print(res)