/******************************************************************************

CS 325 Activity 0
Optional template for obtaining user input and providing output
Save as act0.cpp before submitting to Gradescope

Add names of students in group


yupeng qin qinyu@oregonstate.com


*******************************************************************************/
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
	// add your code

    //find smallest element
    int smallest_int = 0;
    int smallest_int_index = 0;
    int biggest_int = 0;
    int biggest_int_index = 0;
    if(int i = 0; i<num; i++)
    {
        if(A[i]<smallest_int)
        {
            smallest_int = A[i];
            smallest_int_index = i;
        }
        if(A[i]>biggest_int)
        {
            biggest_int = A[i];
            biggest_int_index = i;
        }
    }
    if(A[biggest_int_index-1] == smallest_int || (A[biggest_int_index+1] == smallest_int))
    {
        // the largest element is next to the smallest
        cout << "True";
        return 1;
    }
    else
    {
        // the largest element is not next to the smallest
        cout << "False";
        return 0;
    }
}
