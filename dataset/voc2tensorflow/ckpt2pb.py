import tensorflow as tf
#from create_tf_record import *
from tensorflow.python.framework import graph_util

def freeze_graph(input_checkpoint,output_graph):
	output_node_names = "resnet_v1_101/rpn_bbox_pred/biases,resnet_v1_101/bbox_pred/weights,resnet_v1_101/rpn_cls_score/biases,resnet_v1_101/rpn_cls_score/weights"
	saver = tf.train.import_meta_graph(input_checkpoint + '.meta', clear_devices=True)
	graph = tf.get_default_graph() 
	input_graph_def = graph.as_graph_def() 
	with tf.Session() as sess :
		saver.restore(sess, input_checkpoint) 
		output_graph_def = graph_util.convert_variables_to_constants(sess=sess,input_graph_def=input_graph_def,output_node_names=output_node_names.split(","))
		with tf.gfile.GFile(output_graph, "wb") as f: 
			f.write(output_graph_def.SerializeToString()) 
		print("%d ops in the final graph." % len(output_graph_def.node)) 
 


input_checkpoint = "/home/ykang/tf-faster/scripts/ckpt/vgg16_faster_rcnn_iter_300.ckpt"
out_pb_path = "/home/ykang/tf-faster/pb_pbtxt/res101.pb"

freeze_graph(input_checkpoint, out_pb_path)
