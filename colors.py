#!/usr/bin/env python

colors = {
	'MAGENTA' : '\033[95m',
	'BLUE' : '\033[94m',
	'GREEN' : '\033[92m',
	'YELLOW' : '\033[93m',
	'RED' : '\033[91m',
	'GREY' : '\033[90m',
	'WHITE' : '\033[0m',
}

def color(name):
	name = name.upper()

	if name == 'LIST':
		print(color_list())

	if name in colors:
		return colors[name]
	else:
		return None

def color_list():
	return ', '.join((val + c + colors['WHITE']) for (c,val) in colors.items()) + colors['WHITE']
