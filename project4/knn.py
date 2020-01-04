import csv
import math
import matplotlib.pyplot as plt
from csv import reader
from math import sqrt

def load_csv(fileName):
	dataset = list()
	with open(fileName, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	del dataset[0]
	return dataset

def column_toFloat(dataset, column):
	for row in dataset:
		row[column] = float(row[column])

trainset = load_csv('train.txt')
for i in range(len(trainset[0])-1):
	column_toFloat(trainset, i)

testset = load_csv('test.txt')
for i in range(len(testset[0])-1):
	column_toFloat(testset, i)



def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax

def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0


def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)


def get_neighbours(train, test_row, num_neighbours):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbours = list()
	for i in range(num_neighbours):
		neighbours.append(distances[i][0])
	return neighbours


def predict_classification(train, test_row, num_neighbours):
	neighbours = get_neighbours(train, test_row, num_neighbours)
	output_values = [row[-1] for row in neighbours]
	prediction = max(set(output_values), key=output_values.count)
	return prediction


def k_nearest_neighbours(train, test, num_neighbours = 3):
	predictions = list()
	for row in test:
		output = predict_classification(train, row, num_neighbours)
		predictions.append(output)
	return(predictions)


actual = list()
for i in range(len(testset)):
    actual.append(testset[i][-1])


x_axis = list()
y_axis = list() 

k = int(input("Please enter the k value: "))

for k_value in range(k,10):
	x_axis.append(k_value)
	predicted = k_nearest_neighbours(trainset, testset,k_value)
	accuracy = accuracy_metric(actual, predicted)
	y_axis.append(accuracy)

f = plt.figure()
plt.plot(x_axis, y_axis)
plt.xlabel('k values')
plt.ylabel('accuracy(%)')
plt.title('knn mobile price graph')
plt.show()
f.savefig("plot.pdf", bbox_inches='tight')

