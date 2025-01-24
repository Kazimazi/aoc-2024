import re

def solve(line: str):
    cleaned_line = line.strip()
    parsed = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', cleaned_line)
    result = 0
    for a, b in parsed:
        result += int(a) * int(b)
    return result

with open('input', 'r') as file:
    result = 0
    for line in file:
        result += solve(line)
    print(result)
