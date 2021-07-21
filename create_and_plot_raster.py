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
