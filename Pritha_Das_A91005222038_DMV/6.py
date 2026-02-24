# Write a python code to create a complete graph with vertices user defined and greater than 3
import networkx as nx
import matplotlib.pyplot as plt

# Taking number of vertices
n = int(input("Enter number of vertices (greater than 3): "))

if n <= 3:
    print("Number of vertices must be greater than 3.")
else:
    # Create complete graph
    G = nx.complete_graph(n)

    # Draw graph
    nx.draw(G, with_labels=True, node_color='pink', 
            node_size=800, font_size=12)

    plt.title("Complete Graph")
    plt.show()
