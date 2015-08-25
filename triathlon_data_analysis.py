import numpy as np

SWIM_COL = 1
RUN_COL = 2
CYCLE_COL = 9

# distances in meters
SWIM_DISTANCE = 1500
RUN_DISTANCE = 10000
CYCLE_DISTANCE = 40000
def main():
	#read in  data, parse into training and target sets
	dataset = np.genfromtxt(open('processed_data.csv', 'r'), delimiter=',', dtype='f8')[1:]  
	swim_std = np.std(dataset[:, SWIM_COL])
	run_std = np.std(dataset[:, RUN_COL])
	cycle_std = np.std(dataset[:, CYCLE_COL])

	print 'Swim standard deviation (min): ' + str(swim_std/60)
	print 'Bike standard deviation (min): ' + str(cycle_std/60)
	print 'Run standard deviation (min): ' + str(run_std/60)

	swim_mean = np.mean(dataset[:, SWIM_COL])
	run_mean = np.mean(dataset[:, RUN_COL])
	cycle_mean = np.mean(dataset[:, CYCLE_COL])

	print 'Swim mean (min): ' + str(swim_mean/60)
	print 'Run mean (min): ' + str(run_mean/60)
	print 'Cycle mean (min): ' + str(cycle_mean/60)
	print '\n'

	swim_velocity_mean = SWIM_DISTANCE / (swim_mean)
	run_velocity_mean = RUN_DISTANCE / (run_mean)
	cycle_velocity_mean = CYCLE_DISTANCE / (cycle_mean)

	print 'Swim speed (m/s): ' + str(swim_velocity_mean)
	print 'Run speed (m/s): ' + str(run_velocity_mean)
	print 'Cycle speed (m/s): ' + str(cycle_velocity_mean)
if __name__ == '__main__':
	main()