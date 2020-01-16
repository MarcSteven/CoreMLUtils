import  coremltools
import  numpy as np
model = coremltools.models.MLModel('')

spec = model.get_spec()
print(spec)
layer = spec.neuralNetwork.layers[0]
weight_params = layer.convolution.weights

print("Weights of {} layer:{}.".format(layer.WhichOneOf('layer'),layer.name))
print(np.reshape(np.asarray(weight_params.floatValue),(1,1,3,3)))
