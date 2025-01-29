'''
@author Andrea Corriga
@contact me@andreacorriga.com
@date 2018
@version 1.0
'''

import os

'''
 Starting by a dataset name, this function return 
 classes => an array with all classes (subfolders inside dataset folder)
 filename => an array with all images filenames
 xFilepath => an array with all images name with path /dataset/classes_folder/filename.pgm
 y => an array with the relative label of filename||xFilepath
'''
def getDataset(dataset, subset="train"):
	directory = os.path.join(os.getcwd(), "datasets", dataset, subset)

	classes = []
	filename = []
	xFilepath = []
	y = []
	selected_class = ['happy', 'sad', 'neutral','angry','disgust','fear','surprise']
	counts = {class_name: 0 for class_name in selected_class}

    # The subset directory should contain subdirectories for each class
	for class_name in os.listdir(directory):
		class_path = os.path.join(directory, class_name)
		if os.path.isdir(class_path):
			classes.append(class_name)
			for img_file in os.listdir(class_path):
				img_path = os.path.join(class_path, img_file)
				counts[class_name]+=1
				if os.path.isfile(img_path):  # Check if it's a file and not a subdirectory
					xFilepath.append(img_path)
					filename.append(img_file)
					y.append(class_name)
     
	print(counts.items())
	return classes, filename, xFilepath, y


def getPersonalDataset():
	directory = os.getcwd() + "/datasets/personal/"

	x = []

	for root, dirs, files in os.walk(directory):
		for file in files:
			x.append("datasets/personal/" + file)

	return x