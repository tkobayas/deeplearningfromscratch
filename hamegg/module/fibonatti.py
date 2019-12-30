def fibo(n):
    result = []
    num1 = 1
    num2 = 1

    while num1 < n:
        result.append(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return result

if __name__ == "__main__":
    print("{0}".format(fibo(100)))
    