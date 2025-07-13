#!/bin/bash

# Format HDFS (only if not already formatted)
if [ ! -f /data/hdfs/namenode/current/VERSION ]; then
    echo "Formatting HDFS namenode..."
    $HADOOP_HOME/bin/hdfs namenode -format -force
fi

# Start SSH service
service ssh start

# Start Hadoop services
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh
$HADOOP_HOME/sbin/mr-jobhistory-daemon.sh start historyserver

# Keep container running
tail -f $HADOOP_HOME/logs/*