
import csv
import numpy

def basic(filname):
    csv_reader = csv.reader(open(filname, "r"), delimiter=",")
    print type(csv_reader)

def read_data_patch_to_ndarray(filname="../data/train.csv", start_line=0, limit=None):

    print "Reading data %s of line[%d,%d)" % (filname, start_line, start_line + limit)
    data = []
    labels = []
    csv_reader = csv.reader(open(filname, "r"), delimiter=",")
    index = 0 
    for index in range(start_line, start_line+limit):
        row = csv_reader[index]
        labels.append(int(row[0]))
        row = row[1:]
        data.append(np.float32(row)/255)

    data_x=np.asarray(data)
    data_y=np.asarray(labels,dtype=np.int32)
    return (data_x, data_y)

basic("dataset.expl")
