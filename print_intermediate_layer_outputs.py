
import coremltools
import copy
import coremltools.proto.FeatureTypes_pb2 as ft


#grap the spec for the model
model = coremltools.models.MLModel("")
spec = model._spec
print(spec.WhichOneOf("Type"))

layers = copy.deepcopy(spec.neuralNetworkClassifier.layer)
preprocessing  = copy.deepcopy(spec.neuralNetworkClassifier.preprocessing)

# Assign them to spec's neuralNetwork
spec.neuralNetwork.layers.extend(layers)
spec.neuralNetwork.preprocessing.extend(preprocessing)

#remove old print



# add output for the final layer so that you can compile the model again
spec.description.output.add()
spec.description.output[-1].name = spec.neuralNetwork.layer[-1].output[0]
spec.description.output[-1].type.multiArrayType = ft.ArrayFeatureType.DOUBLE



new_model = coremltools.models.MLModel(spec)

