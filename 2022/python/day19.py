import re, numpy

mkarr = lambda *a: numpy.array(a)
# convert the tuple of numpy arrays to tuple of tuples
# so we can sort
sort_key = lambda a: tuple(zip(*a))

def parse(line):
    id, ore_ore, clay_ore, oby_ore, oby_clay, geo_ore, geo_oby = map(int, re.findall(r'\d+', line))
    # cost and production of each robot in that order: geode, oby, clay, ore.
    # the last one in the list is the option of constructing none
    return (id, (mkarr(0, 0, 0, ore_ore), mkarr(0, 0, 0, 1)),     
               (mkarr(0, 0, 0, clay_ore), mkarr(0, 0, 1, 0)),     
               (mkarr(0, 0, oby_clay, oby_ore), mkarr(0, 1, 0, 0)),     
               (mkarr(0, geo_oby, 0, geo_ore), mkarr(1, 0, 0, 0)),     
               (mkarr(0, 0, 0, 0), mkarr(0, 0, 0, 0)))     

def calc(blueprint, time, cut):
    # what we have at the start
    todo = [(mkarr(0,0,0,0), mkarr(0,0,0,1))]
    for _ in range(time):
        # for the next minute
        next_todo = list()   
        # for each state in the queue                    
        for have, make in todo:
            for cost, more in blueprint:
                if all(have >= cost):        
                    next_todo.append((have+make-cost, make+more))
        # prune the queue to save time since its huge.
        # did some tests to find the ideal prune for each part
        # tests made by hand, prob wont be sufficient for all inputs
        todo = sorted(next_todo, key=sort_key, reverse=True)[:cut]
    return max(todo, key=sort_key)[0][0]

def sol():
    res1, res2 = 0, 1
    for i, *blueprint in map(parse, open('input.txt')):
        res1 += calc(blueprint, 24, 200) * i
        res2 *= calc(blueprint, 32, 8000) if i < 4 else 1
    return res1, res2

if __name__ == "__main__":
    print(sol())