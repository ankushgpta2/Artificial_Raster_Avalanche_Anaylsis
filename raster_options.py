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
