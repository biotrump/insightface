import face_model
import argparse
import cv2
import sys
import numpy as np

parser = argparse.ArgumentParser(description='face model test')
# general

#mxnet model path : 
#--model path_to_prefix,epoch 
#https://mxnet.incubator.apache.org/api/python/model.html
parser.add_argument('--image-size', default='112,112', help='')
parser.add_argument('--model', default='', help='path to load model.')
parser.add_argument('--ga-model', default='', help='path to load model.')
parser.add_argument('--gpu', default=0, type=int, help='gpu id')
parser.add_argument('--cpu', default=1, type=int, help='cpu id')
parser.add_argument('--det', default=0, type=int, help='mtcnn option, 1 means using R+O, 0 means detect from begining')
parser.add_argument('--flip', default=0, type=int, help='whether do lr flip aug')
parser.add_argument('--threshold', default=1.24, type=float, help='ver dist threshold')
args = parser.parse_args()
print args
#default is cpu only
print("args.cpu=",args.cpu)
print("args.gpu=",args.gpu)
model = face_model.FaceModel(args)
print ("model=", model)
img = cv2.imread('Tom_Hanks_54745.png')
#crop the face roi and align the face roi before face recognition
img = model.get_input(img)
print ("img=",img)

#face embed model
f1 = model.get_feature(img)
print("face emed feature=", f1[0:10])

#face embed feature can't work with gender, age model in the same time
#gender, age = model.get_ga(img)
#print("gender=", gender)
#print("age=", age)

#sys.exit(0)
#img = cv2.imread('/raid5data/dplearn/megaface/facescrubr/112x112/Tom_Hanks/Tom_Hanks_54733.png')
img = cv2.imread('/home/thomas/ai/face/mxnet/insightface/deploy/Tom_Hanks_54745.png')
#crop the face roi and align the face roi before face recognition
img = model.get_input(img)
print ("img2=",img)
f2 = model.get_feature(img)
dist = np.sum(np.square(f1-f2))
print("dist=", dist)
sim = np.dot(f1, f2.T)
print("sim=",sim)
#diff = np.subtract(source_feature, target_feature)
#dist = np.sum(np.square(diff),1)
