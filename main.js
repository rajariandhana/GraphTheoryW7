class Graph {
    constructor() {
        this.adjacencyList = {};
    }

    // Add a vertex with specified row and column
    addVertex(row, col) {
        const vertex = `${row},${col}`;
        if (!this.adjacencyList[vertex]) {
            this.adjacencyList[vertex] = [];
        }
    }

    // Add an edge between two vertices (undirected)
    addEdge(row1, col1, row2, col2) {
        const vertex1 = `${row1},${col1}`;
        const vertex2 = `${row2},${col2}`;

        // Ensure both vertices exist
        this.addVertex(row1, col1);
        this.addVertex(row2, col2);

        // Add the edge in both directions
        this.adjacencyList[vertex1].push(vertex2);
        this.adjacencyList[vertex2].push(vertex1);
    }

    // Get adjacent vertices for a specific vertex
    getAdjacent(row, col) {
        const vertex = `${row},${col}`;
        return this.adjacencyList[vertex] || [];
    }

    // Print the graph
    printGraph() {
        for (let vertex in this.adjacencyList) {
            console.log(`${vertex} -> ${this.adjacencyList[vertex].join(', ')}`);
        }
    }
}

// Example usage:
const graph = new Graph();
graph.addEdge(0, 0, 0, 1);
graph.addEdge(0, 0, 1, 0);
graph.addEdge(0, 1, 1, 1);
graph.addEdge(1, 0, 1, 1);

graph.printGraph();

// Get adjacent vertices for a specific vertex
console.log(graph.getAdjacent(0, 0)); // Output: [ '0,1', '1,0' ]
