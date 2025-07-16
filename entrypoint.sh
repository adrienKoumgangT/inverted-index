#!/bin/bash

# Set up hosts file
echo "Updating /etc/hosts"
echo "127.0.0.1 hadoop" >> /etc/hosts

# Format HDFS (only if not already formatted)
if [ ! -d /data/hdfs/namenode/current ]; then
    hdfs namenode -format -force
fi

# Start SSH (required for YARN)
service ssh start

# Start HDFS
start-dfs.sh

# Start YARN
start-yarn.sh

# Start JobHistory
mapred --daemon start historyserver

# Keep the container running
tail -f /dev/null
