#//
#//  onnx_convert_coreml.py
#//  AntsFaceDemo
#//
#//  Created by Marc Zhao on 2019/12/25.
#//  Copyright © 2019 AntsNetwork. All rights reserved.
#//


from onnx_coreml import convert
import sys
from onnx import onnx_pb
import onnx


 
model_in = "torch_model_20191205.onnx"
model_out = "FaceEmotion20200109.mlmodel"
#print the model list here
model = onnx.load(model_in)
print(onnx.helper.printable_graph(model.graph))

args = dict(
     image_scale = 1/255.0,
     red_bias = -0.485 ,
     green_bias = -0.456 ,
     blue_bias = -0.406  ,
      )

coreml_model = convert(model_in,preprocessing_args = args,
minimum_ios_deployment_target = '13')
coreml_model.save('FaceEmotion20200109.mlmodel')




