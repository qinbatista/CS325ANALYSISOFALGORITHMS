"""
Yupeng Qin
April 26 2022
CS325

Reference:
"""
from math import fabs
import random
import time


class Algorithms:
    def __init__(self):
        self.__activity_index = []
        self.__activity_start_time = []
        self.__activity_end_time = []
        self.__length = []
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
        with open("./act.txt") as f:
            lines = f.readlines()
        self._core1(lines,0)
        print("\n")
        self._core1(lines,12)
        print("\n")
        self._core1(lines,16)
        print("\n")
    def _sort_(self,lines):
        for i in range(len(lines)):
            index_i, start_time_i, end_time_i = lines[i].split(" ")
            for j in range(len(lines)-i):
                index_j, start_time_j, end_time_j = lines[j+i].split(" ")
                if int(end_time_i)>int(end_time_j):
                    lines[i], lines[j+i] = lines[j+i], lines[i]

        return lines
    def _core1(self,lines,list_index):
        self.__activity_index = []
        self.__activity_start_time = []
        self.__activity_end_time = []
        if list_index==0:
            print("Set 1")
        if list_index==12:
            print("Set 2")
        if list_index==16:
            print("Set 3")
        cases = lines[list_index]
        lines = self._sort_(lines[list_index+1:list_index+int(cases)+1])
        for index, case in enumerate(range(int(cases))):
            index, start_time, end_time = lines[case].split(" ")
            self.__activity_index.append(int(index))
            self.__activity_start_time.append(int(start_time))
            self.__activity_end_time.append(int(end_time))
        for i in range(len(self.__activity_end_time)):
            self.__length.append(self.__activity_end_time[i] - self.__activity_start_time[i])

        activity_list = []
        data_length = len(self.__activity_end_time)
        min_index = len(self.__activity_end_time)
        next_index= 0
        for i in range(data_length):
            pre = []
            min_index = next_index
            if i ==0:
                last_activity =  max(self.__activity_end_time)
                activity_list.append(self.__activity_index[self.__activity_end_time.index(last_activity)])
                min_index = len(self.__activity_end_time)-1
            min_distance = 99
            for j in range(min_index):
                if min_index-j-1<=0:
                    break
                loop_index = min_index-j-1
                end = self.__activity_end_time[loop_index] #next activity's end time
                start = self.__activity_start_time[min_index] #latest activity's start time
                if end<=start:
                    current_distance = self.__activity_end_time[min_index]- self.__activity_start_time[loop_index]# this activity's distance to previews' activity's distance
                    if min_distance > current_distance:
                        min_distance = current_distance
                        next_index = min_index-j-1

            last_activity_index = self.__activity_end_time[next_index]
            pre.append(self.__activity_start_time[self.__activity_end_time.index(last_activity_index)])
            if len(pre)==1:
                last_activity = pre[0]
                activity_list.append(self.__activity_index[self.__activity_end_time.index(last_activity_index)])
            if next_index<=1:
                break
        print("Maximum number of activities = "+str(len(activity_list)))
        string = ""
        if list_index == 12:
            activity_list.sort(reverse=True)
        else:
            activity_list.sort()
        for i in activity_list:
            string = string+" "+str(i)
        print(string)
        pass

    def _merge3sort(self,__data):
        for _ in range(len(__data)):
            result = self.Mergesort3(__data,1,len(__data))
        return result

    def Mergesort3(self, arr, start, end):
        if len(arr[start -1: end]) < 2:
            return arr
        else:
            mid1 = start + ((end - start) // 3)
            mid2 = start + 2 * ((end-start) // 3)
            self.Mergesort3(arr, start, mid1)
            self.Mergesort3(arr, mid1+1, mid2 + 1)
            self.Mergesort3(arr, mid2+2, end)

            left_array = arr[start -1 : mid1]
            mid_array = arr[mid1: mid2 + 1]
            right_array = arr[mid2 + 1 : end]
            left_array.append(float('inf'))
            mid_array.append(float('inf'))
            right_array.append(float('inf'))
            ind_left = 0
            ind_mid = 0
            ind_right = 0
            for i in range(start-1, end):
                minimum = min([left_array[ind_left], mid_array[ind_mid], right_array[ind_right]])
                if minimum == left_array[ind_left]:
                    arr[i] = left_array[ind_left]
                    ind_left += 1
                elif minimum == mid_array[ind_mid]:
                    arr[i] = mid_array[ind_mid]
                    ind_mid += 1
                else:
                    arr[i] = right_array[ind_right]
                    ind_right += 1

            # self.merge(arr, start, mid1, mid2, end)
            return arr

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
