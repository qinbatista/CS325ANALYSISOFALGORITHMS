#define max 100
double sqroot(double square);
int FindNode(int note[], int vertexno);
void Apply(int note[], int c1, int c2);
typedef struct Edge {
    int u, v, w;
} Edge;
typedef struct EdgeList {
    Edge data[max];
    int n;
} EdgeList;
typedef struct Vertex {
    int x,y;
} Vertex;

typedef struct VertexList {
    Vertex num[max];
    int n;
} VertexList;
