/******************************************************************************
CS 325 Activity 6 Babyface & Heels
Sample Test Case
Input:
4
4
1 2
1 3
4 2
4 3
Output:
Possible
Save file as act6.cpp before submitting to Gradescope
*******************************************************************************/
#include <iostream>
#include <fstream>
using namespace std;

int G[100][100];   // if you want to use an adjacency matrix
int n;

void traverse(int u, bool visited[])
{
   visited[u] = true; //mark v as visited
   for(int v = 0; v<n; v++)
   {
      if(G[u][v])
      {
         if(!visited[v])
            traverse(v, visited);
      }
   }
}
bool babyfaceHeel() {
   bool *vis = new bool[n];
   for(int u=0; u < n; u++)
   {
      for(int i = 0; i<n; i++)
         vis[i] = false;
        traverse(u, vis);
      for(int i = 0; i<n; i++)
      {
         if(!vis[i])
            return false;
      }
   }
   return true;
}
int main()
{
  // Create a graph given in the above diagram
	      	// number of wrestlers numbered 1..n
	int m;		    // number of rivalries
	int w1, w2;
	cin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			G[i][j]=0;

	cin >> m;

	for (int j = 0; j < m; j++)
    {
		// 1st wrestler
		cin >> w1;
		// 2nd wrestler
		cin >> w2;
		w1--;
		w2--;
		// Add edges to adjacency matrix optional
		G[w1][w2] = 1;
		G[w2][w1] = 1;
    }

	bool result = babyfaceHeel();
    // cout << "Impossible"<<endl;
	if (result) {
	  cout << "Possible"<<endl;
	}  else {
      cout << "Impossible" << endl;
	}
	return 0;
}
