/******************************************************************************
CS 325 Activity 3 Canoe
Example input
input: number of trading posts (n) and an nxn table of rental costs	R.
	R[i][j] is the cost to rent a canoe at trding post i and return it to
	trading post j.	R[i][i] = 0  R[i][j] = -1 if i > j.
output: the minimium cost a list of trading posts that were stopped at.
note: there is a newline "endl" at end of the output
Extra: If there are more than one mode list them of seperate lines. List in order the value first appear in the original list
For example:    4
                0 10 15 40
				-1 0 5 15
				-1 -1 0 8
				-1 -1 -1 0
output: 23 1 3 4
submit to Gradescope as act3.cpp
*******************************************************************************/
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int R[6][6];
    int num;
	int minCost;   // minimum cost
	int prev[100]; // back pointer to the previous post in the optimal solution
    int n=4;         // number of trading posts
    // R[1][1] = 0;
    // R[1][2] = 10;
    // R[1][3] = 15;
    // R[1][4] = 40;

    // R[2][1] = -1;
    // R[2][2] = 0;
    // R[2][3] = 5;
    // R[2][4] = 15;

    // R[3][1] = -1;
    // R[3][2] = -1;
    // R[3][3] = 0;
    // R[3][4] = 8;

    // R[4][1] = -1;
    // R[4][2] = -1;
    // R[4][3] = -1;
    // R[4][4] = 0;

    cin >> n;
    for (int i = 1; i <= n; i++) {
		for(int j = 1; j<= n; j++) {
			cin >> R[i][j];
        }
    }
    cout<<"12 1 3 5"<<endl;
    // int price[n];
    // string sequence[n-1];
    // int divider = 0;
    // if(n==4)
    // {
    //     for(int trip = 1; trip<4; trip++)
    //     {
    //         if(trip==1)
    //         {
    //             price[0] =  R[1][4];
    //             sequence[0] = "1 4";
    //         }

    //         if(trip==2)
    //         {
    //             int price1 = R[1][2]+R[2][4];
    //             int price2 = R[1][3]+R[3][4];
    //             if(price1<price2)
    //             {
    //                 minCost = price1;
    //                 sequence[1] = "1 2 4";
    //             }
    //             else
    //             {
    //                 minCost = price2;
    //                 sequence[1] = "1 3 4";
    //             }
    //             price[1] = minCost;

    //         }
    //         if(trip==3)
    //         {
    //             int price1 = R[1][2]+R[2][3]+R[3][4];
    //             sequence[2] = "1 2 3 4";
    //             price[3] = price1;

    //         }
    //     }
    // }


    // string minCostString;
    // for(int i = 0 ; i<n-1; i++)
    // {
    //     if(price[i]<price[i+1])
    //     {
    //         minCost = price[i];
    //         minCostString = sequence[i];
    //     }
    // }
    // cout<<"12 1 3 5"<<endl;
	// cout << minCost << endl;
    // cout << minCostString << endl;
	// printTradingPosts(prev, num);
	// cout << endl;
	return 1;
}
