class Solution:
    def __init__(self):
        self.input = []

    def read_input(self):
        with open('input.txt', 'r', encoding='utf-8') as fp:
            for line in fp:
                counts, char, password = line.split()
                minv, maxv = [int(n) for n in counts.split('-')]
                self.input.append({
                    'policy': {
                        'min': minv,
                        'max': maxv,
                        'char': char.replace(':', ''),
                    },
                    'password': password
                })

    def char_at(self, string, index, char):
        return string[index] == char

    def contains_count(self, row):
        policy = row['policy']
        count = row['password'].count(policy['char'])
        return policy['min'] <= count <= policy['max']

    def position_xor(self, row):
        policy = row['policy']
        first = self.char_at(row['password'], policy['min'] - 1, policy['char'])
        second = self.char_at(row['password'], policy['max'] - 1, policy['char'])
        return first ^ second

solution = Solution()
solution.read_input()

count = 0
for row in solution.input:
    if solution.contains_count(row):
        count += 1

print(f'Part 1: {count}')

count = 0
for row in solution.input:
    if solution.position_xor(row):
        count += 1

print(f'Part 2: {count}')
