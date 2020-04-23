import onnx

model = onnx.load("torch_model_20191205.onnx")

# check that the IR is well formed
onnx.checker.check_model(model)

onnx.helper.printable_graph(model.graph)