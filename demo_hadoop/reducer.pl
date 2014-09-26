#!/usr/bin/awk -f
#BEGIN {
#num = 0;
#urlstr = ""
#}
#{
#if (NR == 1){
#urlstr = $1;
#num = $2;
#}
#else if (urlstr == $1){
#num += $2;
#}
#else
#{
#print urlstr, num;
#urlstr = $1;
#num = $2;
#}
#}
#END{
#print urlstr, num;
#}
