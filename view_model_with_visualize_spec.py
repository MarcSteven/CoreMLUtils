import coremltools

model = coremltools.models.MLModel("")#You must give the path of mlmodel here
model.visualize_spec()