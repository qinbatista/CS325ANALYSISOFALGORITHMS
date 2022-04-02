import random
import time


class Algorithms:
    def __init__(self, __path):
        # self.__data = __data
        # pass
        with open(__path, 'r') as f:
            self.__data = f.readlines()
        for index in range(len(self.__data)):
            self.__data[index] = [
                int(i) for i in self.__data[index].replace("\n", "").split(" ")]
        self.__Merge3_divider = 3

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

    def Merge3(self):
        data_index = 0
        start = time.time()

        result = self.__merge_sort3_core(self.__data[data_index])

        end = time.time()
        return result, end-start

    def __merge_sort3_core(self, data):
        print("data="+str(data))
        if len(data) <= 1:
            return data
        if len(data) <= 2:
            if data[0] < data[1]:
                data[0],data[1]= data[1],data[0]
            else:
                data[1],data[0]= data[0],data[1]
            return data
        # base_divisor = 0
        divider = len(data) // 3
        # if len(data) >3:
            # base_divisor = 3
        if len(data) == 2:
            divider=1
        left_data = data[:divider]
        mid_data = data[divider:2*divider]
        right_data = data[2*divider:]


        self.__merge_sort3_core(left_data)
        self.__merge_sort3_core(mid_data)
        self.__merge_sort3_core(right_data)
        left_index = mid_index = right_index = k = 0
        # while left_index < len(left_data) and mid_index < len(mid_data) and right_index < len(right_data):
        #     if left_data[left_index] < mid_data[mid_index] and left_data[left_index] < right_data[right_index]:
        #         data[k] = left_data[left_index]
        #         left_index += 1
        #     if mid_data[mid_index] < left_data[left_index] and mid_data[mid_index] < right_data[right_index]:
        #         data[k] = mid_data[mid_index]
        #         mid_index += 1
        #     if right_data[right_index] < left_data[left_index] and right_data[right_index] < mid_data[mid_index]:
        #         data[k] = right_index[right_index]
        #         right_index += 1

        # while mid_index < len(mid_data) and right_index < len(right_index):
        #     if mid_data[mid_index] < left_data[left_index] and mid_data[mid_index] < right_data[right_index]:
        #         data[k] = mid_data[mid_index]
        #         mid_index += 1
        #     if right_index[right_index] < left_data[left_index] and right_index[right_index] < mid_data[mid_index]:
        #         data[k] = right_index[right_index]
        #         mid_index += 1

        while left_index < len(left_data) and right_index < len(right_data) and mid_index < len(mid_data):
            if left_data[left_index] < mid_data[mid_index] and left_data[left_index] < right_data[right_index]:
                while left_index <len(left_data):
                    data[k] = left_data[left_index]
                    left_index += 1
                    k += 1
                if mid_data[mid_index] < right_data[right_index]:
                    while mid_index < len(mid_data):
                        data[k] = mid_data[mid_index]
                        mid_index += 1
                        k += 1
                else:
                    while right_index < len(right_data):
                        data[k] = right_data[right_index]
                        right_index += 1
                        k += 1
            elif mid_data[mid_index] < left_data[left_index] and mid_data[mid_index] < right_data[right_index]:
                while mid_index <len(mid_data):
                    data[k] = mid_data[mid_index]
                    mid_index += 1
                    k += 1
                if left_data[left_index] < right_data[right_index]:
                    while left_index < len(left_data):
                        data[k] = left_data[left_index]
                        left_index += 1
                        k += 1
                else:
                    while right_index< len(right_data):
                        data[k] = right_data[right_index]
                        right_index += 1
                        k += 1
            elif right_data[mid_index] < mid_data[mid_index] and right_data[right_index] < left_data[left_index]:
                while right_index <len(right_data):
                    data[k] = right_data[right_index]
                    right_index += 1
                    k += 1
                if left_data[left_index] < mid_data[mid_index]:
                    while left_index < len(left_data):
                        data[k] = left_data[left_index]
                        left_index += 1
                        k+=1
                else:
                    while mid_index < len(mid_data):
                        data[k] = mid_data[mid_index]
                        mid_index += 1
                        k += 1

        while left_index < len(left_data):
            # if left_data[left_index] < mid_data[mid_index]:
                data[k] = left_data[left_index]
                left_index += 1
                k += 1
            # else:
                # break

        while mid_index < len(mid_data):
            # if mid_data[mid_index] < left_data[left_index]:
                data[k] = mid_data[mid_index]
                mid_index += 1
                k += 1
            # else:
                # break
        while right_index < len(right_data):
            # if right_data[right_index] < mid_data[right_index]:
                data[k] = right_data[right_index]
                right_index += 1
                k += 1
            # else:
                # break
        return data

    def Mergesort3(self, data):
        print("data="+str(data))
        if len(data) <= 1:
            return data
        merge3_data = []
        divided_position = len(data)//self.__Merge3_divider
        for i in range(self.__Merge3_divider):
            if i == self.__Merge3_divider-1:
                merge3_data.append(data[i*divided_position:])
            else:
                merge3_data.append(
                    data[i*divided_position:(i+1)*divided_position])

        for i in range(len(merge3_data[i])+1):
            if len(merge3_data[i]) == 2:
                merge3_data[i].append(-999999)
            self.Mergesort3(merge3_data[i])

        index = []
        for i in range(self.__Merge3_divider):
            index.append(0)

        k = 0
        # while index[0]< len(merge3_data[0]) and index[1]< len(merge3_data[1]) and index[2]< len(merge3_data[2]):
        #     smallest_value = min(merge3_data)
        #     data[k] = smallest_value[0]
        #     index[merge3_data.index(smallest_value)]+=1
        #     k+=1
        while index[0] < len(merge3_data[0]) and index[1] < len(merge3_data[1]) and index[2] < len(merge3_data[2]):
            for j in range(self.__Merge3_divider):
                for i in range(j, self.__Merge3_divider-1):
                    if merge3_data[j] > merge3_data[i+1]:
                        merge3_data[j], merge3_data[i +
                                                    1] = merge3_data[i+1], merge3_data[j]
                        index[j], index[i] = index[i], index[j]
                        index[j] += 1
            k += 1
        # while index[0]< len(merge3_data[0]):
        #     data[k] = merge3_data[0][index[0]]
        #     index[0]+=1
        #     k+=1
        # while index[1]< len(merge3_data[1]):
        #     data[k] = merge3_data[1][index[1]]
        #     index[1]+=1
        #     k+=1
        # while index[2]< len(merge3_data[2]):
        #     data[k] = merge3_data[2][index[2]]
        #     index[2]+=1
        #     k+=1

        # for i in range(self.__Merge3_divider):
        #     while index[i] < len(merge3_data[i]):
        #         data[k] = merge3_data[i][index[i]]
        #         index[i] += 1
        #         k += 1
        print(data)
        return merge3_data


if __name__ == "__main__":
    algorithm = Algorithms("./data.txt")
    result, duration = algorithm.Merge3()
    print(result, duration)
