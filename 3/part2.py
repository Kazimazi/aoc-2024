import re

def solve(line: str, should_do: bool):
    def mul(a, b):
        return a * b

    cleaned_line = line.strip()

    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", cleaned_line)
    # print(f'instructions: {instructions}')
        
    result = 0
    for instruction in instructions:
        if instruction == "don't()":
            should_do = False
        elif instruction == 'do()':
            should_do = True
        else:
            if should_do:
                mult = eval(instruction)
                result += mult
    # print(f'result for line {result}')
    return (result, should_do)

with open('input', 'r') as file:
    result = 0
    should_do = True
    for line in file:
        line_result, should_do = solve(line, should_do)
        result += line_result
    print(result)
