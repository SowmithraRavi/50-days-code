class Solution:
    def nthFibonacci(self, n : int) -> int:
        MOD = 1000000007
        def fib(n):
            a, b = 0, 1
            for i in range(n):
                a, b = b, (a + b) % MOD
            return a

        return fib(n)
