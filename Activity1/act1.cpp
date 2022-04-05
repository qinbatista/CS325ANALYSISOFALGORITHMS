/******************************************************************************

CS 325 Activity 0
Optional template for obtaining user input and providing output
Save as act0.cpp before submitting to Gradescope

Add names of students in group
1.yupeng qin
2.Kedar Dhere
3.Atharva Joshi
*******************************************************************************/
#include <iostream>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;



int main()
{
    int A[1000];  	// array of elements <= 1000
    int num;		// number of elements in the array
    cin >> num;		// read in number of elements
	cin >> A[0];	// the list will have at least one element
     for (int j = 1; j < num; j++) {
        cin >> A[j];
    }
    // 7 8 1 3 4 8 3 1 8 1 10 23 3 8 3
    // int A[100];
    // int num = 15;
    // A[0]= 7;
    // A[1]= 8;
    // A[2]= 1;
    // A[3]= 3;
    // A[4]= 4;
    // A[5]= 8;
    // A[6]= 3;
    // A[7]= 1;
    // A[8]= 8;
    // A[9]= 1;
    // A[10]= 10;
    // A[11]= 23;
    // A[12]= 3;
    // A[13]= 8;
    // A[14]= 3;
    int count = 0;
    int freq[num];
    for(int i=0; i<num; i++)
    {
        count = 1;
        for(int j=i+1; j<num; j++)
        {
            if(A[i]==A[j])
            {
                count++;

                freq[j] = 0;
            }
        }

        if(freq[i] != 0)
        {
            freq[i] = count;
        }
    }


    int max_freq = 0;
    int max_value =0;
    for(int i=0; i<num; i++)
    {
        if(freq[i]>max_freq)
        {
            max_freq = freq[i];
        }
    }

    for(int i=0; i<num; i++)
    {
        if (freq[i] == max_freq)
        {
            cout << A[i] << " " << freq[i]<< "\n";
        }
    }
}
