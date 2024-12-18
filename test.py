def fibo(n):
    a,b = 0,1
    result=[]
    for i in range(n+1):
        result.append(b)
        a,b = b, a+b
    return result


result = fibo(5)
print(result)