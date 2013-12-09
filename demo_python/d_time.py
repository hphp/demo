import time

def strptime():
    a = time.strptime("30 Nov 00", "%d %b %y")
    a = time.strptime("2013-11-20 12:34:33", "%Y-%m-%d %H:%M:%S")
    a = time.strptime("2013-11-20 12:34:33.6", "%Y-%m-%d %H:%M:%S.6")
    #a = time.strptime("2013-11-20 12:34:33.7", "%Y-%m-%d %H:%M:%S.") # does not work
    print a

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
strptime()
