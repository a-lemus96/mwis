# stdlib modules
import argparse
import os

# third-party modules
import numpy as np

# custom modules
import mwis

# config argparser
parser = argparse.ArgumentParser(description='Solution to MWIS problem')
parser.add_argument('-file', type=str, default='wis1.txt',
                    help='Input file to read path graph from')
parser.add_argument('-method', type=str, default='dc',
                    help='Method for solving problem, dc or dp')

# parse arguments
args = parser.parse_args()

graph = []
path = os.path.normpath(os.path.join('data', args.file))
# read graph
with open(path, 'r') as f:
    n = int(f.readline()) # read first line
    for _ in range(n): # read remaining lines
        node = f.readline()
        graph.append(int(node))

graph = np.array(graph) # cast to numpy array
#graph = np.array([4, 2 ,8, 3, 2, 6])
#graph = np.random.randint(0, 500, 5)
#graph = np.array([294, 289, 230, 84, 66])
#print(graph)

# solve mwis using whichever method chosen
#if args.method == 'dc':
sol1 = mwis.divide_conquer(graph, p=0, q=len(graph))
#elif args.method == 'dp':
sol2 = mwis.dynamic_programming(graph)

#prune = set(list(range(n))) - set(sol)
print("Final result")
print(np.sum(graph[sol1]) - np.sum(graph[sol2]))
