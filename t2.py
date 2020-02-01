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

# if __name__ == '__main__':
#     rect1 = (661, 27, 679, 47)
#     # (top, left, bottom, right)
#     rect2 = (662, 27, 682, 47)
#     iou = compute_iou(rect1, rect2)
#     print(iou)

vcocopkl=open('Trainval_GT_VCOCO_with_pose.pkl','rb')
xpkl=pickle.load(vcocopkl)

vcocojson= open("instances_vcoco_all_2014.json")
xjson=json.load(vcocojson)

ourclas= open("our_coco_object_classes.json")
ourcls=json.load(ourclas)
print (ourcls["surfboard"])

pkl_image_id=xpkl[0][0]
json_ann=xjson['annotations']
json_cls=xjson['categories']


iou_result=[]
cls_result=[]
max_ind=0
max_iou=0
max_cls=0
print (pkl_image_id)
print (xpkl[0])
pbbox=xpkl[0][3]


for i in range(len(json_ann)):
    if json_ann[i]['image_id']==pkl_image_id:
        jbbox=json_ann[i]['bbox']
        jbbox[2]=jbbox[0]+jbbox[2]
        jbbox[3]=jbbox[1]+jbbox[3]
        # print (jbbox)
        iou=compute_iou(jbbox,pbbox)
        if iou>0:
            iou_result.append(iou) #iou_result
            cls_result.append(json_ann[i]['category_id']) #cls_result
            # max_iou=max(iou_result)
            if iou>max_iou:
                max_iou=iou
                max_cls=json_ann[i]['category_id']
                max_ind=i
fname=""
for i in range(len(json_cls)):
    if json_cls[i]['id']==max_cls:
        fname=json_cls[i]['name']

finde=ourcls[fname]


print (iou_result)
print (fname)
print (finde)









