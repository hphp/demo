
import cPickle

list_l = [0,2,3,1,4,9]
file_t = open('tmp.file','w')
cPickle.dump(list_l,file_t)
file_t = open('tmp.file','r')
test_l = cPickle.load(file_t)
print type(test_l),test_l
