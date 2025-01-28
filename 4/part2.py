def is_xmas(center: str, tl: str, tr: str, bl: str, br: str):
    if center != 'A':
        return False
    if tl == 'M' and bl == 'M' and tr == 'S' and br == 'S':
        return True
    if tl == 'M' and bl == 'S' and tr == 'M' and br == 'S':
        return True
    if tl == 'S' and bl == 'S' and tr == 'M' and br == 'M':
        return True
    if tl == 'S' and bl == 'M' and tr == 'S' and br == 'M':
        return True
    return False


def solve(input: str):
    occurrences = 0
    lines = input.split('\n')

    for (i, line) in enumerate(lines[1:-1], start=1):
        for (j, char) in enumerate(line[1:-1], start=1):
            tl = lines[i - 1][j - 1]
            tr = lines[i - 1][j + 1]
            bl = lines[i + 1][j - 1]
            br = lines[i + 1][j + 1]
            if is_xmas(char, tl, tr, bl, br):
                occurrences += 1

    return occurrences

with open('input', 'r') as file:
    input = file.read();
    solution = solve(input.strip())
    print(f'solution: {solution}')
