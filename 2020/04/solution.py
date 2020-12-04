import re

class Solution:
    def __init__(self):
        self.input = []
        self.read_input()

    def read_input(self):
        with open('input.txt', 'r', encoding='utf-8') as fp:
            passports = fp.read().split('\n\n')
            for passport in passports:
                self.input.append(dict(pair.split(':') for pair in passport.split()))

    def part_1(self):
        valid = [pp for pp in self.input if (len(pp) == 8) or (len(pp) == 7 and 'cid' not in pp)]
        return valid

    def part_2(self):
        valid = 0
        for pp in self.part_1():
            try:
                byr = int(pp['byr'])
                iyr = int(pp['iyr'])
                eyr = int(pp['eyr'])
                pid = int(pp['pid'])
                hgt = pp['hgt']
                hcl = pp['hcl']
                ecl = pp['ecl']
                pid = pp['pid']
            except ValueError as err:
                continue

            if len(str(byr)) != 4 or byr < 1920 or byr > 2002:
                continue
            if len(str(iyr)) != 4 or iyr < 2010 or iyr > 2020:
                continue
            if len(str(eyr)) != 4 or eyr < 2020 or eyr > 2030:
                continue
            if not (hgt.endswith('cm') or hgt.endswith('in')):
                continue
            
            hgt_v = int(hgt[:-2])
            
            if hgt.endswith('cm') and (hgt_v < 150 or hgt_v > 193):
                continue
            if hgt.endswith('in') and (hgt_v < 59 or hgt_v > 76):
                continue
            if not re.match(r'#[0-9a-f]{6}$', hcl):
                continue
            if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue
            if not re.match('[0-9]{9}$', pid):
                continue
            
            valid += 1
            
        return valid

solution = Solution()
print(f'Part 1: {len(solution.part_1())}')
print(f'Part 2: {solution.part_2()}')
