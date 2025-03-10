import networkx as nx
import matplotlib.pyplot as plt

def build_graph():
    G = nx.DiGraph()
    
    edges = [
        ('Source', 'T1', 100), ('Source', 'T2', 100),
        ('T1', 'S1', 25), ('T1', 'S2', 20), ('T1', 'S3', 15),
        ('T2', 'S3', 15), ('T2', 'S4', 30), ('T2', 'S2', 10),
        ('S1', 'M1', 15), ('S1', 'M2', 10), ('S1', 'M3', 20),
        ('S2', 'M4', 15), ('S2', 'M5', 10), ('S2', 'M6', 25),
        ('S3', 'M7', 20), ('S3', 'M8', 15), ('S3', 'M9', 10),
        ('S4', 'M10', 20), ('S4', 'M11', 10), ('S4', 'M12', 15), ('S4', 'M13', 5), ('S4', 'M14', 10),
        ('M1', 'Sink', 15), ('M2', 'Sink', 10), ('M3', 'Sink', 20),
        ('M4', 'Sink', 15), ('M5', 'Sink', 10), ('M6', 'Sink', 25),
        ('M7', 'Sink', 20), ('M8', 'Sink', 15), ('M9', 'Sink', 10),
        ('M10', 'Sink', 20), ('M11', 'Sink', 10), ('M12', 'Sink', 15), ('M13', 'Sink', 5), ('M14', 'Sink', 10)
    ]
    
    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
    
    return G

def find_max_flow(G, source, sink):
    return nx.maximum_flow(G, source, sink)

def visualize_graph(G, flow_dict):
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', node_size=2000, font_size=10)
    edge_labels = {(u, v): f"{flow_dict[u][v]}/{G[u][v]['capacity']}" for u in flow_dict for v in flow_dict[u] if G.has_edge(u, v)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("Логістична мережа та потоки")
    plt.show()

def main():
    G = build_graph()
    source, sink = 'Source', 'Sink'
    flow_value, flow_dict = find_max_flow(G, source, sink)
    
    print(f"Максимальний потік: {flow_value}")
    print("Потоки по ребрах:")
    for u in flow_dict:
        for v in flow_dict[u]:
            if flow_dict[u][v] > 0:
                print(f"{u} -> {v}: {flow_dict[u][v]}")
    
    visualize_graph(G, flow_dict)

if __name__ == "__main__":
    main()