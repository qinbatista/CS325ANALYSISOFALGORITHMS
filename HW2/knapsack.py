"""
Yupeng Qin
April 13 2022
CS325

Reference:
Stooge Sort. geeksforgeeks. https://www.geeksforgeeks.org/stooge-sort/
"""
import random
import time
class Algorithms:
    def __init__(self, __path):
        with open(__path, 'r') as f:
            self.__data = f.readlines()
        for index in range(len(self.__data)):
            self.__data[index] = [
                int(i) for i in self.__data[index].replace("\n", "").split(" ")]
        for index in range(len(self.__data)):
            self.__data[index].pop(0)
            # print(self.__data[index])

    def _stoogesort(self):
        start = time.time()
        for data_index in range(len(self.__data)):
            start = time.time()
            result = self.__stoogesort_core(self.__data[data_index],0, len(self.__data[data_index])-1)
            end = time.time()
            # print(result)
            print(" ".join(map(str,result)))
        return result, end-start

    def __stoogesort_core(self, data, start, end):
        # Check if there are elements in the data
        if start >= end:
            return data

        # Check first element with the last element
        if data[start]>data[end]:
            temp = data[start]
            data[start] = data[end]
            data[end] = temp

        # Check if the number of elements are more than 2
        if end-start+1 > 2:
            temp = (int)((end-start+1)/3)
            # Recursively call the parts of data to be sorted
            self.__stoogesort_core(data, start, (end-temp))
            self.__stoogesort_core(data, start+temp, (end))
            self.__stoogesort_core(data, start, (end-temp))
        return data




if __name__ == "__main__":
    algorithm = Algorithms("./data.txt")
    result, duration = algorithm._stoogesort()
    # print(result, duration)
