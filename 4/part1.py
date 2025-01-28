import re

XMAS = "XMAS"

def find_xmas(string: str):
    matches = re.findall(XMAS, string)
    return len(matches)

def transpose(lines: list[str]):
    characters_of_lines_iter = map(list, lines)
    zipped_chars_iter: zip[str] = zip(*characters_of_lines_iter)
    transposed_characters_iter = map(list, zipped_chars_iter)
    transposed_lines = list(map(lambda cs: ''.join(cs), transposed_characters_iter))
    return list(transposed_lines)

def diagonals(lines: list[str]):
    characters_in_diagonals: list[list[str]] = []
    for i, line in enumerate(lines):
        for j, character in enumerate(line):
            if len(characters_in_diagonals) <= i + j:
                characters_in_diagonals.append([])
            characters_in_diagonals[j + i].append(character)
    diagonal_lines = list(map(lambda cs: ''.join(cs), characters_in_diagonals))
    return diagonal_lines

def solve_line(line: str):
    return find_xmas(line) + find_xmas(line[::-1])

def solve(input: str):
    occurrences = 0
    lines = input.split('\n')
    for line in lines:
        occurrences += solve_line(line)

    transposed_lines = transpose(lines)
    for line in transposed_lines:
        occurrences += solve_line(line)

    diagonal_lines = diagonals(lines)
    for line in diagonal_lines:
        occurrences += solve_line(line)

    reversed_lines = list(map(lambda line: line[::-1], lines))
    diagonal_reversed_lines = diagonals(reversed_lines)
    for line in diagonal_reversed_lines:
        occurrences += solve_line(line)

    return occurrences

with open('input', 'r') as file:
    input = file.read();
    solution = solve(input.strip())
    print(f'solution: {solution}')
