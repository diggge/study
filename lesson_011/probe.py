# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers

class PrimeNumbers:
    def __init__(self,n):
        self.i, self.j,  self.n = 1, 1, n
    def __iter__(self):
        self.i, self.j = 1, 1
        return self
    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            for self.j in range(2, self.i):
                if self.i % self.j == 0:
                    break
                else:
                    return self.i
prime_number_iterator = PrimeNumbers(n=10000)
print(prime_number_iterator)
# for number in prime_number_iterator:
#     if number is not None:
#         print(number)