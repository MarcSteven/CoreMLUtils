import  coremltools
import numpy as np
from PIL import  Image
from Helper import printTop5
img = Image.open("")

model = coremltools.models.MLModel("")
spec = model._spec
img_width = spec.description.input[0].type.imageType.width
img_height = spec.description.input[0].type.imageType.height
img = img.resize((img_width,img_height),Image.BILINEAR)
input_name = spec.description.input[0].name
y = model.predict({input_name:img},usesCPUOnly=True)
y.keys()
printTop5(y["classLabelProbs"])

