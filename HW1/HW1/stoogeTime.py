import random
import time


class Algorithms:
    def __init__(self, data):
        self.__data = data
        # with open(__path, 'r') as f:
            # self.__data = f.readlines()
        # for index in range(len(self.__data)):
            # self.__data[index] = [
                # int(i) for i in self.__data[index].replace("\n", "").split(" ")]

    def _stoogesort(self):
        start = time.time()
        # for data_index in range(len(self.__data)):
        start = time.time()
        result = self.__stoogesort_core(self.__data,0, len(self.__data)-1)
        end = time.time()
        # print(result, end-start)
        return result, end-start

    def __stoogesort_core(self, data, start, end):
        # Check if there are elements in the data
        if start >= end:
            return

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
    quantities = 5
    for quantity in range(1,quantities):
        algorithm = Algorithms([random.randint(0,10000) for i in range(0,100*quantity)])
        result, duration = algorithm._stoogesort()
        print(100*quantity, duration)
