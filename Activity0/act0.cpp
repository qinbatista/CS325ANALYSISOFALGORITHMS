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
    //gcc act0.cpp -o out -lstdc++
    int A[1000];  	// array of elements <= 1000

    int num;		// number of elements in the array
    cin >> num;		// read in number of elements
	cin >> A[0];	// the list will have at least one element
    for (int j = 1; j < num; j++) {
        cin >> A[j];
    }

	// add your code
    // int A[5]={1,9,10,5,6};
    // int num = 5;
    //find smallest element
    int smallest_int = 9999;
    int smallest_int_index = 0;
    int biggest_int = 0;
    int biggest_int_index = 0;

    //find smallest integer and largest integer at same time
    for(int i = 0; i<num; i++)
    {
        if(A[i]<smallest_int)
        {
            smallest_int = A[i];
            smallest_int_index = i;
            // printf("smallest_int: %d\n",smallest_int);
        }
        if(A[i]>biggest_int)
        {
            biggest_int = A[i];
            biggest_int_index = i;
            // printf("biggest_int: %d\n",biggest_int);
        }
    }
    // printf("smallest:%d\n",smallest_int);
    // printf("biggest:%d\n",biggest_int);

    //if the left and the right from the smallest integer is big value, return true, else return false
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

1:find smallest integer and the biggest integer, and recored their index in the list

2:if the left and the right from the smallest integer is biggest integer, return true, else return false,
because we already know the index of the smallest integer and the biggest integer, we can use the index to find the left and right of the biggest integer


for check all the elements in the list
    if biggest integer:
        save the index and keep this integer
    if smallest integer:
        save the index and keep this integer

if the right and the left of the smallest integer is biggest integer:
    return true
else:
    return false