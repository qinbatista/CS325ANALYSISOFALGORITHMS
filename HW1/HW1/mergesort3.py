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

    def _merge3sort(self):
        # data_index = 0
        for data_index in range(len(self.__data)):
            start = time.time()
            result = self.Mergesort3(self.__data[data_index],1,len(self.__data[data_index]))
            end = time.time()
            print(result, end-start)
        return result, end-start

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

    def ___merge_sort3_core(self, data):
        # print("data="+str(data))
        if len(data) <= 1:
            return data
        if len(data) <= 2:
            if data[0] < data[1]:
                pass#data[0],data[1]= data[1],data[0]
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

        while left_index < len(left_data) and right_index < len(right_data) and mid_index < len(mid_data):
            if left_data[left_index] <= mid_data[mid_index] and left_data[left_index] <= right_data[right_index]:
                # while left_index <len(left_data):
                data[k] = left_data[left_index]
                left_index += 1
                k += 1
                # if mid_data[mid_index] < right_data[right_index]:
                #     while mid_index < len(mid_data):
                #         data[k] = mid_data[mid_index]
                #         mid_index += 1
                #         k += 1
                # else:
                #     while right_index < len(right_data):
                #         data[k] = right_data[right_index]
                #         right_index += 1
                #         k += 1
            elif mid_data[mid_index] <= left_data[left_index] and mid_data[mid_index] <= right_data[right_index]:
                # while mid_index <len(mid_data):
                data[k] = mid_data[mid_index]
                mid_index += 1
                k += 1
                # if left_data[left_index] < right_data[right_index]:
                #     while left_index < len(left_data):
                #         data[k] = left_data[left_index]
                #         left_index += 1
                #         k += 1
                # else:
                #     while right_index< len(right_data):
                #         data[k] = right_data[right_index]
                #         right_index += 1
                #         k += 1
            elif right_data[mid_index] <= mid_data[mid_index] and right_data[right_index] <= left_data[left_index]:
                # while right_index <len(right_data):
                data[k] = right_data[right_index]
                right_index += 1
                k += 1
                # if left_data[left_index] < mid_data[mid_index]:
                #     while left_index < len(left_data):
                #         data[k] = left_data[left_index]
                #         left_index += 1
                #         k+=1
                # else:
                #     while mid_index < len(mid_data):
                #         data[k] = mid_data[mid_index]
                #         mid_index += 1
                #         k += 1
        if left_index==0 and mid_index==0:
            if left_data[left_index]<mid_data[mid_index]:
                data[k] = left_data[left_index]
                left_index += 1
                k += 1
                data[k] = mid_data[mid_index]
                mid_index += 1
                k += 1
            else:
                data[k] = mid_data[mid_index]
                mid_index += 1
                k += 1
                data[k] = left_data[left_index]
                left_index += 1
                k += 1

        if left_index==0 and right_index==0:
            if left_data[left_index]<right_data[right_index]:
                data[k] = left_data[left_index]
                left_index += 1
                k += 1
                data[k] = right_data[right_index]
                right_index += 1
                k += 1
            else:
                data[k] = right_data[right_index]
                right_index += 1
                k += 1
                data[k] = left_data[left_index]
                left_index += 1
                k += 1

        if mid_index==0 and right_index==0:
            if mid_data[mid_index]<right_data[right_index]:
                data[k] = mid_data[mid_index]
                mid_index += 1
                k += 1
                data[k] = right_data[right_index]
                right_index += 1
                k += 1
            else:
                data[k] = right_data[right_index]
                right_index += 1
                k += 1
                data[k] = mid_data[mid_index]
                mid_index += 1
                k += 1

        # while left_index < len(left_data) :
        #     if left_data[left_index] < mid_data[mid_index]:
        #         data[k] = left_data[left_index]
        #         left_index += 1
        #         k += 1
        #     else:
        #         break

        # while mid_index < len(mid_data):
        #     if mid_data[mid_index] < left_data[left_index]:
        #         data[k] = mid_data[mid_index]
        #         mid_index += 1
        #         k += 1
        #     else:
        #         break
        # while right_index < len(right_data):
        #     if right_data[right_index] < mid_data[right_index]:
        #         data[k] = right_data[right_index]
        #         right_index += 1
        #         k += 1
        #     else:
        #         break

        return data



if __name__ == "__main__":
    algorithm = Algorithms("./data.txt")
    result, duration = algorithm._merge3sort()
    # print(result, duration)
