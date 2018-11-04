#! /usr/bin/python3

import sys

node_type = int(sys.argv[1])
task_number = int(sys.argv[2])
mem_fraction = float(sys.argv[3])

import tensorflow as tf

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=mem_fraction)
config = tf.ConfigProto(gpu_options=gpu_options)
config.gpu_options.allow_growth=True

cluster = tf.train.ClusterSpec(
{
"ps": ["172.17.0.2:2223",
       "172.17.0.3:2224"],
"worker": ["172.17.0.1:2222"]
}
)

if node_type == 0:
	server = tf.train.Server(cluster, job_name="ps", task_index=task_number, config=config)
	print("Starting Parameter Server #{}".format(task_number))

elif node_type == 1:
	server = tf.train.Server(cluster, job_name="worker", task_index=task_number, config=config)
	print("Starting Worker Server #{}".format(task_number))
	
server.start()
server.join()

