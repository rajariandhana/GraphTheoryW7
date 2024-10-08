# GraphTheoryW7
 
## The Knight's Tour
Demonstration is available in graph.ralfazza.com

### Problem Description
Given a chessboard with a single knight, we must find out if the knight can visit all squares in the board only once. We can represent this problem into an undirected unweighted graph problem such that each vertex is a square in the board with any vertices in reach from a knight's moveset is the adjacent vertices. Since all vertices must be visited once, The Knight's Tour is also a Hamiltonian Path problem.

### Algorithm
A simple DFS is used.

### Graph Representation
Adjacency List is used where each vertex contains a list of vertices in range. Since a coordinate is used as a key, the graph is representated as
```cpp
map<int, map<int,vector<pair<int,int>>>> nodes
```
For instance if we want to add the square at 3,1 to square 1,0 we can use
```cpp
nodes[1,0].push_back(make_pair(3,1));
```

### Solution
A knight's set move is all vertices in reach of an L shape from a square.
```cpp
int knight_moves_r[8]={1,2,2,1,-1,-2,-2,-1};
int knight_moves_c[8]={-2,-1,1,2,2,1,-1,-2};
```

Generate the graph based on the input. Each vertex can have a direct path to the L shape thus pushing those vertices as a pair of coordinates into the adjacency list of a square.
```cpp
bool validCoord(int r, int c){
    if(r<0 || c<0 || r>=rows || c>=columns) return false;
    return true;
}
for(int i=0;i<rows;i++){
    for(int j=0;j<columns;j++){
        for(int k=0;k<8;k++){
            int newR = i+knight_moves_r[k];
            int newC = j+knight_moves_c[k];
            if(validCoord(newR,newC)) nodes[i][j].push_back(make_pair(newR,newC));
        }
    }
}
```

Set all vertices to be unvisited.
```cpp
for(int i=0;i<rows;i++){
    for(int j=0;j<columns;j++){
        vis[i][j]=false;
    }
}
```

A recursive function that implements DFS is used where the base case occurs when the length of the path vector is the same with the number of nodes (this means that all vertices have been visited). At each vertex it sets the vertex as visited then iterates through all adjacent vertices of current vertex. If the vertex has not been visited, it marks it as visited and push it into the path. It then recursively goes to the current iteration's vertices and does the same thing. If it finds a hamiltonian it returns true and end it, else it unmarks the vertex (make it unvisited) and remove it from the path.
```cpp
bool Hamiltonian(int r,int c){
    vis[source_r][source_c]=true;
    if(path.size()==n_nodes) return true;

    for (auto i:nodes[r][c]){
        int curR=i.first;
        int curC=i.second;
        if(!vis[curR][curC]){
            vis[curR][curC]=true;
            path.push_back(make_pair(curR,curC));
            if(Hamiltonian(curR,curC)) return true;
            vis[curR][curC]=false;
            path.pop_back();
        }
    }
    return false;
}
```