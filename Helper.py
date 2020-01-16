import  numpy as np
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