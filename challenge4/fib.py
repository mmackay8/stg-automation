class Fib:
    def fib(self, num):
        a, b = 1, 1
        for i in range(num - 1):
            a,b = b, a+b
        return a

