from enum import IntEnum
import pandas as pd


df = pd.read_csv('day2/input.txt', header=None)
df = df[0].str.split(' ')

# Points matrix, indexed by Player two RPS, columns Player One RPS
rps_table = [
    [4, 1, 7],
    [8, 5, 2],
    [3, 9, 6]
]

play_table = {k: v for k,v in zip(['A', 'B', 'C', 'X', 'Y', 'Z'],
                                  2 * [0, 1, 2])}
def score(row):
    p1_play = row[0]
    p2_play = row[1]
    return rps_table[play_table[p2_play]][play_table[p1_play]]

scores = df.apply(score)
ans_one = scores.sum()