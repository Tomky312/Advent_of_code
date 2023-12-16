from __future__ import annotations

lines = []
line = "1mhggggg3"
lines.append(line)

def get_digits(line):
    numbers = []
    for symbol in line:
        if symbol.isnumeric():
            numbers.append(symbol)

    return numbers

num = get_digits(line)
print(num)



