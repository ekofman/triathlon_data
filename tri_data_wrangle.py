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


with open('olympic_tri_results.csv', 'r') as results:
	lines = results.readlines()
	headers = lines[0].split(',')

	participants = []

	for line in lines[1:]:
		participant = {}
		for i,element in enumerate(line.split(',')):
			header = headers[i]
			if header in ['Pos','Category', 'Cat Pos', 'Age', 'Gender', 'Gen Pos']:
				participant[header] = element
			elif header in ['Time', 'Swim', 'Bike', 'Run']:
				participant[header] = convert_time_to_seconds(element)
		participants.append(participant)

	for participant in participants:
		print participant