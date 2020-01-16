import  numpy as np
import  coremltools.proto.FeatureTypes_pb2 as ft
def printTop5(resultsDict):
    # put probabilities and labels into their own lists
    probs = np.array(list(resultsDict.values()))
    labels = list(resultsDict.keys())
    # find the indices of the 5 classes with the highest probabilities
    top5Probs = probs.argsort()[-5:][::-1]

    # find the corresponding labels and probabilities
    top5Results = map(lambda x:labels[x],probs[x],top5Probs)
    #print them from high to low
    for label,prob in top5Results:
        print("%.5f %s" %(prob,label))

def get__nn(spec):
      if spec.WhichOneOf('Type') == 'neuralNetwork':
        return  spec.neuralNetwork
      elif spec.WhichOneOf('Type') == 'neuralNetworkClassifier':
          return  spec.neuralNetworkClassifier
      elif spec.WhichOneOf('Type') == 'neuralNetworkRegressor':
          return  spec.neuralNetworkRegressor
      else:
          raise  ValueError("MLModel does not have a neural network")
        
def convert_multiArray_to_image(feature,is_bgr= False):
    import  coremltools.proto.FeatureType_pb2 as ft
    if feature.type.WhichOneOf("Type") != "multiArrayType":
        raise  ValueError("%s is not a multiArray type" % feature.name)
    shape = tuple(feature.type.multiArrayType.shape)
    channels = None
    if len(shape) == 2:
        channels = 1
        height,width = shape
    elif len(shape) == 3:
        channels,height,width = shape
    if channels != 1 and channels != 3:
        raise  ValueError("Shape{} not supported for image type".format(shape))
    if channels == 1:
        feature.type.imageType.colorSpace = ft.ImageFeatureType.GRAYSCALE
    elif channels == 3:
        if is_bgr:
            feature.type.imageType.colorSpace = ft.ImageFeatureType.BGR
        else:
            feature.type.imageType.colorSpace = ft.ImageFeatureType.RGB
    feature.type.imageType.width = width
    feature.type.imageType.height = height
    
def update_multiarray_to_float32(feature):
    if feature.type.HasField("multiArrayType"):
        feature.type.multiArrayType.dataType = ft.ArrayFeatureType.FLOAT32
        
