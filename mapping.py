import sys
import math
from collections import Counter

def total_cost(input_matrix):
	dictornary = {}
	total = 0
	output = open("output.txt",'r')
	input_file = output.read().splitlines()
	input_dicto = map(lambda x: x.split("\t"), input_file)
	#print input_dicto[0][1]
	for i,j in input_dicto:
		dictornary[int(i)] = j
	#print dictornary
	#print input_matrix
	#print input_matrix[0][0]
	#print dictornary[0]
	for i in range(len(input_matrix)):
		x1 = dictornary[input_matrix[i][0]]
		y1 = dictornary[input_matrix[i][1]]
		weight = input_matrix[i][2]
		#print weight
		#print x1[4],y1[4]
		distance = abs((int(y1[1])-int(x1[1])))+abs((int(y1[4])-int(x1[4])))
		#print distance
		total = total + (distance*weight)
	print "The Total Communication cost using this method is ",total
	output.close()

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
			output.write(str(source) + "\t"+str(coordinates[count])+"\n")
			mapped.append(source)
			count +=1
	for i in range(len(input_matrix)):
		j = input_matrix[i]
		destination = j[1]
		if not (destination in mapped):
			output.write(str(destination) + "\t"+str(coordinates[count])+"\n")
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
			output.write(str(source) + "\t"+str(coordinates[middle])+"\n")
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
			output.write(str(destination) + "\t"+str(coordinates[middle])+"\n")
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
			output.write(str(source) + "\t"+str(coordinates[count])+"\n")
			mapped.append(source)
			count -=1
			limit +=1
			if limit == 3:
				count -=1
	for i in range(len(input_matrix)):
		j = input_matrix[i]
		destination = j[1]
		if not (destination in mapped):
			output.write(str(destination) +  "\t"+str(coordinates[count])+"\n")
			mapped.append(destination)
			count -=1
			limit +=1
			if limit == 3:
				count -=1


File = open(sys.argv[1])
output = open("output.txt",'w')
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
n = input("Please select the type of mapping  \n1 --> FIRST ALGORITHM\n2 --> SECOND ALGORITHM\n3 --> THIRD ALGORITHM\nAnything else to quit\n")
if n == 1:
	greedy_mapping(input_matrix,coordinates,total_tasks)
	output.close()
	File.close()
	total_cost(input_matrix)
elif n == 2:
	center(coordinates,input_matrix,total_tasks)
	output.close()
	File.close()
	total_cost(input_matrix)
elif n == 3:
	corner(input_matrix,coordinates,total_tasks)
	output.close()
	File.close()
	total_cost(input_matrix)
else:
	output.close()
	File.close()
	exit()