import networkx as nx
import matplotlib.pyplot as plt
import math

# 1. Landmarks including an expanded Hostel Block
locations = {
    'Main_Gate': (5, 10),
    'Exit_Gate': (90,65),
    'Auditorium': (30, 33),
    'Library': (65, 20),
    'Lab_Complex': (85, 25),
    'Shopping_Complex': (25, 60),
    'Canteen': (65, 40),
    'Gym': (55, 80),
    'Sports_Ground': (70, 90),
    'Academic_Block': (50, 15),
    'Medical_Center': (42, 65),
    # Expanded Hostel Block
    'Central_Office': (25, 80), # Hub for hostels
    'Hostel_1': (15, 95),
    'Hostel_2': (5, 85),
    'Hostel_4': (10, 70),
    'Hostel_8': (35, 90)
}

G = nx.Graph()
for node, pos in locations.items():
    G.add_node(node, pos=pos)

# 2. Updated Edges with specific hostel connections
paths = [
    ('Main_Gate', 'Auditorium', 450, 'flat'),
    ('Auditorium', 'Shopping_Complex', 320, 'flat'),
    ('Shopping_Complex', 'Central_Office', 150, 'flat'),
    ('Central_Office','Medical_Center',75,'flat'),
    ('Medical_Center','Gym',150,'flat'),
    ('Academic_Block','Canteen',220,'flat'),
    ('Auditorium','Academic_Block',380,'flat'),
    ('Canteen','Sports_Ground',650,'flat'),
    ('Canteen','Exit_Gate',500,'flat'),
    ('Academic_Block','Library',85,'stairs'),
    ('Lab_Complex','Exit_Gate',380,'flat'),
    
    
    # Connecting Hostels to the Central Office
    ('Central_Office', 'Hostel_1', 60, 'stairs'),
    ('Central_Office', 'Hostel_2', 70, 'flat'),
    ('Central_Office', 'Hostel_4', 50, 'flat'),
    ('Central_Office', 'Hostel_8', 80, 'stairs'),
    
    # Inter-Hostel paths (Shortcuts)
    ('Hostel_1', 'Hostel_2', 40, 'flat'),
    ('Hostel_4', 'Shopping_Complex', 65, 'flat'),
    
    # Academic/Social connections
    ('Lab_Complex', 'Library', 120, 'flat'),
    ('Lab_Complex', 'Canteen', 90, 'flat'),
    ('Library', 'Canteen', 110, 'stairs'), # Direct steep path
    ('Hostel_8', 'Gym', 200, 'flat'),
    ('Gym', 'Sports_Ground', 80, 'flat'),
    ('Academic_Block', 'Medical_Center', 420, 'flat'),
    ('Gym', 'Academic_Block', 130, 'flat')
]

for u, v, w, t in paths:
    # Applying the 1.5x Factor for stairs
    weight = w * 1.5 if t == 'stairs' else w
    G.add_edge(u, v, weight=weight, type=t)

# 3. A* Logic
def heuristic_dist(u, v):
    x1, y1 = locations[u]
    x2, y2 = locations[v]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #Euclidean Distance

# Change these to test different routes (input)
start_point = input("Start_point:")
end_point = input("End_point:")

path = nx.astar_path(G, start_point, end_point, heuristic=heuristic_dist, weight='weight')
path_length = nx.astar_path_length(G, start_point, end_point, heuristic=heuristic_dist, weight='weight')

# 4. Visualization
plt.figure(num="Smart University Campus Navigator by Devesh Katneshwarkar",figsize=(12, 10))
pos = nx.get_node_attributes(G, 'pos')


# Draw Nodes
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color='lightgrey', label='Landmarks')
nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

# Differentiate Edges: Solid for flat, Dashed for stairs
flat_edges = [(u, v) for u, v, d in G.edges(data=True) if d['type'] == 'flat']
stair_edges = [(u, v) for u, v, d in G.edges(data=True) if d['type'] == 'stairs']

nx.draw_networkx_edges(G, pos, edgelist=flat_edges, alpha=0.3, edge_color='black', label='Flat Path')
nx.draw_networkx_edges(G, pos, edgelist=stair_edges, alpha=0.5, edge_color='red', style='dashed', label='Stairs (1.5x Cost)')

# Highlight the selected path
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange', node_size=1500)
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=4, label='Optimized Route')

plt.title(f"A* Navigator: {start_point} to {end_point}\nDistance: {path_length:.2f}m", fontsize=15)
plt.legend(scatterpoints=1, loc='best', fontsize=10)
plt.axis('off')
plt.show()