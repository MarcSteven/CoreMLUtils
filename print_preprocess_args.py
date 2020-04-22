
import coremltools


spec = coremltools.models.utils.load_spec("FacialExpressionAnalysisTest11.mlmodel")

# Get neural network portion of the spec
if spec.WhichOneof('Type') == 'neuralNetworkClassifier':
  nn = spec.neuralNetworkClassifier
if spec.WhichOneof('Type') == 'neuralNetwork':
  nn = spec.neuralNetwork
elif spec.WhichOneof('Type') == 'neuralNetworkRegressor':
  nn = spec.neuralNetworkRegressor
else:
    raise ValueError('MLModel must have a neural network')

print(nn.preprocessing)

preprocessing == nn.preprocessing[0].scaler

print('channel scale:',preprocessing.channelScale)
print('blue bias:' ,preprocessing.blueBias)
print('green bias:',preprocessing.greenBias)
print('red bis:',preprocessing.redBias)

#print(nn.preprocessing)
