# plot size vs duration for the multiple avalanches at this single temporal resolution (acquisition)
avalanche_size_values_acquisition = avalanche_size_values
avalanche_duration_values_acquisition = avalanche_duration_values

m, b = np.polyfit(avalanche_size_values_acquisition, avalanche_duration_values_acquisition, 1)
plt.scatter(avalanche_size_values_acquisition, avalanche_duration_values_acquisition, color='blue', label='Acquisition - ' + str(m), s=1)
plt.plot(np.unique(avalanche_size_values_acquisition), np.poly1d(np.polyfit(avalanche_size_values_acquisition, avalanche_duration_values_acquisition, 1))(np.unique(avalanche_size_values_acquisition)), color='blue')

# linregress(x, y) ---> THIS IS SUPER NICE FOR GETTING SOME GOOD STATISTICS ON THE PLOTTED VALUES
