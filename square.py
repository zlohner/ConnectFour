#!/usr/bin/env python

class Square(object):
	def __init__(self, tag=' '):
		self.tag = tag

	def __str__(self):
		return self.tag

	def __eq__(self, other):
		return self.tag == other.tag

	def key(self):
		if self.tag == ' ':
			return '-'
		else:
			return self.tag
