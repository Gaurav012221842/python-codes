dict2={}
dict1={1:4,5:7,8:9,10:11}
t=(4,5,6,7)
m=list(dict1.items())
y=list(t)
for index,i in enumerate(y):
    dict2[i]={m[index][0]:m[index][1]}
print(dict2)    