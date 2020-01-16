
import coremltools
import coremltools.proto.FeatureTypes_pb2 as ft

spec = coremltools.utils.load_spec("FaceEmotionAddPreprocessArgs.mlmodel")
output = spec.description.output[0]
input = spec.description.input[0]
#delete the first dimension of size 1 to let the coreml know what it is

del output.type.multiArrayType.shape[0]

del input.type.multiArrayType.shape[0]

print(spec.description)
# delete the output of first dimension of size1 to let the CoreML know what it is
print(input)

#del output.type.multiArrayType.shape[0]
print(spec.description)


coremltools.utils.save_spec(spec,"FaceEmotionAddPreprocessArgs.mlmodel")
