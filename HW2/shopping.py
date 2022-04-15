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
    def __init__(self):
        self.__val = []
        self.__wt = []
        self.__family_volume= []
        # self.__max_volume = __max_volume
        # self.__generate_value_weight(__size)
        self.__read_data()
    def __generate_value_weight(self, __size):
        self.__val = [random.randint(1, 100) for i in range(__size)]
        self.__wt = [random.randint(1, 100) for i in range(__size)]
        # self.__val = [60, 100, 120]
        # self.__wt = [10, 20, 30]
        # self.__max_volume =50
        # print(self.__val)
        # print(self.__wt)

    def __read_data(self):
        # with open("./shopping.txt") as f:
        with open("./shopping.txt") as f:
            lines = f.readlines()
        index = 0
        cases = lines[index]
        for case in range(int(cases)):
            self.__val.clear()
            self.__wt.clear()
            self.__family_volume.clear()
            index+=1
            number_of_products = int(lines[index])
            for i in range(index+1, index+int(number_of_products)+1):
                value, weight =lines[i].split(" ")
                self.__val.append(int(value))
                self.__wt.append(int(weight))
            index+=int(number_of_products)+1
            number_of_family = int(lines[index])
            for i in range(index+1, index+int(number_of_family)+1):
                volume = lines[i]
                self.__family_volume.append(int(volume))
            index+=int(number_of_family)
            print(f"Test Case {case+1}")
            totalWeight=[]
            totalItemList =[]
            for i in range(0,number_of_family):
                weight, itemList = self.__pickKLnapSack(self.__family_volume[i], self.__wt, self.__val, len(self.__val))
                totalWeight.append(weight)
                totalItemList.append(itemList)
            print(f"Total Price {sum(totalWeight)}")

            for i in range(0,number_of_family):
                this_index = []
                for j in range(0, len(totalItemList[i])):
                    # print(totalItemList[i][j])
                    value = totalItemList[i][j]
                    this_index.append(self.__wt.index(value)+1)
                    # itemstr = itemstr +" "+  str(this_index+1)
                this_index.sort()
                itemstr = ""
                for i in range(0, len(this_index)):
                    itemstr = itemstr +" "+  str(this_index[i])
                print(f"{i+1}: {itemstr}")
                itemstr = ""


    def _knapsack_dynamic(self):
        start_time = time.time()
        # return self.__knapsack_dynamic_core(self.__max_volume, self.__wt, self.__val, len(self.__val)), time.time()-start_time

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
        return K[cur_index][__max_volume],K

    def __pickKLnapSack(self, W, wt, val, n):
        K = [[0 for w in range(W + 1)]
                for i in range(n + 1)]
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1] <= w:
                    K[i][w] = max(val[i - 1]
                    + K[i - 1][w - wt[i - 1]],
                                K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]
        res = K[n][W]
        # print(res)
        result = res
        item_list = []
        w = W
        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == K[i - 1][w]:
                continue
            else:
                # print(wt[i - 1])
                item_list.append(wt[i - 1])
                res = res - val[i - 1]
                w = w - wt[i - 1]
        return result,item_list

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
    algorithm = Algorithms()

    # W = 100
    # for N in [i*10 for i in range(1, 10)]:
    #     algorithm = Algorithms(N, W)
    #     r_result, r_e_time = algorithm._knapsack_recursive()
    #     d_result, d_e_time = algorithm._knapsack_dynamic()
    #     print(f"N={N} W={W} Rec time = {r_e_time:.8f} DP time = {d_e_time:.8f} max Rec = {r_result} max DP = {d_result}")

    # for N in [i*10 for i in range(1, 101)]:
    #     algorithm = Algorithms(N, W)
    #     r_result, r_e_time = algorithm._knapsack_dynamic()
    #     print(f"{N},{r_e_time}")

    # for N in [i*1 for i in range(1, 100)]:
    #     algorithm = Algorithms(N, W)
    #     r_result, r_e_time = algorithm._knapsack_recursive()
    #     print(f"{N},{r_e_time}")
