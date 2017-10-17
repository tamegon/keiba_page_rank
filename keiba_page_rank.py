import networkx as nx
import os
import pandas as pd
import json
import yaml

RELATION_CSV_PATH = './relations.csv'

relations = pd.read_csv(RELATION_CSV_PATH, header=None)
relations.columns = ['loser', 'winner']

names = relations['loser'].unique()

g = nx.DiGraph()

for name in names:
	g.add_node(name)

for row in relations.iterrows():
	g.add_edge(row[1]['loser'],row[1]['winner'])

prn = nx.pagerank_numpy(g,alpha=0.85)

print(prn)
