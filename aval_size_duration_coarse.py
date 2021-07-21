# varying temporal resolutions
avalanche_counter = 0
size = 0
coarse_graining_range = 8  # up to 8 times as coarse (counts every eight acquisition resolution time bins or time points as a single one)
coarse_graining_interval = 1

avalanche_size_values = []
avalanche_duration_values = []
mean_size_array = []
mean_duration_array = []

print(spikes_time_bin_list)

for x in range(1, coarse_graining_range, coarse_graining_interval):
    coarse_graining_factor = x
    coarse_graining_span = np.zeros(coarse_graining_factor)
    for time_point_counter in range(0, total_time_points, coarse_graining_factor):
        for y in range(0, coarse_graining_factor):
            integer = time_point_counter + y
            coarse_graining_span[y] = integer
        if any(item in coarse_graining_span for item in spikes_time_bin_list):
            avalanche_counter += 1
            for z in coarse_graining_span:
                size += spikes_time_bin_list.count(z)
            if avalanche_counter == 2:
                start = math.floor((time_point_counter - coarse_graining_factor) / coarse_graining_factor)
            if time_point_counter >= total_time_points - coarse_graining_factor and avalanche_counter >= 2:
                #print('Avalanche From ' + str(start) + '-' + str(start + avalanche_counter) + '... size was ' + str(size) + ' and duration was ' + str(avalanche_counter) + ' out of a total of ' + str(total_time_points / coarse_graining_factor) + ' timebins')
                avalanche_duration_values.append(avalanche_counter / (total_time_points / coarse_graining_factor))
                avalanche_size_values.append(size / len(spikes_time_bin_list))
                avalanche_counter = 0
                size = 0
        else:
            if avalanche_counter >= 2:
                #print('Avalanche From ' + str(start) + '-' + str(start + avalanche_counter) + '... size was ' + str(size) + ' and duration was ' + str(avalanche_counter) + ' out of a total of ' + str(total_time_points / coarse_graining_factor) + ' timebins')
                avalanche_duration_values.append(avalanche_counter / (total_time_points / coarse_graining_factor))
                avalanche_size_values.append(size / len(spikes_time_bin_list))
            avalanche_counter = 0
            size = 0
        coarse_graining_span = np.zeros(coarse_graining_factor)
