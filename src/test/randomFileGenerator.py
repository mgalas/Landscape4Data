import pandas as pd
import random


filename = '../../data/01aJourneyDataExtract10Jan16-23Jan16.csv'
n = sum(1 for line in open(filename)) - 1
s = 40
skip = sorted(random.sample(range(1, n+1), n-s))
df = pd.read_csv(filename, skiprows=skip)
df.drop(df.columns[0], axis=1)
df.to_csv('../../data/test.csv')