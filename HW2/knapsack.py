"""
Yupeng Qin
April 13 2022
CS325

Reference:
knapsack-problem. geeksforgeeks. https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/
Dynamic Programming | KnapSack | Python. Youtube. https://www.youtube.com/watch?v=wJJ3FFjFSaM
"""
import random
import time


class Algorithms:
    def __init__(self, __size, __max_volume):
        self.__val = []
        self.__wt = []
        self.__max_volume = __max_volume
        self.__generate_value_weight(__size)

    def __generate_value_weight(self, __size):
        self.__val = [random.randint(1, 100) for i in range(__size)]
        self.__wt = [random.randint(1, 100) for i in range(__size)]
        # self.__val = [60, 100, 120]
        # self.__wt = [10, 20, 30]
        # self.__max_volume =50
        # print(self.__val)
        # print(self.__wt)

    def _knapsack_dynamic(self):
        start_time = time.time()
        return self.__knapsack_dynamic_core(self.__max_volume, self.__wt, self.__val, len(self.__val)), time.time()-start_time

    def __knapsack_dynamic_core(self, __max_volume, __wt, __val, cur_index):
        K = [[0 for x in range(__max_volume + 1)] for x in range(cur_index + 1)]
        for i in range(cur_index + 1):
            for w in range(__max_volume+1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif __wt[i-1] <= w:
                    K[i][w] = max(__val[i-1] + K[i-1][w-__wt[i-1]],  K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]
        return K[cur_index][__max_volume]
    def _knapsack_recursive(self):
        start_time = time.time()
        return self.__knapsack_recursive_core(self.__val, self.__wt, self.__max_volume, len(self.__val)), time.time()-start_time

    def __knapsack_recursive_core(self, __val, __wt, __max_volume, cur_index):
        if cur_index == 0 or __max_volume == 0:
            return 0
        # print(type(self.__wt[cur_index-1]))
        if (self.__wt[cur_index-1] > __max_volume):
            return self.__knapsack_recursive_core(__val, __wt, __max_volume, cur_index-1)
        else:
            return max(__val[cur_index-1] + self.__knapsack_recursive_core(__val, __wt, __max_volume-__wt[cur_index-1], cur_index-1),
                       self.__knapsack_recursive_core(__val, __wt, __max_volume, cur_index-1))


if __name__ == "__main__":
    W = 100
    for N in [10,20,30,40,50,60,70]:
        algorithm = Algorithms(N, W)
        r_result, r_e_time = algorithm._knapsack_recursive()
        d_result, d_e_time = algorithm._knapsack_dynamic()
        print(f"N={N} W={W} Rec time = {r_e_time} DP time = {d_e_time} max Rec = {r_result} max DP = {d_result}")
