import sys

def coordinate_system(total_tasks):
	max_map = len(total_tasks)
	coordinates = []
	x,y = 0,0
	for x in xrange(max_map-1):
		for y in xrange(max_map-1):
			coordinates.append([x, y])
	return coordinates

def mapping(tasks,coordinates):
	mapped = []
	count = 0
	length = len(coordinates)
	middle = length/2
	#print coordinates[middle]
	horizontal = 3
	vertical = 1
	for key in tasks:
		numbProc = len(tasks[key])
		




input_file = File = open(sys.argv[1])
input_matrix = []
dicto = {}
check_list = []
source_tasks = []
total_task = []
destination_tasks = []
total_tasks = []

temp = input_file.read().splitlines()
input_list =  map(lambda x: x.split("\t"), temp)
for i in range(len(input_list)):
	input_matrix.append([int(input_list[i][0]),int(input_list[i][1]),int(input_list[i][2])])
	source_tasks.append(int(input_list[i][0]))
	destination_tasks.append(int(input_list[i][1]))
	check_list.append([int(input_list[i][0]),int(input_list[i][1])])

total_tasks = source_tasks + destination_tasks
total_tasks = sorted(set(total_tasks))
source_tasks = set(source_tasks)
total_task = list(source_tasks)
for key,values in check_list:
	if key not in dicto:
		dicto[key] = [values]
	else:
		dicto[key].append(values)

coordinates = coordinate_system(total_tasks)
#print coordinates
mapping(dicto,coordinates)
