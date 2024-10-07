#include <bits/stdc++.h>
using namespace std;

int knight_moves_r[8]={1,2,2,1,-1,-2,-2,-1};
int knight_moves_c[8]={-2,-1,1,2,2,1,-1,-2};
int rows,columns;
int n_nodes;
int source_r,source_c;

map<int,map<int,vector<pair<int,int> > > > nodes;
map<int,map<int,bool> >vis;
vector<pair<int,int> >path;

bool validCoord(int r, int c){
    if(r<0 || c<0 || r>=rows || c>=columns) return false;
    return true;
}
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
void GeneratePath(){
    for(int i=0;i<rows;i++){
        for(int j=0;j<columns;j++){
            vis[i][j]=false;
        }
    }
    path.push_back(make_pair(source_r,source_c));
    if(Hamiltonian(source_r,source_c)){
        for(auto i:path){
            cout<<i.first<<" "<<i.second<<endl;
        }
    }
}
int main(){
    cout<<"Number of rows: ";
    cin>>rows;
    cout<<"Number of columns: ";
    cin>>columns;
    cout<<"Source row: ";
    cin>>source_r;
    cout<<"Source column: ";
    cin>>source_c;
    n_nodes = rows*columns;

    for(int i=0;i<rows;i++){
        for(int j=0;j<columns;j++){
            for(int k=0;k<8;k++){
                int newR = i+knight_moves_r[k];
                int newC = j+knight_moves_c[k];
                if(validCoord(newR,newC)) nodes[i][j].push_back(make_pair(newR,newC));
            }
        }
    }
    // for(int i=0;i<rows;i++){
    //     for(int j=0;j<columns;j++){
    //         cout<<i<<" "<<j<<endl;
    //         for(auto k:nodes[i][j]){
    //             cout<<"    "<<k.first<<" "<<k.second<<endl;
    //         }
    //     }
    // }
    GeneratePath();
    ofstream outFile("path.txt");
    
    if (outFile.is_open()) {
        outFile << rows << endl<<columns<<endl<<source_r<<endl<<source_c<<endl<<n_nodes<<endl;

        for (const auto& p : path) {
            outFile << p.first << " " << p.second << endl;
        }

        outFile.close();
        cout << "Data exported to output.txt successfully." << endl;
    } else {
        cerr << "Unable to open file for writing." << endl;
    }
}