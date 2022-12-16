import functools

@functools.lru_cache(maxsize=None) #128 by default
def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
print(fibonacci(2))
//
def fibonacci(n):
  fib = [0,1]
  for i in range(2,n+1):
    fib.append(fib[i-1] + fib[i-2])
  print(fib)
  return fib[n]
//
def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)