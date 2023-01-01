import pandas as pd


df = pd.read_csv('day2/input.txt', header=None)

def score(row):
    player_1 = {k, v for k,v in zip([])}