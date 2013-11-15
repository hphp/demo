
import time

def sys_time():
    print time.time()
    time.sleep(2)
    print time.time()

def cpu_time():
    start_time = time.clock()
    time.sleep(1)
    end_time = time.clock()
    print start_time,end_time,type(start_time),type(end_time)
    print end_time - start_time
    print (end_time - start_time) / 60.
    #print " %.2f " % (end_time - start_time) / 60. # not available
    print " %.2f " % ((end_time - start_time) / 60.) # available
#systime()
#cpu_time()
