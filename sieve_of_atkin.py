def sieve_of_atkin(limit):
    is_prime = [False] * (limit + 1)  # Create a list of flags for prime numbers.
    sqrt_limit = int(limit ** 0.5) + 1  # Calculate the square root of the limit.

    # Mark 2 and 3 as primes
    is_prime[2] = True
    is_prime[3] = True

    # Apply the Atkin sieve algorithm to identify prime numbers.
    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]

            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                is_prime[n] = not is_prime[n]

            n = 3 * x**2 - y**2
            if x > y:
                if n <= limit and n % 12 == 11:
                    is_prime[n] = not is_prime[n]

    # Unmark square of prime numbers
    for i in range(5, sqrt_limit):
        if is_prime[i]:
            for j in range(i**2, limit + 1, i**2):
                is_prime[j] = False

    # Count prime numbers and build the prime vector
    prime_count = 0
    prime_numbers = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            prime_count += 1
            prime_numbers.append(i)

    return prime_count, prime_numbers

# Example of usage
limit = int(input("Enter the limit to search for prime numbers: "))
count, primes = sieve_of_atkin(limit)
print(f"Total prime numbers found up to {limit}: {count}")
print("Prime numbers found:", primes)

