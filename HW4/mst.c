// Kruskal's algorithm in C
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "function.h"
int caseIndex=1;
VertexList vert;
int point[max][max], n;
EdgeList elist;
EdgeList path;
void Apply(int note[], int c1, int c2) {
    int i;
    for (i = 0; i < n; i++)
        if (note[i] == c2)
            note[i] = c1;
}
void Print(int caseIndex) {
    int i, total = 0;
    for (i = 0; i < path.n; i++)
    {
        total = total + path.data[i].w;
    }
    printf("\nTest case %d: MST weight %d\n",caseIndex, total);
}

void Sort() {
    int i, j;
    Edge temp;

    for (i = 1; i < elist.n; i++)
        for (j = 0; j < elist.n - 1; j++)
            if (elist.data[j].w > elist.data[j + 1].w) {
                temp = elist.data[j];
                elist.data[j] = elist.data[j + 1];
                elist.data[j + 1] = temp;
            }
}

void kruskal() {
    int note[max], i, j, check1, check2;
    elist.n = 0;
//save data to elist
     for (i = 1; i < n; i++)
        for (j = 0; j < i; j++) {
            //printf("i=%d j=%d\n",i,j);
            if (point[i][j] != 0) {
                elist.data[elist.n].u = i;
                elist.data[elist.n].v = j;
                elist.data[elist.n].w = point[i][j];
                elist.n++;
            }
        }
    Sort();
    for (i = 0; i < n; i++)
       note[i] = i;
    path.n = 0;
    for (i = 0; i < elist.n; i++) {
        check1 = FindNode(note, elist.data[i].u);
        check2 = FindNode(note, elist.data[i].v);

        if (check1 != check2) {
            path.data[path.n] = elist.data[i];
            path.n = path.n + 1;
            Apply(note, check1, check2);
        }
    }
}

int main() {

    char file_name[20];
    strcpy(file_name, "graph.txt");
    FILE *fp = fopen(file_name, "r");
    if (fp == NULL) {
        printf("no file");
        return 0;
    }
    int k1, k2, k3, k4;
    fscanf(fp, "%d", &k1);
    for ( int s = 0; s < k1; s++)
    {
        fscanf(fp, "%d", &k2);
        n=k2;
        vert.n=0;
        for(int i =0; i< n ; i++)
        {
            fscanf(fp, "%d", &k3);
            vert.num[vert.n].x = k3;
            fscanf(fp, "%d", &k4);
            vert.num[vert.n].y = k4;
            vert.n++;
        }
        for(int j=0; j<n; j++)
        {
            for(int k = 0; k<n; k++)
            {
                int number,f_number;
                float temp1, sqrt1;
                number= (((vert.num[j].x-vert.num[k].x)*(vert.num[j].x-vert.num[k].x))
                        +((vert.num[j].y-vert.num[k].y)*(vert.num[j].y-vert.num[k].y)));
                temp1=sqroot(number);
                sqrt1=temp1+0.5;
                f_number=(int)sqrt1;
                point[j][k]=  f_number;
            }
        }
        kruskal();
        Print(caseIndex);
        caseIndex=caseIndex+1;
    }
    fclose(fp);
}