import pickle
import json


vcocopkl=open('Trainval_Neg4_VCOCO_with_pose.pkl','rb')
xpkl=pickle.load(vcocopkl)


a1=open('object_list.json','rb')
j1=json.load(a1)
k1=list(j1.keys())

a2=open('our_coco_object_classes.json','rb')
j2=json.load(a2)
k2=list(j2.keys())

print ("object_list is true, but our_coco_object_classes is non-existant:")
for i in k1:
    t=-1
    for j in k2:
        if i==j:
            t=1
            break
    if t==-1:
        print (i)
print ("")
print ("our_coco_object_classes is true, but object_list is non-existant:")

for i in k2:
    t=-1
    for j in k1:
        if i==j:
            t=1
            break
    if t==-1:
        print (i)