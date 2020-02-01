f = open('vcoco_test.ids');
# t=open('coco_test.txt', 'w+')

# come from train
list=[]
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

    final="COCO_val2014_"+name+".jpg"
    list.append(final)


    with open('coco_test.txt', 'a') as t:
        t.write(final)
        t.write('\n')


print('ok')