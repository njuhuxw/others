
import json
import pickle

vcocopkl=open('Test_Faster_RCNN_R-50-PFN_2x_VCOCO.pkl','rb')
xpkl=pickle.load(vcocopkl)
dict=list(xpkl.keys())

ourclas= open("our_coco_object_classes.json")
ourcls=json.load(ourclas)

objlist= open("object_list.json")
obj_list=json.load(objlist)
kk=list(obj_list.keys())

final_result = {}
num=0
# print (len(xpkl))

# for k in [565248]:
for k in dict:
    print (k)
    newpkl = xpkl[k]
    pkl_image_id = k
    # print (len(newpkl))
    for m in range(len(newpkl)):
        fid=newpkl[m][4]
        fname="-1"
        for i in range(len(kk)):
            if obj_list[kk[i]]==fid:
                fname=kk[i]
            if fname == "hot dog":
                fname = "hot_dog"

            if fname == "wine glass":
                fname = "wine_glass"

            if fname == "cell phone":
                fname = "cell_phone"

            if fname == "fire hydrant":
                fname = "fire_hydrant"

            if fname == "traffic light":
                fname = "traffic_light"

            if fname == "baseball bat":
                fname = "baseball_bat"

            if fname == "potted plant":
                fname = "potted_plant"

            if fname == "teddy bear":
                fname = "teddy_bear"

            if fname == "tennis racket":
                fname = "tennis_racket"

            if fname == "dining table":
                fname = "dining_table"

            if fname == "parking meter":
                fname = "parking_meter"

            if fname == "sports ball":
                fname = "sports_ball"

            if fname == "baseball glove":
                fname = "baseball_glove"

            if fname == "stop sign":
                fname = "stop_sign"

            if fname == "hair drier":
                fname = "hair_drier"

        if fname=="-1":
            num += 1
            print (str(k)+" "+str(m)+" out")
            continue

        finde = ourcls[fname]
        newpkl[m][4]=finde
        # print ("key:"+str(fname)+ " value: "+str(finde))
    final_result[k]=newpkl

# print (final_result)

print ("@@#$write...")
with open('Test2_Faster_RCNN_R-50-PFN_2x_VCOCO.pkl', 'wb+') as f:
    pickle.dump(final_result, f)
f.close()

# output2 = open('Trainval_Neg4_VCOCO_with_pose.pkl', 'rb')
# a = pickle.load(output2)

print ("overhuxw")





