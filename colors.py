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

def getColor(colorStr):
	colorStr = colorStr.upper()

	if colorStr == 'LIST':
		print colorList()

	if colorStr == 'pink':
		colorStr = 'magenta'

	if colorStr in colors:
		return colors[colorStr]
	else:
		return None

def colorList():
	return ', '.join((val + c + colors['WHITE']) for (c,val) in colors.items()) + colors['WHITE'];
