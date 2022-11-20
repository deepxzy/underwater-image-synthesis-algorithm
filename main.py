import cv2
import os
from utils import *
import numpy as np
from tqdm import trange
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root_img', type=str, default='', help='the root of RGB images')
parser.add_argument('--root_deep', type=str, default='', help='the root of deepth images')
parser.add_argument('--root_save', type=str, default='', help='the root of synthesised underwater images')
parser.add_argument('--atmospheric', type=float, default=0.8, help='the value of global atmospheric light')
parser.add_argument('--watertype', type=int, default=5, help='watertype, from 1 to 10')

opt = parser.parse_args()

root_img=opt.root_img
root_deep=opt.root_deep
root_save=opt.root_save

if not os.path.exists(root_save):
    os.makedirs(root_save)

img_list=os.listdir(root_img)
deep_list=os.listdir(root_deep)
A=opt.atmospheric
watertype=opt.watertype

for i in trange(len(img_list)):
    depth_img=cv2.imread(os.path.join(root_deep, deep_list[i]),0)
    img=cv2.imread(os.path.join(root_img, img_list[i]))

    depth=value_to_deep(depth_img,0.5,10)

    n=water_type(watertype)
    B=n[0]**depth
    G=n[1]**depth
    R=n[2]**depth

    B = np.expand_dims(B, axis=2)
    G = np.expand_dims(G, axis=2)
    R = np.expand_dims(R, axis=2)

    t=np.concatenate([B,G,R],axis=2)

    final=img*t+A*(1-t)
    cv2.imwrite(os.path.join(root_save,img_list[i]),final)

