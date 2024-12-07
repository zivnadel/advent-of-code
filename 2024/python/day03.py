import re

mul_pattern, control_pattern = r"mul\((\d{1,3}),(\d{1,3})\)", r"(do|don't)\(\)"

print(sum(int(x[0]) * int(x[1]) for x in re.findall(mul_pattern, open("input.txt").read())))

tokens = re.finditer(fr"{mul_pattern}|{control_pattern}", open("input.txt").read())
valid, mul_enabled = [], True

for token in tokens:
    token = token.group()
    if re.fullmatch(control_pattern, token):
        mul_enabled = token == "do()"
    elif mul_enabled and re.fullmatch(mul_pattern, token):
        valid.append(re.findall(mul_pattern, token)[0])

print(sum(int(x[0]) * int(x[1]) for x in valid))