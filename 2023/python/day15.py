from collections import defaultdict
from functools import reduce

hash = lambda label: reduce(lambda cur, ch: (cur + ord(ch)) * 17 % 256, label, 0)

with open("input.txt") as f:
    labels = f.read().split(',')

def part2():
    boxes = defaultdict(dict)
    for label in labels:
        if '-' in label:
            boxes[hash(label[:-1])].pop(label[:-1], None)
        elif '=' in label:
            lens, focal = label.split('=')
            boxes[hash(lens)][lens] = int(focal)
    return sum((1+box) * (i+1) * focal for box in boxes for i, focal in enumerate(boxes[box].values()))

print(sum(hash(label) for label in labels), part2())