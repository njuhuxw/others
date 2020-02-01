import pickle
from random import random
from time import sleep

import h5py
import COCO_CLASSES
import HICO_CLASSES
import numpy as np

# 数据转化, background-->background;traffic light-->traffic_light
coco_classes = ["_".join(i.strip().split(" ")) for i in COCO_CLASSES.COCO_CLASSES]

hico_classes = [i for i in HICO_CLASSES.HICO_CLASSES]

# 读取pkl
train_GT_HICO = "train_GT_HICO.pkl"
hicoes = pickle.load(open(train_GT_HICO, "rb"), encoding='iso-8859-1')
# id 去重
hico_unique_ids = list(set([i[0] for i in hicoes]))

file = h5py.File('SELECTED_HICO_final.hdf5', 'w')  # 创建一个h5文件，文件指针是file
print(hico_unique_ids)

for hico_unique_id in hico_unique_ids:
    file.create_group("HICO_test2015_" + str(hico_unique_id).zfill(8))
    boxes_score = [[] for i in coco_classes]  # [[[0,0,0,0,1]][][][][]]
    start_end = [[] for i in coco_classes]
    for hico in hicoes:
        hico_id = hico[0]  # id
        hico_class_ids = hico[1]  # hoi
        hico_person = hico[2]  # person
        hico_object = hico[3]  # object
        if hico_unique_id == hico_id:
            hico_class_chs = []
            for hico_class_id in hico_class_ids:
                hico_class_chs.append(hico_classes[hico_class_id - 1])  # 错位 -1
            hico_class_chs = list(set(hico_class_chs))
            for hico_class_ch in hico_class_chs:
                if (hico_person + [1]) not in boxes_score[1]:
                    boxes_score[1].append(hico_person + [1])
                if (hico_object + [1]) not in boxes_score[coco_classes.index(hico_class_ch)]:
                    boxes_score[coco_classes.index(hico_class_ch)].append(hico_object + [1])
    start_end_idx = 0
    for i in range(len(boxes_score)):
        if len(boxes_score[i]) == 0:
            boxes_score[i].append([random()*0.0001, random()*0.0001, random()*0.0001, random()*0.0001, 1])
            start_end[i] = [start_end_idx, start_end_idx + 1]
            start_end_idx += 1
        else:
            start_end[i] = [start_end_idx, start_end_idx + len(boxes_score[i])]
            start_end_idx += len(boxes_score[i])
    boxes_score_result = []
    for i in boxes_score:
        for j in i:
            boxes_score_result.append(j)
    # file.create_dataset(str(hico_unique_id) + '/boxes_scores_rpn_ids', shape=(len(boxes_score_result), 5))
    # file.create_dataset(str(hico_unique_id) + '/start_end_ids', shape=(81, 2))
    file["HICO_test2015_" + str(hico_unique_id).zfill(8) + '/boxes_scores_rpn_ids'] = boxes_score_result
    file["HICO_test2015_" + str(hico_unique_id).zfill(8) + '/start_end_ids'] = start_end
file.close()

# # HDF5的写入：
# imgData = np.zeros((30, 3, 128, 256))
# f = h5py.File('HDF5_FILE.h5', 'w')  # 创建一个h5文件，文件指针是f
# f['data'] = imgData  # 将数据写入文件的主键data下面
# f['labels'] = range(100)  # 将数据写入文件的主键labels下面
# f.close()  # 关闭文件
