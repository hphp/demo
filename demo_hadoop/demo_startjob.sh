#!/bin/sh

/home/users/hanjiatong/hadoop-client/hadoop/bin/hadoop fs -D hadoop.job.ugi=mmt-vis,mmt-vis1234 -put hanjiatongfiles hdfs://nj01-nanling-hdfs.dmop.baidu.com:54310/user/mmt-vis/.Trash/
/home/users/hanjiatong/hadoop-client/hadoop/bin/hadoop streaming -jobconf mapred.job.name="hanjiatong-test-job" -jobconf mapred.job.priority=NORMAL -jobconf mapred.reduce.tasks=1 -mapper mapper.sh -reducer reducer.sh -file mapper.sh -file reducer.sh -input /user/mmt-vis/.Trash/hanjiatongfiles -output /user/mmt-vis/.Trash/hanjiatongoutput
