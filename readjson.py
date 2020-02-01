import json
def loadFont():
    file = open("our_coco_object_classes.json", encoding='utf-8')
    vcoco_test = json.load(file)
    # a = vcoco_test['annotations'][183192]
    # b = vcoco_test['annotations'][183193]
    # c = vcoco_test['annotations'][183205]
    return vcoco_test
load_test = loadFont()
json_str = json.dumps(load_test)
# print(type(load_test))
# print("Python 原始数据：", repr(load_test))
print("JSON 对象：", load_test)

