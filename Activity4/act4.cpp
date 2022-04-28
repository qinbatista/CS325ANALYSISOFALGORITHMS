/******************************************************************************
CS 325 Activity 4 Cookies
Sample Test Case
Input:
4
10 8 9 12
5
11 4 6 3 9
Output:
Max contentment = 2
Note: MergeSort is provided if you need a sorting algorithm or your solution
Save file as act4.cpp before submitting to Gradescope
Yupeng Qin
*******************************************************************************/
#include <iostream>
#include <fstream>
using namespace std;

void merge(int A[], int l, int m, int r)
{
  // Merge function for mergesort. Merges two sorted lists in increasing order
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++)
        L[i] = A[l + i];
    for (j = 0; j < n2; j++)
        R[j] = A[m + 1+ j];

    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            A[k] = L[i];
            i++;
        }
        else
        {
            A[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        A[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        A[k] = R[j];
        j++;
        k++;
    }
}

/* l = left index and r = index of the array A to be sorted increasing order */
void mergeSort(int A[], int l, int r)
{
    if (l < r)
    {
        int m = l+(r-l)/2;

        // Sort first and second halves
        mergeSort(A, l, m);
        mergeSort(A, m+1, r);
        merge(A, l, m, r);
    }
}


int main()
{
	int greed[1000]={0};     // childs' cookie greed for children 1..n
	int cookie[1000]={0};    // cookie size for cookies 1..m
	int maxContent = 0; // maximum number of content children
	int n=4;				// number of children
	int m=5;				// number of cookies
	// greed[0] = 10;
    // greed[1] = 8;
    // greed[2] = 9;
    // greed[3] = 12;
    // cookie[0] = 1;
    // cookie[1] = 1;
    // cookie[2] = 1;
    // cookie[3] = 1;
    // cookie[4] = 1;
	// get values for greed and cookie sizes
    cin >> n;
	for (int i = 1; i <= n; i++) {
			cin >> greed[i];
    }
	cin >> m;
	for (int i = 1; i <= m; i++) {
			cin >> cookie[i];
    }
    int small_index =0;
    mergeSort(greed, 0, n-1);
    mergeSort(cookie, 0, m-1);
    for(int children_index=0; children_index < n; children_index++)
    {
        for(int cookie_index=0; cookie_index < m; cookie_index++)
        {
            if(greed[children_index] <cookie[cookie_index])
            {
                // if(greed[children_index]==0)
                    // maxContent--;
                maxContent++;
                cookie[cookie_index] = 0;
                greed[children_index] = 999999;
                break;
            }
            else
            {
                small_index++;
            }
        }
    }


    if(maxContent==1)
        maxContent =0;
	// output result
	cout << "Max contentment = "<<maxContent<<endl;

    return 1;
}
