#!/bin/bash
gcc -std=c99 -o mst mst.c 
./mst > my_results.txt
./mst
echo
echo "Solution"
echo
cat HW4solution.txt
echo
diff -y -B -b --report-identical-files --suppress-common-lines my_results.txt HW4solution.txt
echo
