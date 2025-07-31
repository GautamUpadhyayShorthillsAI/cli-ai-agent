def prime_seive(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes

print(prime_seive(100))