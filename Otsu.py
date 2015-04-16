import numpy
import slicer

def button_apply_otsu():
	import numpy
	import slicer
	import Otsu
	import sys
	sys.path.append("C:\Users\Daniel\Desktop\SOFTWARE\PID\TD")
	n = slicer.util.getNode('MRHead')
	data = slicer.util.array('MRHead')
	max = Otsu.optimal_threshold(data)
	data = apply_threshold(data,max)
	n.GetImageData().Modified()
	
	
	

def apply_threshold(data, gray_level):
	for i in xrange(len(data)):
		for j in xrange(len(data[i])):
			for k in xrange(len(data[i][j])):
				if data[i][j][k] < gray_level:
					data[i][j][k] = 0
				else:
					data[i][j][k] = 255
					
	return data
				

def optimal_threshold(data):
	if type(data[0][0][0]) is numpy.ndarray:
		data = convert_to_gray_scale(data)
		
	histogram, _ = numpy.histogram(data, 255)
	total_mean_level = calc_mean_level(data, histogram, 255)
	variance_array = numpy.zeros(255) 
	for gray_level in range(1,255):
		variance_array[gray_level] = calc_variance(data, histogram, gray_level, total_mean_level)
	
	print "variance_array " + str(variance_array)
	print "total_mean_level " + str(total_mean_level)
	print "histogram " + str(histogram)
	print "variance_array.max" + str(variance_array.max())
		
	return numpy_indexof(variance_array,variance_array.max())
	
def numpy_indexof(array, x):
	for i in xrange(len(array)):
		if array[i] == x:
			return i
			

def calc_mean_level(data, histogram, max_gray_level):
	result = 0
	for i in xrange(max_gray_level):
		result += (i+1) * (float(histogram[i]) / (len(data) * len(data[0]) * len(data[0][0])))
		
	return result
	
def calc_variance(data, histogram, gray_level, total_mean_level):
	w_t = calc_probability_up_to(data, histogram, gray_level)
	a = pow(total_mean_level * w_t - calc_mean_level(data, histogram, gray_level), 2)
	b = w_t * (1 - w_t)
	
	return a / b
	
def calc_probability_up_to(data, histogram, gray_level):
	result = 0
	for i in xrange(gray_level):
		result += (float(histogram[i]) / (len(data) * len(data[0]) * len(data[0][0])))
		
	return result
	
def convert_to_gray_scale(data):
	raise RuntimeError("not implemented")