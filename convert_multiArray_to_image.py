import  coremltools
import  coremltools.proto.FeatureTypes_pb2 as ft

spec = coremltools.utils.load_spec("")
input = spec.description.input[0]
input.type.imageType.colorSpace = ft.ImageFeatureType.RGB
input.type.imageType.height = 224
input.type.imageType.width = 224
coremltools.utils.save_spec(spec,"")