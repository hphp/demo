#!/usr/bin/python
import os

from_dir_route = "/home/hphp/Documents/codes/demo/d_sh/"
to_dir_route = "/home/hphp/Documents/code/demo/demo/demo_sh/"
file_route = "/home/hphp/Documents/codes/demo/python/"

def checkout(from_dir_route, to_dir_route):
    from_dir_list = os.listdir(from_dir_route)
    to_dir_list = os.listdir(to_dir_route)

    for dir_name in from_dir_list:
        if dir_name not in to_dir_list:
            if dir_name[0:2] != "._":
                print dir_name 
                cmd = "mv " + from_dir_route + dir_name + " " + to_dir_route
                os.system(cmd)
        else:
            print from_dir_route + dir_name
            cmd = "diff " + from_dir_route + dir_name + " " + to_dir_route + dir_name
            #print cmd
            os.system(cmd)

def rm_unneccessary(file_route):
    cmd = "rm " + file_route + "._*"
    os.system(cmd)
    filename_list = os.listdir(file_route)
    for filename in filename_list:
        if os.path.isdir(file_route + filename):
            rm_unneccessary(file_route+filename+"/")

rm_unneccessary(file_route)
#checkout(from_dir_route, to_dir_route)
