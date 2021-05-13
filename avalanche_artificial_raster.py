
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import math
import sys
import scipy
from scipy.stats import linregress
from statistics import mean
                                                # GENERATE RASTER
plt.clf()
np.set_printoptions(threshold=sys.maxsize)

# acquisition framerate and time - 45.5 Hz for 10 minutes
num_of_neurons = 10
framerate = 45.5
desired_time_points = 1000
session_duration = desired_time_points / 45.5

total_time_points = math.floor(framerate * session_duration)
hold_array = np.zeros((total_time_points, num_of_neurons))

x = [a for a in range(total_time_points)]

for i in range(0, total_time_points):  # cycles through for the amount of total_time_points
    num_of_neurons_activated = random.randint(num_of_neurons)
    random_time_bin = random.randint(len(x))
    random_time_bin2 = x[random_time_bin]  # random time bin selected for firing (some bins may be chosen twice or none at all)
    for y in range(0, num_of_neurons_activated): # random number of neurons activated at time point
        neuron = random.randint(num_of_neurons)  # randomly selected neurons for firing
        plt.scatter(random_time_bin2, neuron, s=1, color='blue')
        hold_array[random_time_bin2, neuron] = 1

plt.title('Raster of Random Number of Random Neurons Firing', fontsize=10, fontweight='bold')
plt.xlabel('Time (s)', fontsize=9)
plt.ylabel('Neurons', fontsize=9)
plt.locator_params(axis='x', nbins=10)
plt.xticks(x, '')
plt.xscale("log")
plt.show()

                                    # DETERMINE WHERE THERE WAS AN AVALANCHE

hold_array = np.ndarray.flatten(hold_array)

# to read location of spikes in entire vector (array was flattened)
spikes_list = []

starting = 0
while starting < (num_of_neurons * total_time_points):
    if hold_array[starting] == 1:
        spikes_list.append(starting)
        starting += 1
    else:
        starting += 1

# to get general time_bins with activity from spikes_list + which neuron spiked (ROI)
spikes_time_bin_list = []
involved_neurons_list = []

for x in range(0, len(spikes_list)):
    time_bin_involved = math.floor(spikes_list[x] / num_of_neurons)
    spikes_time_bin_list.append(time_bin_involved)
    neuron_involved = math.floor(spikes_list[x] / num_of_neurons)
    neuron_involved2 = spikes_list[x] - (num_of_neurons * neuron_involved)
    involved_neurons_list.append(neuron_involved2)

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

# plot size vs duration for the multiple avalanches at this single temporal resolution (acquisition)
avalanche_size_values_acquisition = avalanche_size_values
avalanche_duration_values_acquisition = avalanche_duration_values

m, b = np.polyfit(avalanche_size_values_acquisition, avalanche_duration_values_acquisition, 1)
plt.scatter(avalanche_size_values_acquisition, avalanche_duration_values_acquisition, color='blue', label='Acquisition - ' + str(m), s=1)
plt.plot(np.unique(avalanche_size_values_acquisition), np.poly1d(np.polyfit(avalanche_size_values_acquisition, avalanche_duration_values_acquisition, 1))(np.unique(avalanche_size_values_acquisition)), color='blue')

# linregress(x, y) ---> THIS IS SUPER NICE FOR GETTING SOME GOOD STATISTICS ON THE PLOTTED VALUES

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
    if coarse_graining_factor == 2:  # plotting the 2x coarse graining values
        m, b = np.polyfit(avalanche_size_values, avalanche_duration_values, 1)
        plt.plot(np.unique(avalanche_size_values), np.poly1d(np.polyfit(avalanche_size_values, avalanche_duration_values, 1))(np.unique(avalanche_size_values)), \
                 color='red')
        plt.scatter(avalanche_size_values, avalanche_duration_values, color='red', label='2x Coarse - ' + str(m), s=1)
        ticks = np.arange(0, max(avalanche_size_values), (max(avalanche_size_values)) / 6)
        plt.xticks(ticks)
        plt.title('Size vs Duration for Avalanches - Acquisition vs 2x Coarse', fontsize=10, fontweight='bold')
        plt.xlabel('Avalanche Size (Normalized to Total Spiking Events)', fontsize=9)
        plt.ylabel('Avalanche Duration (Normalized to Total Time Bins)', fontsize=9)
        plt.locator_params(axis='x', nbins=10)
        plt.xscale("log")
        plt.legend()
        plt.show()
    mean_size_array.append(mean(avalanche_size_values))
    mean_duration_array.append(mean(avalanche_duration_values))
    avalanche_size_values = []
    avalanche_duration_values = []

print(mean_size_array)
print(mean_duration_array)

# plotting mean size vs duration for a variety of different coarse graining

plt.scatter(mean_size_array[0], mean_duration_array[0], color='blue', label='Acquisition', s=7)

for x in range(1, len(mean_size_array)):
    if x != len(mean_size_array)-1:
        plt.scatter(mean_size_array[x], mean_duration_array[x], color='red', s=15)
    else:
        m, b = np.polyfit(mean_size_array, mean_duration_array, 1)
        plt.plot(np.unique(mean_size_array), np.poly1d(np.polyfit(mean_size_array, mean_duration_array, 1))(np.unique(mean_size_array)), \
                 color='black')
        plt.scatter(mean_size_array[x], mean_duration_array[x], color='red', label='Coarse Grained - ' + str(m), s=15)

plt.title('Mean Size vs Duration for Varying Temporal Coarse Graining', fontsize=10, fontweight='bold')
plt.xlabel('Mean Avalanche Size')
plt.ylabel('Mean Duration')
plt.legend()
plt.show()
