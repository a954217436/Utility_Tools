from tensorflow.python import pywrap_tensorflow
checkpoint_path = '/home/ykang/tf-faster/output/res101/voc_2007_trainval/default/res101_faster_rcnn_iter_40000.ckpt'
reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()
for key in var_to_shape_map:
    print("tensor_name: ", key)
 
