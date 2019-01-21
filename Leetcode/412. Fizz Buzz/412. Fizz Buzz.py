    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = list(range(1, n+1))
        for idx, value in enumerate(nums):
            if not value%15:
                nums[idx] = "FizzBuzz"
            elif not value%5:
                nums[idx] = "Buzz"
            elif not value%3:
                nums[idx] = "Fizz"
            else:
                nums[idx] = str(value)
        return nums