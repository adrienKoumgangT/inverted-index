FROM ubuntu:24.04

ENV DEBIAN_FRONTEND noninteractive

# Install Java 8, python3, dependencies and utilities
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    sudo openssh-server openjdk-8-jdk \
    python3 python3-pip python3-venv \
    curl wget vim nano ssh pdsh rsync net-tools iputils-ping && \
    mkdir -p /opt && \
    rm -rf /var/lib/apt/lists/*

# Auto-detect Java path (for both amd64/arm64)
RUN JAVA_PATH=$(dirname $(dirname $(readlink -f $(which java)))) && \
    echo "Java detected at: $JAVA_PATH" && \
    ln -s $JAVA_PATH /usr/lib/jvm/default-java

ENV JAVA_HOME /usr/lib/jvm/default-java

# Set Python alternatives
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

ENV PYSPARK_PYTHON /usr/bin/python3

# Configure SSH
RUN ssh-keygen -t rsa -P '' -f /root/.ssh/id_rsa && \
    cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys && \
    chmod 0600 /root/.ssh/authorized_keys

# Set environment variables
ENV HADOOP_VERSION 3.4.1
ENV HADOOP_HOME /opt/hadoop
ENV HADOOP_CONF_DIR $HADOOP_HOME/etc/hadoop
ENV PATH $PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV HDFS_NAMENODE_USER root
ENV HDFS_DATANODE_USER root
ENV HDFS_SECONDARYNAMENODE_USER root
ENV HDFS_JOURNALNODE_USER root
ENV YARN_RESOURCEMANAGER_USER root
ENV YARN_NODEMANAGER_USER root

# Download and extract Hadoop
RUN wget https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz -P /opt && \
    tar -xzf /opt/hadoop-${HADOOP_VERSION}.tar.gz -C /opt && \
    mv /opt/hadoop-${HADOOP_VERSION} $HADOOP_HOME && \
    rm /opt/hadoop-${HADOOP_VERSION}.tar.gz

# Configure Hadoop for pseudo-distributed mode
COPY hadoop-configs/* $HADOOP_CONF_DIR

# Create data directories
RUN mkdir -p /data/hdfs/namenode && \
    mkdir -p /data/hdfs/datanode && \
    mkdir -p /opt/hadoop/logs

# Set JAVA_HOME in hadoop-env.sh
# RUN sed -i "s|^\(export JAVA_HOME=\).*|\1$JAVA_HOME|" $HADOOP_HOME/etc/hadoop/hadoop-env.sh
RUN echo "export JAVA_HOME=$JAVA_HOME" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh

# Expose necessary ports
EXPOSE 19888 9870 9867 9866 9864 9000 8088 8042 8040 8033 8032 8031 8030 8020

# CMD ["/bin/bash"]

# Entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
