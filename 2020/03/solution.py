import math

class Solution:
    def __init__(self):
        self.input = []
        self.read_input()

    def read_input(self):
        with open('input.txt', 'r', encoding='utf-8') as fp:
          self.input = fp.read().splitlines()

    def count_trees_hit(self, directions):
        r, d = directions
        lines = enumerate(self.input[::d])
        trees_hit = [line for index, line in lines if line[index * r % len(line)] == '#']
        return len(trees_hit)

    def part_1(self):
        return self.count_trees_hit((3, 1))

    def part_2(self):
        to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        answers = map(self.count_trees_hit, to_check)
        return math.prod(answers)

solution = Solution()
print(f'Part 1: {solution.part_1()}')
print(f'Part 2: {solution.part_2()}')
