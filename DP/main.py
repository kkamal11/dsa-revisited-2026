import time
class Solutiion:
    def fib(self,n):
        if n<= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    
    def fibdp(self, n, dp = {}):
        if n in dp:
            return dp[n]
        
        if n <= 1:
            return n
        
        dp[n] = self.fibdp(n-1, dp) + self.fibdp(n-2, dp)

        return dp[n]


    def fib_opt(self, n):
        if n<= 1:
            return n
        a, b = 0, 1

        for i in range(2, n+1):
            a, b = b, a + b
        
        return b


if __name__ == "__main__":
    s = Solutiion()
    s1 = time.perf_counter()
    # print(s.fib(40))
    s2 = time.perf_counter()
    print(f"Time taken by recursive approach: {s2-s1:.6f} seconds")
    s3 = time.perf_counter()
    print(s.fibdp(4))
    s4 = time.perf_counter()
    print(f"Time taken by dp approach: {(s4-s3):.6f} seconds")
    print("opt ",s.fib_opt(4))