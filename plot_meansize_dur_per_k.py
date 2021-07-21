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
