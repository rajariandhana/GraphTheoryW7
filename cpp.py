import itertools
import heapq

# Read the number of vertices and edges
num_vertices = int(input(""))
num_edges = int(input(""))
edges_dict, adjacency_list = {}, {i: [] for i in range(1, num_vertices + 1)}

def insert_edge(edge_id, vertex_a, vertex_b, weight):
    existing_edges = [(adj, wt, name) for adj, wt, name in adjacency_list[vertex_a] if adj == vertex_b and wt > weight]
    if existing_edges:
        previous_edge_name = existing_edges[0][2]
        adjacency_list[vertex_a] = [(adj, wt, name) for adj, wt, name in adjacency_list[vertex_a] if adj != vertex_b]
        adjacency_list[vertex_b] = [(adj, wt, name) for adj, wt, name in adjacency_list[vertex_b] if adj != vertex_a]
        del edges_dict[previous_edge_name]

        edges_dict[edge_id] = (vertex_a, vertex_b, weight)
        adjacency_list[vertex_a].append((vertex_b, weight, edge_id))
        adjacency_list[vertex_b].append((vertex_a, weight, edge_id))

        edges_dict[previous_edge_name] = (vertex_a, vertex_b, existing_edges[0][1])
        adjacency_list[vertex_a].append((vertex_b, existing_edges[0][1], previous_edge_name))
        adjacency_list[vertex_b].append((vertex_a, existing_edges[0][1], previous_edge_name))
    else:
        edges_dict[edge_id] = (vertex_a, vertex_b, weight)
        adjacency_list[vertex_a].append((vertex_b, weight, edge_id))
        adjacency_list[vertex_b].append((vertex_a, weight, edge_id))

# Input edges
for _ in range(num_edges):
    edge_input = input("").split()
    edge_id, vertex_a, vertex_b, weight = int(edge_input[0]), int(edge_input[1]), int(edge_input[2]), int(edge_input[3])
    if vertex_a > vertex_b:
        vertex_a, vertex_b = vertex_b, vertex_a
    insert_edge(edge_id, vertex_a, vertex_b, weight)

# Calculate the degrees of each vertex
def calculate_degrees(adj_list):
    return {i: len(adj_list[i]) for i in adj_list}

# Find vertices with odd degrees
def get_odd_vertices(degrees):
    return [v for v in degrees if degrees[v] % 2 != 0]

# Dijkstra's algorithm for shortest paths
def shortest_path(start_vertex, end_vertex):
    distances = {i: float('inf') for i in range(1, num_vertices + 1)}
    distances[start_vertex], predecessors, edge_used = 0, {i: None for i in range(1, num_vertices + 1)}, {}
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight, edge_id in adjacency_list[current_vertex]:
            if current_distance + weight < distances[neighbor]:
                distances[neighbor], predecessors[neighbor], edge_used[neighbor] = current_distance + weight, current_vertex, edge_id
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))
    
    path, current = [], end_vertex
    while predecessors[current]:
        path.append(edge_used[current])
        current = predecessors[current]
    return distances[end_vertex], path[::-1]

# Match vertices with odd degrees
def match_odd_degree_vertices(odd_vertices):
    vertex_pairs = itertools.combinations(odd_vertices, 2)
    return {(u, v): shortest_path(u, v) for u, v in vertex_pairs}

# Add edges for the matched pairs
def append_matching_edges(odd_vertices, pairings):
    total_extra_cost, combined_route = 0, []
    while odd_vertices:
        current_vertex = odd_vertices.pop(0)
        best_match = min((v for v in odd_vertices), key=lambda v: pairings[(current_vertex, v)][0])
        odd_vertices.remove(best_match)
        total_extra_cost += pairings[(current_vertex, best_match)][0]
        combined_route += pairings[(current_vertex, best_match)][1]
    return total_extra_cost, combined_route

# Perform Eulerian tour
def create_eulerian_tour(start_vertex):
    path_stack, eulerian_path, visited_edges = [start_vertex], [], set()
    while path_stack:
        current_vertex = path_stack[-1]
        possible_edges = [(v, w, eid) for v, w, eid in adjacency_list[current_vertex] if eid not in visited_edges]
        if possible_edges:
            next_vertex, weight, edge_id = min(possible_edges, key=lambda x: x[1])
            visited_edges.add(edge_id)
            path_stack.append(next_vertex)
        else:
            eulerian_path.append(path_stack.pop())
    return eulerian_path

# Main function for solving the Chinese Postman Problem
def solve_chinese_postman():
    vertex_degrees = calculate_degrees(adjacency_list)
    odd_degree_vertices = get_odd_vertices(vertex_degrees)
    additional_cost, additional_edges = 0, []
    
    if odd_degree_vertices:
        vertex_pairings = match_odd_degree_vertices(odd_degree_vertices)
        additional_cost, additional_edges = append_matching_edges(odd_degree_vertices, vertex_pairings)

    total_cost = sum(weight for _, (_, _, weight) in edges_dict.items()) + additional_cost
    eulerian_path = create_eulerian_tour(start_vertex)
    print(f"Total Cost: {total_cost}")
    print("Complete Route:", ', '.join(str(edge) for edge in list(edges_dict.keys()) + additional_edges))

start_vertex = int(input(""))
solve_chinese_postman()
