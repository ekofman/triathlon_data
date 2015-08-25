from collections import defaultdict
import numpy as np


def convert_time_to_seconds(readout):
	"""Convert a digital readout like 01:26:30 into total seconds"""
	split_on_colons = readout.split(':')

	hours = 0
	minutes = 0
	seconds = 0

	# Only minutes and seconds have been included
	if len(split_on_colons) == 2:
		minutes = int(split_on_colons[0])
		seconds = int(split_on_colons[1])
	elif len(split_on_colons) == 3:
		hours = int(split_on_colons[0])
		minutes = int(split_on_colons[1])
		seconds = int(split_on_colons[2])

	total_seconds = seconds + 60*minutes + 3600*hours
	return total_seconds

def parse_triathlon_data(filename):
	participants = []			
	with open(filename, 'r') as results:
		lines = results.readlines()
		headers = lines[0].split(',')

		for line in lines[1:]:
			participant = {}
			for i,element in enumerate(line.split(',')):
				header = headers[i]
				if header in ['Pos','Category', 'Cat Pos', 'Age', 'Gender', 'Gen Pos']:
					if element == 'Male':
						element = 1
					elif element == 'Female':
						element = 0
					participant[header] = element
				elif header in ['Time', 'Swim', 'Cycle', 'Run']:
					participant[header] = convert_time_to_seconds(element)
			participants.append(participant)

	return participants
	
def output_csv(participants):
	"""Make a csv file with the processed data"""
	with open('processed_data.csv', 'w+') as processed:
		for i,key in enumerate(participants[0]):
			processed.write(key)
			if i < (len(participants[0]) - 1):
				processed.write(',')
		processed.write('\n')
		for participant in participants:
			for i,key in enumerate(participant):
				processed.write(str(participant[key]))
				if i < (len(participant) - 1):
					processed.write(',')
			processed.write('\n')

def main():
	participants = parse_triathlon_data('olympic_tri_results.csv')
	output_csv(participants)

if __name__ == '__main__':
	main()