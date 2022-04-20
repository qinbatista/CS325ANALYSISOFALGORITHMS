def dp(MaxTT, QPort, data): # MaxTT == max trip time, QPort == Port Quantity
    min_cost_data = [[-1 for x in range(MaxTT)] for x in range(QPort)]
    stop_data = [[-1 for x in range(MaxTT)] for x in range(QPort)]
    for trip_time in range(MaxTT):
        for port_code in range(trip_time, QPort):
            if trip_time == 0:
                min_cost_data[trip_time][port_code] = data[trip_time][port_code]
                stop_data[trip_time][port_code] = [0 for x in range(QPort)]
                stop_data[trip_time][port_code][trip_time] = 1
                stop_data[trip_time][port_code][port_code] = 1
            elif port_code == trip_time:
                min_cost_data[trip_time][port_code] = min_cost_data[trip_time - 1][port_code]
                stop_data[trip_time][port_code] = list(stop_data[trip_time - 1][port_code])
            else:
                if data[trip_time][port_code] + min_cost_data[trip_time][port_code - 1] < min_cost_data[trip_time - 1][port_code]:
                    min_cost_data[trip_time][port_code] = data[trip_time][port_code] + min_cost_data[trip_time][port_code - 1]
                    stop_data[trip_time][port_code] = list(stop_data[trip_time][trip_time])
                    stop_data[trip_time][port_code][port_code] = 1
                else:
                    min_cost_data[trip_time][port_code] = min_cost_data[trip_time - 1][port_code]
                    stop_data[trip_time][port_code] = list(stop_data[trip_time - 1][port_code])
    answer = []
    answer.append(min_cost_data[MaxTT - 1][QPort - 1])
    for n in range(QPort):
        if stop_data[MaxTT - 1][QPort - 1][n] == 1:
            answer.append(n + 1)
    result = ""
    for index, _mystr in enumerate(answer):
        if index ==0:
            result = str(_mystr)
        else:
            result = result +" "+ str(_mystr)
    return result

if __name__ == '__main__':
    data = [[0, 10, 15, 40], [-1, 0, 5, 15], [-1, -1, 0, 8], [-1, -1, -1, 0]]
    n =int(input())
    for i in range(int(n)):
        for j in range(int(n)):
            data[i][j] = int(input())

    print(dp(n, n, data))