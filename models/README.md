Put pretrained models here
get the pretrained model: https://drive.google.com/open?id=1x0-EiYX9jMUKiq-n1Bd9OCK4fVB3a54v
Where is the model?
models/model-r50-am-lfw/model-r50-am-lfw.zip
unzip it : model-0000.params, model-symbol.json, log
Specify the model: 
--ga-model to specify the gender and age feature
--model to specify the face embed feature

--ga-model /path_to/insightface/models/model-r50-am-lfw/model,0 --model /path_to/insightface/models/model-r50-am-lfw/model,0