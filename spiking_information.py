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
