#!/bin/sh
checkLog="checklog"

get_df_usage(){
	df -h > $checkLog
	pos=`cat $checkLog | awk '{for(i=1;i<=NF;i++)if($i=="Use%")print i}'`
	if [ "$pos" == "" ];then
		pos=5
	fi
	percent_list=$(cat $checkLog  | awk -v p=$pos '{print $p}' | grep -Eo "[0-9]+")
	echo $percent_list
}

iostat -d -x > $checkLog
pos=`cat $checkLog | awk '{for(i=1;i<=NF;i++)if($i=="%util")print i}'`
echo $pos
if [ "$pos" == "" ];then
        pos=14
fi
percent_list=$(iostat -d -x | awk -v p=$pos '{print $p}' | grep -Eo "[0-9]+")
echo $percent_list
