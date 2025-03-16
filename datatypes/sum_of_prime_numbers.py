limit = 2000000
primes = [True] * (limit + 1)
primes[0] = primes[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, limit + 1, i):
            primes[j] = False

prime_sum = sum(i for i, prime in enumerate(primes) if prime)
print(f"Sum: {prime_sum}")
