{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3a88d9c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the limit to search for prime numbers: 1000\n",
      "Total prime numbers found up to 1000: 168\n",
      "Prime numbers found: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]\n"
     ]
    }
   ],
   "source": [
    "def sieve_of_atkin(limit):\n",
    "    is_prime = [False] * (limit + 1)  # Create a list of flags for prime numbers.\n",
    "    sqrt_limit = int(limit ** 0.5) + 1  # Calculate the square root of the limit.\n",
    "\n",
    "    # Mark 2 and 3 as primes\n",
    "    is_prime[2] = True\n",
    "    is_prime[3] = True\n",
    "\n",
    "    # Apply the Atkin sieve algorithm to identify prime numbers.\n",
    "    for x in range(1, sqrt_limit):\n",
    "        for y in range(1, sqrt_limit):\n",
    "            n = 4 * x**2 + y**2\n",
    "            if n <= limit and (n % 12 == 1 or n % 12 == 5):\n",
    "                is_prime[n] = not is_prime[n]\n",
    "\n",
    "            n = 3 * x**2 + y**2\n",
    "            if n <= limit and n % 12 == 7:\n",
    "                is_prime[n] = not is_prime[n]\n",
    "\n",
    "            n = 3 * x**2 - y**2\n",
    "            if x > y:\n",
    "                if n <= limit and n % 12 == 11:\n",
    "                    is_prime[n] = not is_prime[n]\n",
    "\n",
    "    # Unmark square of prime numbers\n",
    "    for i in range(5, sqrt_limit):\n",
    "        if is_prime[i]:\n",
    "            for j in range(i**2, limit + 1, i**2):\n",
    "                is_prime[j] = False\n",
    "\n",
    "    # Count prime numbers and build the prime vector\n",
    "    prime_count = 0\n",
    "    prime_numbers = []\n",
    "    for i in range(2, limit + 1):\n",
    "        if is_prime[i]:\n",
    "            prime_count += 1\n",
    "            prime_numbers.append(i)\n",
    "\n",
    "    return prime_count, prime_numbers\n",
    "\n",
    "# Example of usage\n",
    "limit = int(input(\"Enter the limit to search for prime numbers: \"))\n",
    "count, primes = sieve_of_atkin(limit)\n",
    "print(f\"Total prime numbers found up to {limit}: {count}\")\n",
    "print(\"Prime numbers found:\", primes)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19ead20c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
