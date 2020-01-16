
import onnxmltools
import coremltools

#load a coreml model
coreml_model = coremltools.utils.load_spec('HumanEmotions.mlmodel')

# convert the coreML model into ONNX
onnx_model = onnxmltools.convert_coreml(coreml_model,'example model')

# save as protobuf
onnxmltools.utils.save_model(onnx_model,'emotion.onnx')

