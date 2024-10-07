#include <bits/stdc++.h>
using namespace std;
int knight_moves_r[8]={1,2,2,1,-1,-2,-2,-1};
int knight_moves_c[8]={-2,-1,1,2,2,1,-1,-2};
int rows,columns;
int n_nodes;
int source_r,source_c;
map<int,map<int,vector<pair<int,int> > > > nodes;
map<int,map<int,bool> >vis;
bool validCoord(int r, int c){
    if(r<0 || c<0 || r>=rows || c>=columns) return false;
    return true;
}
vector<pair<int,int> >path;
bool hamil(int r,int c){
    if(path.size()==n_nodes) return true;

    for (auto i:nodes[r][c]){
        if(!vis[i.first][i.second]){
            vis[i.first][i.second];
            path.push_back(make_pair(i.first,i.second));
            if(hamil(i.first,i.second)) return true;
            vis[i.first][i.second]=false;
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
    if(hamil(source_r,source_c)){
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
    for(int i=0;i<rows;i++){
        for(int j=0;j<columns;j++){
            cout<<i<<" "<<j<<endl;
            for(auto k:nodes[i][j]){
                cout<<"    "<<k.first<<" "<<k.second<<endl;
            }
        }
    }
}