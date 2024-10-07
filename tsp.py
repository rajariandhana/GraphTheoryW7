import sys
from itertools import permutations

# Function to calculate the TSP cost using a brute-force approach
def tsp(n, edges, start):
    # Create the adjacency matrix and edge name map
    graph = [[sys.maxsize] * n for _ in range(n)]
    edge_map = [[None] * n for _ in range(n)]
    
    # Fill the adjacency matrix and edge map with the given edge costs and edge names
    for edge in edges:
        edge_id, u, v, cost = edge
        graph[u - 1][v - 1] = cost
        graph[v - 1][u - 1] = cost
        edge_map[u - 1][v - 1] = edge_id
        edge_map[v - 1][u - 1] = edge_id
    
    # List of nodes except the starting node
    nodes = [i for i in range(n) if i != (start - 1)]
    
    # Store the minimum cost and the best route
    min_cost = sys.maxsize
    best_route_edges = []

    # Try all permutations of nodes
    for perm in permutations(nodes):
        current_cost = 0
        current_node = start - 1
        route_edges = []
        
        # Traverse through the permutation and calculate the cost
        for next_node in perm:
            current_cost += graph[current_node][next_node]
            route_edges.append(edge_map[current_node][next_node])
            current_node = next_node
        
        # Add the cost of returning to the starting node
        current_cost += graph[current_node][start - 1]
        route_edges.append(edge_map[current_node][start - 1])
        
        # If the current cost is less than the minimum cost, update it
        if current_cost < min_cost:
            min_cost = current_cost
            best_route_edges = route_edges
    
    return min_cost, best_route_edges

# Main function to read input and solve the TSP
def main():
    # Input for number of nodes and edges
    n = int(input())  # Number of nodes
    e = int(input())  # Number of edges
    
    # Read edges (edge_id, node1, node2, cost)
    edges = []
    for _ in range(e):
        edges.append(list(map(int, input().split())))
    
    # Starting node
    start = int(input())
    
    # Solve TSP
    cost, route_edges = tsp(n, edges, start)
    
    # Print results
    print(f"Cost: {cost}")
    print(f"Route: {', '.join(map(str, route_edges))}")

if __name__ == "__main__":
    main()
