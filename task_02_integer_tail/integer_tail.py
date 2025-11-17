def integer_tail(n):
    result = []
    for num in range(1, n + 1):
        result.append(str(num))

    return "".join(result)


n = int(input())
print(integer_tail(n))
