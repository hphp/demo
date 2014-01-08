
import os
f_list = os.listdir("./")
for filename in f_list:
    l = filename.split(".")
    if l[-1] == "txt":
        newname = ".".join((l[0],"gt",l[1]))
        os.rename(filename, newname)
