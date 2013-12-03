
import csv
import numpy as np

def basic(filname):
    csv_reader = csv.reader(open(filname, "r"), delimiter=",")
    print type(csv_reader) # a csv reader instance , no len() function.

def read_data_patch_to_ndarray(filname="../data/train.csv", start_line=0, limit=None):

    print "Reading data %s of lines %s from starting line %d" % (filname, str(limit), start_line)
    data = []
    labels = []
    csv_reader = csv.reader(open(filname, "r"), delimiter=",")
    index = -1 
    for row in csv_reader:
        index += 1
        if index < start_line:
            continue
        if (limit != None) :
            if (index >= (start_line+limit)):
                break
        labels.append(int(row[0]))
        row = row[1:]
        data.append(np.float32(row)/255)

    data_x=np.asarray(data)
    data_y=np.asarray(labels,dtype=np.int32)
    return (data_x, data_y)

#basic("dataset.expl")
dataset = read_data_patch_to_ndarray("dataset.expl",1,4)
#dataset = read_data_patch_to_ndarray("dataset.expl",1)
#dataset = read_data_patch_to_ndarray("dataset.expl")
print dataset[0].shape, dataset[1].shape
print dataset
