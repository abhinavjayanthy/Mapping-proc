import sys
from collections import Counter

def total_cost():


def coordinate_system(total_tasks):
	max_map = len(total_tasks)
	coordinates = []
	x,y = 0,0
	for x in xrange(max_map-1):
		for y in xrange(max_map-1):
			coordinates.append([x, y])
	return coordinates

def origin(source_task):
	origin = []
	source_task.sort()
	start = Counter(source_task)
	#print start.most_common(1)[0][0]
	origin.append(start.most_common(1)[0][0])
	origin.append(start.most_common(1)[0][0])
	return origin

def hops(source_task,destination_task,weight,input_matrix):
	for i in range(len(source_task)):
		hop.append(destination_task[i]-source_task[i])
		comm_weight.append(hop[i]*weight[i])
		input_matrix[i].append(hop[i])
		input_matrix[i].append(comm_weight[i])
	return input_matrix


def greedy_mapping(input_matrix,coordinates,total_tasks):
	print "GREEDY MAPPING USING [0 0] AS THE CONSTANT"
	mapped = []
	count = 0
	input_matrix.sort(key=lambda x: x[2]) #SORTING BASED ON weight
	#print input_matrix
	for i in range(len(input_matrix)):
		j = input_matrix[i]
		source = j[0]
		if not (source in mapped):
			print str(source) + " task is mapped on to " + str(coordinates[count])
			mapped.append(source)
			count +=1
	for i in range(len(input_matrix)):
		j = input_matrix[i]
		destination = j[1]
		if not (destination in mapped):
			print str(destination) + " task is mapped on to " + str(coordinates[count])
			mapped.append(destination)
			count +=1

def center(coordinates,input_matrix,total_tasks):
	count = 0
	print "MAPPING USING THE CENTER OF THE SET OF CO-ORDINATES"
	mapped = []
	length = len(coordinates)
	middle = length/2
	input_matrix.sort(key=lambda x: x[2],reverse = True) #SORTING BASED ON weight
	#print input_matrix
	for i in range(len(input_matrix)):
		j = input_matrix[i]
		source = j[0]
		if not (source in mapped):
			print str(source) + " task is mapped on to " + str(coordinates[middle])
			mapped.append(source)
			middle +=1
			count +=1
			if count == 3:
				middle +=1
			if middle == length:
				middle = 0
	for i in range(len(input_matrix)):
		j = input_matrix[i]
		destination = j[1]
		if not (destination in mapped):
			print str(destination) + " task is mapped on to " + str(coordinates[middle])
			mapped.append(destination)
			middle +=1
			count +=1
			if count == 3:
				middle +=1
			if middle == length:
				middle = 0

def corner(input_matrix,coordinates,total_tasks):
	print "MAPPING ON THE CORNER MOST CORDINATE SYSTEM"
	limit = 0 
	mapped = []
	count = (len(coordinates) -1)
	input_matrix.sort(key=lambda x: x[2]) #SORTING BASED ON weight
	#print input_matrix
	for i in range(len(input_matrix)):
		j = input_matrix[i]
		source = j[0]
		if not (source in mapped):
			print str(source) + " task is mapped on to " + str(coordinates[count])
			mapped.append(source)
			count -=1
			limit +=1
			if limit == 3:
				count -=1
	for i in range(len(input_matrix)):
		j = input_matrix[i]
		destination = j[1]
		if not (destination in mapped):
			print str(destination) + " task is mapped on to " + str(coordinates[count])
			mapped.append(destination)
			count -=1
			limit +=1
			if limit == 3:
				count -=1


File = open(sys.argv[1])
text_output = open("output.txt",'w')
source_task = []
destination_task = []
weight = []
hop = []
comm_weight = []
input_matrix = []
input_file = File.read().splitlines()
input_list = map(lambda x: x.split("\t"), input_file)
for i in range(len(input_list)):
	input_matrix.append([int(input_list[i][0]),int(input_list[i][1]),int(input_list[i][2])])
	source_task.append(int(input_list[i][0]))
	destination_task.append(int(input_list[i][1]))
	weight.append(int(input_list[i][2]))

total_tasks = source_task + destination_task
total_tasks = sorted(set(total_tasks))
coordinates = coordinate_system(total_tasks)
#print "The coordinates are limited to :"
#print coordinates
start = origin(source_task+destination_task)
#print "The origin is ",start
input_matrix = hops(source_task,destination_task,weight,input_matrix)
greedy_mapping(input_matrix,coordinates,total_tasks)
center(coordinates,input_matrix,total_tasks)
corner(input_matrix,coordinates,total_tasks)