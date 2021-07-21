# to get the avalanche size (number of spikes) and duration across time bins for acquisition resolution
avalanche_counter = 0
size = 0

avalanche_duration_values = []
avalanche_size_values = []

for x in range(0, total_time_points):
    if x in spikes_time_bin_list:
        avalanche_counter += 1
        size += spikes_time_bin_list.count(x)
        if avalanche_counter == 2:
            start = x-1
        if x == total_time_points - 1 and avalanche_counter >= 2:
            #print('duration of ' + str(avalanche_counter) + ' from ' + str(start) + '-' + str(x) + ' with size of ' + str(size))
            avalanche_duration_values.append(avalanche_counter / total_time_points)
            avalanche_size_values.append(size / len(spikes_time_bin_list))
    else:
        if avalanche_counter >= 2:
            #print('duration of ' + str(avalanche_counter) + ' from ' + str(start) + '-' + str(x) + ' with size of ' + str(size))
            avalanche_duration_values.append(avalanche_counter / total_time_points)
            avalanche_size_values.append(size / len(spikes_time_bin_list))

            avalanche_counter = 0
            size = 0
