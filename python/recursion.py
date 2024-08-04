def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def sumn(n):
    if n==0:
        return 1
    return sumn(n-1)+n

def print1ton(n):
    if n==0:
        return 0
    print1ton(n-1)
    print(n)
    return

def printnton(n):
    if n==0:
        return 0
    print(n)
    printnton(n-1)
    return
 
def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=" ")
    fibonacci(n-1, b, a+b)


n= int(input())
# print(fact(n))
# print(sumn(n))
# print1ton(n)
# printnton(n)
print(fibonacci(n,0))