import random
import time
class Algorithms:
    def __init__(self, __data):
        self.__data = __data
        pass
        # with open(__file_path, 'r') as f:
            # self.__data = f.readlines()
        # self.__data = self.__insert_sort_core([int(i) for i in self.__data[0].replace("\n", "").split(" ")])
    def _merge_sort(self):
        start = time.time()
        result = self.__merge_sort_core(self.__data)
        end = time.time()
        return result, end-start

    def __merge_sort_core(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left_data = data[:mid]
        right_data = data[mid:]
        self.__merge_sort_core(left_data)
        self.__merge_sort_core(right_data)
        left_index = right_index = k = 0
        while left_index < len(left_data) and right_index < len(right_data):
            if left_data[left_index] < right_data[right_index]:
                data[k] = left_data[left_index]
                left_index += 1
            else:
                data[k] = right_data[right_index]
                right_index += 1
            k += 1
        while left_index < len(left_data):
            data[k] = left_data[left_index]
            left_index += 1
            k += 1
        while right_index < len(right_data):
            data[k] = right_data[right_index]
            right_index += 1
            k += 1
        return data

    def _insert_sort(self):
        start = time.time()
        result = self.__insert_sort_core(self.__data)
        end = time.time()
        return result, end-start

    def __insert_sort_core(self, data):
        for i in range(len(data)):
            for j in range(i-1, -1, -1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                else:
                    break
        return data


if __name__ == "__main__":
    bundle = 100
    chunk = 8
    data = [line for line in range(bundle,0,-1)]
    # for times in range(1,bundle//chunk+1):
    algorithm = Algorithms(data[:chunk])
    result, duration = algorithm._merge_sort()
    print(f"{result}	{duration}")

    # print(data[:chunk*times])
    # print(f"{times*chunk}	{duration}",file=open("_merge_sort.txt", "a"))
    # print(result)
    # print(data[:chunk*times])
    result, duration = algorithm._insert_sort()
    # print(f"{times*chunk}	{duration}",file=open("_insert_sort.txt", "a"))
    # print(result)
