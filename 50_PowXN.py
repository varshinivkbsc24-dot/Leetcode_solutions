class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative power
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:      
                result *= x
            x *= x              
            n //= 2             

        return result

if __name__ == "__main__":
    sol = Solution()

    print("Example 1:", sol.myPow(2.00000, 10))   
    print("Example 2:", sol.myPow(2.10000, 3))    
    print("Example 3:", sol.myPow(2.00000, -2))   
