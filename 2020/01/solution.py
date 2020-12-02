from itertools import combinations

class Solution:
    def __init__(self):
        self.numbers = []

    def read_input(self):
        with open('input.txt', 'r', encoding='utf-8') as fp:
            input = fp.read().split('\n')
            self.numbers = [int(n) for n in input if n]
 
    def sumto(self, target, count):
        return (combo for combo in combinations(self.numbers, count) if sum(combo) == target)

solution = Solution()
solution.read_input()

twosum = solution.sumto(2020, 2)
threesum = solution.sumto(2020, 3)

print(f'Part 1: {next(twosum)}')
print(f'Part 2: {next(threesum)}')
