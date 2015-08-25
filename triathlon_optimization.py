import argparse
import random
import math

SWIM_M_S = .0945
RUN_M_S = 3.6
BIKE_M_S = 9.99

SWIM_CAL_S = .2142
RUN_CAL_S = .3042
BIKE_CAL_S = .405

SWIM_STD_S_M = .174
RUN_STD_S_M = .0449
BIKE_STD_S_M = .0099

"""
We want to minimize:
max(std(swimming), std(running), std(biking s)) - min(std(swimming), std(running), std(biking s))

max(.174*swim_meters, .0449*run_meters, .0099*bike_meters) 
-min(.174*swim_meters, .0449*run_meters, .0099*bike_meters)

AND
max(cal(swimming), cal(running), cal(biking)) - min(cal(swimming), cal(running), cal(biking))
max()
"""

def get_seconds_from_meters(meters, meters_per_second):
	return float(meters) / float(meters_per_second)

def get_calories_from_seconds(seconds, calories_per_second):
	return seconds * calories_per_second

def get_f_derivative(swim_std_s, run_std_s, bike_std_s):
	derivatives = {'run_std_s': None, 'bike_std_s': None}
	if (run_std_s <= swim_std_s and swim_std_s <= bike_std_s):
		derivatives['run_std_s'] = -1
		derivatives['bike_std_s'] = 1
	if (run_std_s <= bike_std_s and bike_std_s <= swim_std_s): 
		derivatives['run_std_s'] = -1
		derivatives['bike_std_s'] = 0

	if (bike_std_s <= swim_std_s and swim_std_s <= run_std_s):
		derivatives['run_std_s'] = 1
		derivatives['bike_std_s'] = -1
	if (bike_std_s <= run_std_s and run_std_s <= swim_std_s): 
		derivatives['run_std_s'] = 0
		derivatives['bike_std_s'] = -1

	if (swim_std_s <= bike_std_s and bike_std_s <= run_std_s):
		derivatives['run_std_s'] = 1
		derivatives['bike_std_s'] = 0
	if (swim_std_s <= run_std_s and run_std_s <= bike_std_s): 
		derivatives['run_std_s'] = 0
		derivatives['bike_std_s'] = 1
	return derivatives

def run_simulation(swim_meters):
	"""Calculate the optimal run and bike meters based on the swim meters"""
	# Seed the starting values for run and bike distance
	random.seed()

	run_meters = random.randint(0, 30000)
	bike_meters = random.randint(0, 60000)
	run_meters_old = 0
	bike_meters_old = 0
	run_meters_really_old = 0
	bike_meters_really_old = 0

	precision = 10
	gamma = 1

	while (math.sqrt(math.pow((run_meters- run_meters_old),2) + (math.pow((bike_meters - bike_meters_old),2))) > precision):

		if run_meters_really_old == run_meters and bike_meters_really_old == bike_meters:
			break
			
		swim_std_s = swim_meters * SWIM_STD_S_M
		run_std_s = run_meters * RUN_STD_S_M
		bike_std_s = bike_meters * BIKE_STD_S_M

		print 'swim: {}, run: {} , bike: {}'.format(swim_meters, run_meters, bike_meters)
		print 'swim_std {}, run_std {}, bike_std {}'.format(swim_std_s, run_std_s, bike_std_s)

		# Gradient depends on the relative values of each standard deviation
		f_derivative = get_f_derivative(swim_std_s, run_std_s, bike_std_s)
		run_std_old = run_std_s
		bike_std_old = bike_std_s
		run_std_s = run_std_old - gamma * f_derivative['run_std_s']
		bike_std_s = bike_std_old - gamma * f_derivative['bike_std_s']

		run_meters_really_old = run_meters_old
		bike_meters_really_old = bike_meters_old
		run_meters_old = run_meters
		bike_meters_old = bike_meters
		run_meters = run_std_s / RUN_STD_S_M
		bike_meters = bike_std_s / BIKE_STD_S_M


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Get triathlon optimization parameters')
	parser.add_argument('swim_meters', metavar='s', type=int)
	
	args = parser.parse_args()

	swim_meters = args.swim_meters

	run_simulation(swim_meters)
