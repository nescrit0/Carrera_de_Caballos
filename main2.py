import networkx as nx
import matplotlib.pyplot as plt
import random

from re import X
caballos=list(range(1,26))
velocistas=[]
ciclos=[[] for i in range(5)]
random.shuffle(caballos)
print("Lista de numeros de los caballos")
print(caballos)

for i in range(5):
    for j in range(5):
        ciclos[j].append(caballos.pop())
for i in ciclos:
    i.sort()

def last(velocistas):
    return velocistas[-1]

ciclos = sorted(ciclos,key=last,reverse=True)
print("\nGrupos por sorteo seleccionados:")
for i in ciclos:
    for j in i:
        print('{:2d}'.format(j),end = ' ')
    print()

velocistas = ciclos[0][2:4] + ciclos[1][3:] + ciclos[2][4:]
velocistas.sort()
print("\nCarrera N°7: ")
print("\n  5°  4°  3°  2°  1°")
print(velocistas)

G=nx.DiGraph()
G.add_edges_from([('78','65'),('65','89')])
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=500)
nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='black')
nx.draw_networkx_nodes(G,pos)
plt.show()

