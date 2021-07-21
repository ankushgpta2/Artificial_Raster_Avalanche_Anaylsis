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
