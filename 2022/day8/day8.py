from itertools import product, chain, takewhile


forest = []
with open('/home/kunnu/Documents/Python/aoc/2022/day8/input.txt', 'r') as f:
    for line in f.readlines():
        row = [int(t) for t in line.strip('\n')]
        forest.append(row)

n_rows = len(forest)
n_cols = len(forest[0])

border_trees = [(i, j) for i, j in chain(
    product(range(0, n_rows), [0, n_cols-1]),
    product([0, n_rows-1], range(1, n_cols-1)))]

def check_visible(forest: list, pos: tuple):
    r, c = pos
    if pos in border_trees:
        return True
    else:
        height = forest[r][c]
        vis_row = height > max(forest[r][c+1:]) or height > max(forest[r][:c])
        vis_col = (height > max([forest[i][c] for i in range(0, r)]) or
                   height > max([forest[i][c] for i in range(r+1, n_rows)]))
        if vis_row or vis_col:
            return True
        else:
            return False


ans_1 = [check_visible(forest, pos) for pos in product(range(n_rows), range(n_cols))].count(True)
print(ans_1)


def count_stop(lst: list, ht: int):
    """
    Count number of trees whose height is less than given height, stop when equal height
    :param lst: list of integers
    :param ht: height
    :return: generator object
    """
    for x in lst:
        if x < ht:
            yield x
        elif x >= ht:
            yield x
            break



# Answer 2
def scenic_score(forest: list, pos: tuple):
    r, c = pos
    if pos in border_trees:
        return 0
    height = forest[r][c]

    # calculate scores
    up = len(list(count_stop([forest[i][c] for i in range(r-1, -1, -1)], height)))
    down = len(list(count_stop([forest[i][c] for i in range(r+1, n_rows)], height)))
    left = len(list(count_stop(forest[r][c-1::-1], height)))
    right = len(list(count_stop(forest[r][c+1:], height)))
    return up * down * left * right

ans_2 = max([scenic_score(forest, pos) for pos in product(range(n_rows), range(n_cols))])
print(ans_2)