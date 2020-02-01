import json
import pickle

res={}
f = open("object_list.txt")
t=0
for line in f:
    k=line.strip()
    res[k] = t
    t+=1


# j = json.load(file)
# ann=j['categories']


print ("#E#$#@")
print(res)
with open("./object_list.json","w+") as f:
    json.dump(res,f)

print("over")

