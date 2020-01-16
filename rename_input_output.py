from  coremltools import  utils

spec = utils.load_spec("")

utils.rename_feature(spec,"UglyInputName","Image",rename_outputs = False)
utils.rename_feature(spec,"UglyOutputName","prediction",rename_inputs = False)
#save the model
utils.save_spec(spec,"")#your model name
