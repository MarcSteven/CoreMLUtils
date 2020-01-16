import  coremltools
import  coremltools.proto.FeatureTypes_pb2 as ft

spec = coremltools.utils.load_spec("")
output = spec.description.output[0]

output.type.imageType.colorSpace = ft.ImageFeatureType.RGB
output.type.imageType.width = 150
output.type.imageType.height = 300

coremltools.utils.save_spec(spec,"")