import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 40
start = time.time()
result = fib(n)
end = time.time()

print(f"Fibonacci({n}) = {result}")
print("Tiempo en Python:", end - start, "segundos")
