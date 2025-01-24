safe_counter = 0

def solve_report(report):
    trend = None
    for n in range(0, len(report) - 1):
        a, b = report[n:n + 2]
        if not trend:
            if a > b:
                trend = -1
            else:
                trend = 1
        diff = b - a
        if trend == 1 and not 1 <= diff <= 3:
            return False
        elif trend == -1 and not -3 <= diff <= -1:
            return False
        if n == len(report) - 2:
            return True

def solve_line(line):
    report = list(map(int, line.strip().split(' ')))
    return solve_report(report)

with open('input', 'r') as file:
    for line in file:
        if solve_line(line):
            safe_counter += 1

print(f'safe counter: {safe_counter}')
