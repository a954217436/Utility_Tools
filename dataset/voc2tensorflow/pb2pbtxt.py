
import tensorflow as tf
from tensorflow.python.platform import gfile
from google.protobuf import text_format

def convert_pb_to_pbtxt(filename):
    with gfile.FastGFile(filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')
        tf.train.write_graph(graph_def, './pb_pbtxt', 'res101.pbtxt', as_text=True)
    return

filepath = '/home/ykang/tf-faster/pb_pbtxt/res101.pb'
convert_pb_to_pbtxt(filepath)
