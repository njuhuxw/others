import shutil

f = open('vcoco_trainval.ids');
# come from train
for line in f:
    k = line.strip()
    print(k)

    length = len(k)
    if length == 1:
        name = "00000000000" + k
    if length == 2:
        name = "0000000000" + k
    if length == 3:
        name = "000000000" + k
    if length == 4:
        name = "00000000" + k
    if length == 5:
        name = "0000000" + k
    if length == 6:
        name = "000000" + k
    if length == 7:
        name = "00000" + k
    if length == 8:
        name = "0000" + k

    src = "/home/magus/dataset3/coco2014/train2014/COCO_train2014_" + name + ".jpg"
    dst = "/home/magus/dataset3/coco2014/trainval/COCO_train2014_" + name + ".jpg"
    shutil.copyfile(src, dst)

# test = "000000014219"
# src = "/Users/huxinwen/Desktop/a/COCO_train2014_" + test + ".jpg"
# dst = '/Users/huxinwen/Desktop/b/bg.jpg'
# shutil.copyfile(src, dst)

print('ok')
