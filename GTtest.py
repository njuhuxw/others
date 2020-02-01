import pickle
import json
def compute_iou(rec1, rec2):
    """
    computing IoU
    :param rec1: (y0, x0, y1, x1), which reflects
            (top, left, bottom, right)
    :param rec2: (y0, x0, y1, x1)
    :return: scala value of IoU
    """
    # computing area of each rectangles
    S_rec1 = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1])
    S_rec2 = (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])

    # computing the sum_area
    sum_area = S_rec1 + S_rec2

    # find the each edge of intersect rectangle
    left_line = max(rec1[1], rec2[1])
    right_line = min(rec1[3], rec2[3])
    top_line = max(rec1[0], rec2[0])
    bottom_line = min(rec1[2], rec2[2])

    # judge if there is an intersect
    if left_line >= right_line or top_line >= bottom_line:
        return 0
    else:
        intersect = (right_line - left_line) * (bottom_line - top_line)
        return (intersect / (sum_area - intersect)) * 1.0

vcocopkl=open('Trainval_GT_VCOCO_with_pose.pkl','rb')
xpkl=pickle.load(vcocopkl)

vcocojson= open("instances_vcoco_all_2014.json")
xjson=json.load(vcocojson)

ourclas= open("our_coco_object_classes.json")
ourcls=json.load(ourclas)

json_ann=xjson['annotations']
json_cls=xjson['categories']


# print (pkl_image_id)
# print (xpkl[0])

final_result = []
num=0
# print (len(xpkl))
for k in range(len(xpkl)):
    newpkl = xpkl[k]
    pkl_image_id = xpkl[k][0]
    pbbox = xpkl[k][3]
    iou_result = []
    cls_result = []
    max_ind = 0
    max_iou = 0
    max_cls = 0
    finde=-1
    for i in range(len(json_ann)):
        if json_ann[i]['image_id'] == pkl_image_id:
            jbbox = json_ann[i]['bbox']
            jbbox[2] = jbbox[0] + jbbox[2]
            jbbox[3] = jbbox[1] + jbbox[3]
            # print (jbbox)
            iou = compute_iou(jbbox, pbbox)
            if iou > 0:
                iou_result.append(iou)  # iou_result
                cls_result.append(json_ann[i]['category_id'])  # cls_result
                # max_iou=max(iou_result)
                if iou > max_iou:
                    max_iou = iou
                    max_cls = json_ann[i]['category_id']
                    max_ind = i
    fname = ""
    for i in range(len(json_cls)):
        if json_cls[i]['id'] == max_cls:
            fname = json_cls[i]['name']
            if fname=="hot dog":
                fname="hot_dog"

            if fname == "wine glass":
                fname="wine_glass"

            if fname=="cell phone":
                fname="cell_phone"

            if fname=="fire hydrant":
                fname="fire_hydrant"

            if fname=="traffic light":
                fname="traffic_light"

            if fname=="baseball bat":
                fname="baseball_bat"

            if fname=="potted plant":
                fname="potted_plant"

            if fname=="teddy bear":
                fname="teddy_bear"

            if fname=="tennis racket":
                fname="tennis_racket"

            if fname=="dining table":
                fname="dining_table"

            if fname=="parking meter":
                fname="parking_meter"

            if fname=="sports ball":
                fname="sports_ball"

            if fname=="baseball glove":
                fname="baseball_glove"

            if fname=="stop sign":
                fname="stop_sign"

            if fname=="hair drier":
                fname="hair_drier"

    finde = ourcls[fname]

    # print (iou_result)
    # print (fname)
    # print (finde)
    if finde==-1:
        num+=1

    newpkl.append(finde)
    final_result.append(newpkl)
    print (k)


# print (final_result)
# print ("@@#$")
with open('Trainval_GT3_VCOCO_with_pose.pkl', 'wb+') as f:
    pickle.dump(final_result, f)
f.close()

output2 = open('Trainval_GT3_VCOCO_with_pose.pkl', 'rb')
a = pickle.load(output2)

print ("overhuxw")
print ("num:")
print (num)





