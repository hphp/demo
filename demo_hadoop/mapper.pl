#!/usr/bin/awk -f
#{
#urlstr = $13;
#if(index(urlstr,"http://") == 2 ){
#urlstr = substr(urlstr, 9, length(urlstr)-2);
#}else{
#urlstr = substr(urlstr, 2, length(urlstr)-2);
#}
#theindex=index(urlstr, "/");
#if(theindex = 0){
#urlstr = substr(urlstr,1,theindex-1);
#}
#sortarray[urlstr]++;
#}
#END {
#for(i in sortarray)
#print i, sortarray[i];
#}
