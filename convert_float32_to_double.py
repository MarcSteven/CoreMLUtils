
import coremltools
from coremltools.proto import FeatureTypes_pb2 as ft

model = coremltools.model.MLModel('FacialExpressionAnalysis.mlmodel')
spec = model.get_spec()




def convert_float_to_double(feature):

    if feature.type.HasField('multiArrayType'):
        feature.type.multiArrayType.dataType = ft.arrayFeatureType.arryDataType.double
        
    
    for output_ in spec.description.output:
    
        convert_float_to_double(output_)
 
    model = coremltools.model.MLModel(spec)
    model.save('FacialExpressionAnalysis.mlmodel')
 

