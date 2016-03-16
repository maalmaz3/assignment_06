#from utils import check_coincident
#import utils
from .utils import *

class Point(object):

	#Create a point class with three attributes, x, y, and a keyword argument mark. Please place the point pattern class in point.py.
	def __init__(self, x, y, mark={}):
		self.x = x
		self.y = y
		self.mark = mark

	#Add a method to the Point class to chec if another point, passed as an argument, is coincident. Remember that you already wrote this logic.
	def check_coincident(self,other):
		return check_coincident((self.x, self.y), (other.x, other.y))

	#Add a method to shift the point in some direction. This logic is also already written.
	def shift_point(self, dx, dy):
		return shift_point((self.x,self.y),dx,dy)

