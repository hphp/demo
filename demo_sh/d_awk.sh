#!/bin/sh

test_awk_time_math(){
    awk -F ']' '{
        split($1,a,":");
        split($2,b,":");
        time_a=a[1]*3600+a[2]*60+a[3]*1
        time_b=b[1]*3600+b[2]*60+b[3]*1
        print time_a","time_b","time_b-time_a
    }' time_c
}
test_awk_time_math

test_awk_output_to_array(){
    s=`echo | awk '{while(i<30)print i++}'`
    echo ${#s[@]} # 1
    s=(`echo | awk '{while(i<30)print i++}'`)
    echo ${#s[@]} # 30 
}
#test_awk_output_to_array

test_awk_get_first_line(){
    s=$(echo "good bad" echo "bad2 good2" | awk 'NR>1{exit};{print $2}')
    echo $s
}
#test_awk_get_first_line

test_awk_variable(){
#root="/ddd"
#awk -v r=$root '{print r}' main.sh
hostname="update2.dlied.qq.com"
#tail -n 100 nws.conf | awk -F ' ' '{if(($1=="vhost")&&($3=="update2.dlied.qq.com")){print $4}}' | awk -F '=' '{print $2}'
tail -n 100 nws.conf | awk -F ' ' -v host=$hostname '{if(($1=="vhost")&&($3==host)){print $4}}' | awk -F '=' '{print $2}'
}
#test_awk_variable

test_awk_input_variable(){
    t_path="/minigamefile/mission/Mission81_23.cab"
    t_path="/dl_dir3.qq.com/minigamefile/mission/Mission81_23.cab"
    echo $t_path | awk -F '/' '{print $2}'
}
#test_awk_input_variable
test_awk_output(){
    
    t_path="/dl_dir3.qq.com/minigamefile/mission/Mission81_23.cab"
    xx=$(echo $t_path | awk -F '/' '{print $2}')
    echo $xx
}
#test_awk_output
get_localdir(){
    hostname=$1
    #echo get_localdir_hostname:$hostname
    localfile=$(tail -n 100 nws.conf | awk -F ' ' -v host=$hostname '{if(($1=="vhost")&&($3==host)){print $4}}' | awk -F '=' '{print $2}')
    echo $localfile
}
test_awk_output2(){
    h="update2.dlied.qq.com"
    localfile=$(get_localdir $h)
    echo $localfile
}
#test_awk_output2

test_number_of_fields_v(){
    #NF means number of fields
    str="a/b/c/d/e/f/g"
    num=$(echo $str | awk -F '/' '{print NF}')
    #seperate each part and get it to variable
    echo $num
    for (( i = 0 ; i < $num ; i ++ ))
    do
        dir=$(echo $str | awk -F '/' -v x=$(expr $i + 1) '{print $x}')
        echo $dir
    done
}
#test_number_of_fields_v
