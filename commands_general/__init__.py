from .joke import joke_message
from .invite import invite_message
from .rickroll import rickroll_message
from .facepalm import facepalm_message
from .meme import meme_message

def convert_the_time(time):
	time_units = ['s', 'm', 'h', 'd']

	time_measures = {'s' : 1, 'm' : 60, 'h' : 3600, 'd' : 86400}
	unit = time[-1]

	if unit not in time_units:
		return -1 #Check if the unit is valid at all

	try:
		value = int(time[:-1])

	except:
		return -2 #Error code for non integers

	return value * time_measures[unit]
