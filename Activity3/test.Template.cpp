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
    int data[6][6];
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
			cin >> data[i][j];
        }
    }
    int min_cost_data[n][n];
    int stop_data[n][n];
    // min_cost_data = [[-1 for x in range(MaxTT)] for x in range(QPort)]
    // stop_data = [[-1 for x in range(MaxTT)] for x in range(QPort)]
    for(int trip_time =0; trip_time<n; trip_time++)
        for(int port_code =trip_time; trip_time<n; port_code++)
        {

            if (trip_time == 0)
            {
                min_cost_data[trip_time][port_code] = data[trip_time][port_code];
                stop_data[trip_time][port_code] = [0,0,0,0];
                stop_data[trip_time][port_code][trip_time] = 1;
                stop_data[trip_time][port_code][port_code] = 1;
            }
            else if(port_code == trip_time)
            {
                min_cost_data[trip_time][port_code] = min_cost_data[trip_time - 1][port_code]
                stop_data[trip_time][port_code] = list(stop_data[trip_time - 1][port_code])
            }
            else
            {
                if(data[trip_time][port_code] + min_cost_data[trip_time][port_code - 1] < min_cost_data[trip_time - 1][port_code])
                {
                    min_cost_data[trip_time][port_code] = data[trip_time][port_code] + min_cost_data[trip_time][port_code - 1]
                    stop_data[trip_time][port_code] = list(stop_data[trip_time][trip_time])
                    stop_data[trip_time][port_code][port_code] = 1
                }
                else:
                {
                    min_cost_data[trip_time][port_code] = min_cost_data[trip_time - 1][port_code]
                    stop_data[trip_time][port_code] = list(stop_data[trip_time - 1][port_code])
                }
            }
        }
    print(min_cost_data[MaxTT - 1][QPort -1])
    print(stop_data[MaxTT - 1][QPort -1])
    return 0


    cout<<"12 1 3 5"<<endl;

	return 1;
}
